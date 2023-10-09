import logging
from drf_yasg import openapi
from asgiref.sync import async_to_sync
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from apps.audience.services.job_services import JobService
from apps.core.exceptions import ResourceNotFoundException
from apps.core.serializers import response_200, response_400

logger = logging.getLogger(__name__)

job_id_param = openapi.Parameter(
    'job_id',
    openapi.IN_QUERY,
    description="Job ID",
    type=openapi.TYPE_STRING,
    required=False,
)


class JobViewSet(viewsets.ViewSet):

    @async_to_sync
    @swagger_auto_schema(
        operation_summary="Create a Job",
        tags=['Job Views'],
    )
    async def create_job(self, request):
        """
        Create a Job
        """
        data = request.data
        segment_id = data['segment_id']
        job_name = data['job_name']
        platforms = data['platforms']
        try:
            response = await JobService.create_job(
                segment_id=segment_id,
                job_name=job_name,
                platforms=platforms,
            )
            return response_200(response)
        except ResourceNotFoundException as e:
            return response_400(e)

    @async_to_sync
    @swagger_auto_schema(
        operation_summary="Trigger Job",
        manual_parameters=[job_id_param],
        tags=['Job Views'],
    )
    async def trigger_job(self, request):
        """
        Trigger Job
        """
        job_id = request.GET.get(job_id_param.name)
        try:
            response = JobService.trigger_job(job_id=job_id)
            return response_200(response)
        except ResourceNotFoundException as e:
            return response_400(e)
