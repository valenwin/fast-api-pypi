from typing import List


def release_count() -> int:
    return 100


def package_count() -> int:
    return 1000000


def latest_package_releases(limit: int = 10) -> List:
    return [
               {'id': 'fastapi', 'summary': "A great web framework"},
               {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
               {'id': 'aiohttp', 'summary': "Great for an async world"},
           ][:limit]
