import logging

from asgiref.sync import async_to_sync
from django.core.management.base import BaseCommand

from apps.audience.services.job_services import JobService

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--job',
            type=str,
            help='Pass the job id',
        )

    def handle(self, *args, **options):
        job_id = options.get("job")
        # todo empty job id can be handled at service
        logger.info(f'[Job:{job_id}] Publish Job Triggered')
        try:
            async_to_sync(JobService.trigger_job)(job_id)
        except Exception as e:
            logger.info(f'[Job:{job_id}] Publish Job Failed. {e}')

