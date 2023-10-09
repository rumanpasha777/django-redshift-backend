from typing import List


class PublishJobException(Exception):

    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return f"PublishJobException: {self.errors}"
