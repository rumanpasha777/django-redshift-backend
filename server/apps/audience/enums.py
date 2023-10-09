from apps.core.enums import AppEnum


class PlatformsEnum(AppEnum):
    META = 'META'
    TIKTOK = 'TIKTOK'
    PINTEREST = 'PINTEREST'
    SNAPCHAT = 'SNAPCHAT'
    ADELPHIC = 'ADELPHIC'
    AMAZON = 'AMAZON'
    THE_TRADE_DESK = 'THE_TRADE_DESK'
    TWITTER = 'TWITTER'
    YAHOO = 'YAHOO'
    DV360 = 'DV360'
    JUN_GROUP = 'JUN_GROUP'
    LINKEDIN = 'LINKEDIN'
    MICROSOFT_BING = 'MICROSOFT_BING'
    ROKU = 'ROKU'
    SAMSUNG_ADS = 'SAMSUNG_ADS'
    WALMART = 'WALMART'


class PlatformUploadTypeEnum(AppEnum):
    DMO = 'DMO'  # direct
    DMP = 'DMP'


class JobRunStatusType(AppEnum):
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class JobPlatformStatusType(AppEnum):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    PUBLISHED = 'PUBLISHED'
    ERRORED = 'ERRORED'


class ResourceActionTypeEnum(AppEnum):
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'


class ResourceNameEnum(AppEnum):
    PUBLISH_JOB = 'PUBLISH_JOB'


UploadTypeSupportedPlatforms = {
    PlatformUploadTypeEnum.DMO.value: [
        PlatformsEnum.ADELPHIC.value,
        PlatformsEnum.AMAZON.value,
        PlatformsEnum.META.value,
        PlatformsEnum.PINTEREST.value,
        PlatformsEnum.SNAPCHAT.value,
        PlatformsEnum.THE_TRADE_DESK.value,
        PlatformsEnum.TIKTOK.value,
        PlatformsEnum.TWITTER.value,
        PlatformsEnum.YAHOO.value,
    ],
    PlatformUploadTypeEnum.DMP.value: [
        PlatformsEnum.AMAZON.value,
        PlatformsEnum.META.value,
        PlatformsEnum.PINTEREST.value,
        PlatformsEnum.SNAPCHAT.value,
        PlatformsEnum.THE_TRADE_DESK.value,
        PlatformsEnum.TIKTOK.value,
        PlatformsEnum.TWITTER.value,
        PlatformsEnum.YAHOO.value,
        PlatformsEnum.DV360.value,
        PlatformsEnum.JUN_GROUP.value,
        PlatformsEnum.LINKEDIN.value,
        PlatformsEnum.MICROSOFT_BING.value,
        PlatformsEnum.ROKU.value,
        PlatformsEnum.SAMSUNG_ADS.value,
        PlatformsEnum.WALMART.value,
    ]
}
