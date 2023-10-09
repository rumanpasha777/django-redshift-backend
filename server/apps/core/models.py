from typing import List, Optional, Type, TypeVar, Union
import uuid
from django.db import models

from apps.core.exceptions import ResourceNotFoundException

# For typechecking. Helps type checker keep track of inherited classes
U = TypeVar('U', bound='BaseModel')


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    async def base_aget_from_field(
        cls: Type[U],
        field_name: str,
        field_value: str,
        raise_exception: bool = False,
        filters: Optional[dict] = None,
        select_related: Optional[List[str]] = None,
        prefetch_related: Optional[List[Union[str, models.Prefetch]]] = None,
    ) -> U:
        queryset = cls.objects.filter(**{field_name: field_value})
        if filters is not None:
            queryset = queryset.filter(**filters)
        if select_related is not None:
            queryset = queryset.select_related(*select_related)
        if prefetch_related is not None:
            queryset = queryset.prefetch_related(*prefetch_related)
        object = await queryset.afirst()
        if object is None and raise_exception is True:
            raise ResourceNotFoundException(cls.__name__, field_name, field_value)
        return object
