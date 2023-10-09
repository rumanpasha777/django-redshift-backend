import logging
from typing import List, Dict

from apps.audience.enums import JobRunStatusType, ResourceNameEnum, ResourceActionTypeEnum
from apps.audience.exceptions import PublishJobException
from apps.audience.models import Job, JobPlatformMapping, JobTriggerLog, WorkflowAudit
from apps.audience.serializers.job_serializers import CreateJobSerializer
from apps.audience.utils.workflow_utils import get_audit_data

logger = logging.getLogger(__name__)


class JobService:

    @classmethod
    async def create_job(
        cls,
        segment_id: str,
        job_name: str,
        platforms: List[Dict[str, str]]
    ) -> dict:
        """
        platforms: [
            {
                "platform": "META",
                "upload_type": "DMO",
            }
        ]
        """
        logger_prefix = f'[CreateJob][SID-{segment_id}]'
        logger.info(f'{logger_prefix} Received request to create a job')
        job_data = {
            'segment_id': segment_id,
            'job_name': job_name,
            'platforms': platforms,
        }
        CreateJobSerializer.avalidate_and_map(job_data)
        logger.info(f'{logger_prefix} Creating job')
        job = await Job.create_job(
            segment_id=segment_id,
            job_name=job_name,
        )
        logger.info(f'{logger_prefix} Created job. Job ID: {job.pk}')

        await JobPlatformMapping.create_job_platform_mapping(
            job_id=str(job.pk),
            platforms=platforms,
        )
        logger.info(f'{logger_prefix} Created {len(platforms)} job platform mapping')
        # Audit log
        await WorkflowAudit.create_audit_record(
            get_audit_data(
                resource=ResourceNameEnum.PUBLISH_JOB.value,
                resource_id=str(job.pk),
                action=ResourceActionTypeEnum.CREATE.value,
                raw_data=job_data,
            )
        )
        return {"job_id": str(job.pk)}

    @classmethod
    async def trigger_job(cls, job_id: str) -> None:
        logger_prefix = f'[JID-{job_id}][TriggerJob]'
        logger.info(f'{logger_prefix} Received request to trigger a job')
        job = await Job.get_from_id(job_id=job_id, raise_exception=True)
        job_platform_mapping = await JobPlatformMapping.fetch_pending_platforms_from_job(job_id=str(job.pk))
        logger.info(f'data: {job_platform_mapping}')
        if not job_platform_mapping:
            raise PublishJobException("No Pending Platforms in Job")

        job_trigger = await JobTriggerLog.create_job_trigger(
            job_id=str(job.pk),
            platform_config=job_platform_mapping,

        )
        logger.info(f'{logger_prefix} Triggered job')
        # todo plugin service call
        logger.info(f'{logger_prefix} Job Completed')
        await JobTriggerLog.update_job_run_status(
            job_trigger_id=str(job_trigger.pk),
            job_run_status=JobRunStatusType.COMPLETED.value
        )
        logger.info(f'{logger_prefix} Job trigger status updated')

    @classmethod
    async def run_job(cls, job_id: str):
        ...

    @classmethod
    async def get_job(cls):
        ...

    @classmethod
    async def list_jobs(cls):
        ...
