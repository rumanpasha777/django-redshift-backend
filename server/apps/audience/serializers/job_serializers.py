from rest_framework import serializers

from apps.audience.enums import PlatformsEnum, PlatformUploadTypeEnum
from apps.core.serializers import BaseSerializer


class PlatformUploadTypeSerializer(BaseSerializer):
    platform = serializers.ChoiceField(choices=PlatformsEnum.choices(), allow_null=False, allow_blank=False)
    upload_type = serializers.ChoiceField(choices=PlatformUploadTypeEnum.choices(), allow_null=False, allow_blank=False)


class CreateJobSerializer(BaseSerializer):
    segment_id = serializers.UUIDField(required=True, allow_null=False)
    job_name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    platforms = serializers.ListField(
        child=PlatformUploadTypeSerializer(many=True, required=True),
        allow_null=False,
        allow_empty=False
    )
