from django.db import models

from apps.core.models import BaseModel
from apps.audience.enums import ResourceActionTypeEnum, ResourceNameEnum


class WorkflowAudit(BaseModel):
    resource = models.CharField(max_length=100, choices=ResourceNameEnum.choices())
    resource_id = models.UUIDField(blank=False, null=False)
    resource_action_type = models.CharField(max_length=20, choices=ResourceActionTypeEnum.choices())
    raw_data = models.JSONField(null=False, blank=False)
    user_id = models.CharField(max_length=100, null=True)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    is_system_action = models.BooleanField(default=False)
    timestamp = models.DateTimeField()

    @classmethod
    async def create_audit_record(cls, data: dict) -> ['WorkflowAudit']:
        return await cls.objects.acreate(**data)
