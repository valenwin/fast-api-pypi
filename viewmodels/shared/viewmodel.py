from typing import Optional
from fastapi import Request


class ViewModelBase:

    def __init__(self, request: Request):
        self.request: Optional[str] = request
        self.error: Optional[str] = None
        self.user_id: Optional[str] = None

    def to_dict(self) -> dict:
        return self.__dict__
