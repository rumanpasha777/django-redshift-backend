from abc import abstractmethod


class BaseException(Exception):

    @abstractmethod
    def config(self):
        pass


class RequestValidationException(BaseException):

    def __init__(self, resource_name, errors):
        self.resource_name = resource_name
        self.errors = errors

    def config(self):
        return {
            'resource_name': self.resource_name,
            'errors': self.errors,
        }

    def __str__(self):
        return f"Request Validation for Resource: {self.resource_name}"


class ResourceNotFoundException(BaseException):

    def __init__(self, resource_name: str, field_name: str, field_value: str):
        self.resource_name = resource_name
        self.field_name = field_name
        self.field_value = field_value

    def config(self):
        return {
            'resource_name': self.resource_name,
            'field_name': self.field_name,
            'field_value': self.field_value,
        }

    def __str__(self):
        return f'Resource {self.resource_name} with {self.field_name} "{self.field_value}" not found'


class ResourceAlreadyExistsException(BaseException):

    def __init__(self, resource_name: str, field_name: str, field_value: str):
        self.resource_name = resource_name
        self.field_name = field_name
        self.field_value = field_value

    def config(self):
        return {
            'resource_name': self.resource_name,
            'field_name': self.field_name,
            'field_value': self.field_value,
        }

    def __str__(self):
        return f'Resource {self.resource_name} with {self.field_name} "{self.field_value}" already exists'
