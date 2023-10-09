from typing import List, Optional, Dict, Mapping
from django.db import models

from apps.core.models import BaseModel
from apps.audience.enums import PlatformsEnum, JobPlatformStatusType, ResourceActionTypeEnum, JobRunStatusType, \
    PlatformUploadTypeEnum


class Job(BaseModel):
    job_name = models.CharField(max_length=300)
    segment_id = models.UUIDField(null=False, blank=False)
    is_audience_refresh = models.BooleanField(null=False, default=False)
    user_id = models.CharField(max_length=100, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['segment_id', 'job_name'],
                name='UniqueSegmentJob',
            )
        ]

    def __str__(self):
        return f'Job - {self.job_name} - Segment id[{self.segment_id}]'

    @classmethod
    async def get_from_id(
            cls,
            job_id: str,
            raise_exception: bool = False,
    ) -> Optional['Job']:
        return await cls.base_aget_from_field(
            field_name='pk',
            field_value=job_id,
            raise_exception=raise_exception,
        )

    @classmethod
    async def create_job(
            cls,
            segment_id: str,
            job_name: str,
    ) -> 'Job':
        obj = cls(
            segment_id=segment_id,
            job_name=job_name,
        )
        await obj.asave()
        return obj


class JobPlatformMapping(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.PROTECT, null=False)
    platform = models.CharField(
        choices=PlatformsEnum.choices(),
        null=False,
        max_length=50
    )
    upload_type = models.CharField(
        choices=PlatformUploadTypeEnum.choices(),
        null=False,
        max_length=50
    )
    status = models.CharField(
        choices=JobPlatformStatusType.choices(),
        default=JobPlatformStatusType.PENDING.value,
        max_length=50
    )
    is_retryable = models.BooleanField(default=False)  # todo default value
    retry_after = models.DateTimeField(null=True, blank=True)
    attempts = models.IntegerField(default=0)
    error = models.JSONField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['job', 'platform'],
                name='UniqueJobPlatform',
            )
        ]

    def __str__(self):
        return f'JobPlatformMapping - {self.job.job_name} - Platform[{self.platform}]'

    @classmethod
    async def create_job_platform_mapping(
            cls,
            job_id: str,
            platforms: List[Dict[str, str]],
    ) -> None:
        await cls.objects.abulk_create(
            objs=[
                cls(
                    job_id=job_id,
                    platform=each['platform'],
                    upload_type=each['upload_type'],
                ) for each in platforms
            ],
        )

    @classmethod
    async def fetch_pending_platforms_from_job(cls, job_id: str) -> List[Dict[str, str]]:
        platform_mapping = cls.objects.filter(
            job_id=job_id,
            status__in=[
                JobPlatformStatusType.PENDING.value,
                JobPlatformStatusType.ERRORED.value,
            ],
        )
        data = []
        async for each in platform_mapping:
            data.append({
                "platform": each.platform,
                "upload_type": each.upload_type,
            })
        return data

    async def update_state(
            self,
            state: JobPlatformStatusType,
    ) -> None:
        self.state = state.value
        await self.asave()


class JobTriggerLog(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.PROTECT, null=False)
    job_run_status = models.CharField(
        choices=JobRunStatusType.choices(),
        default=JobRunStatusType.RUNNING.value,
        max_length=50
    )
    platform_config = models.JSONField(null=False)
    error = models.JSONField(null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True)

    @classmethod
    async def create_job_trigger(
            cls,
            job_id: str,
            platform_config: List[Dict[str, str]],
            user_id: Optional[str] = None,
    ) -> 'JobTriggerLog':
        obj = cls(
            job_id=job_id,
            platform_config=platform_config,
            user_id=user_id,
        )
        await obj.asave()
        return obj

    @classmethod
    async def update_job_run_status(cls, job_trigger_id: str, job_run_status: str) -> None:
        await cls.objects.filter(
            id=job_trigger_id
        ).aupdate(
            job_run_status=job_run_status
        )
