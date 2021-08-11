from typing import List

from fastapi import Request
from viewmodels.shared.viewmodel import ViewModelBase

import services.user_service as user_service
import services.package_service as package_service


class IndexViewModel(ViewModelBase):

    def __init__(self, request: Request):
        super().__init__(request)
        self.user_count: int = user_service.users_count()
        self.release_count: int = package_service.release_count()
        self.package_count: int = package_service.package_count()
        self.packages: List = package_service.latest_package_releases()
