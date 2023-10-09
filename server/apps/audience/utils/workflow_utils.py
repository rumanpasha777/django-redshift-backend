from django.conf import settings


def get_audit_data(
        resource: str,
        resource_id: str,
        action: str,
        raw_data: dict,
        session_id: str = None,   # todo
        user_id: str = None,
        system_action: bool = False
) -> dict:
    return {
        "resource": resource,
        "resource_id": resource_id,
        "resource_action_type": action,
        "raw_data": raw_data,
        "user_id": user_id,
        "session_id": session_id,
        "is_system_action": system_action,
        "timestamp": str(settings.TS_NOW()),
    }
