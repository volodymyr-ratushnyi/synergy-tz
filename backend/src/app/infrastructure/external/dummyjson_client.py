from typing import Any

import httpx

from app.core.exceptions import AppError


class DummyJsonClient:
    def __init__(self, base_url: str, timeout: float) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout

    async def fetch_users(self) -> list[dict[str, Any]]:
        return await self._fetch_resource("/users", "users")

    async def fetch_posts(self) -> list[dict[str, Any]]:
        return await self._fetch_resource("/posts", "posts")

    async def _fetch_resource(self, path: str, key: str) -> list[dict[str, Any]]:
        url = f"{self._base_url}{path}"
        try:
            async with httpx.AsyncClient(timeout=self._timeout) as client:
                response = await client.get(url, params={"limit": 0})
                response.raise_for_status()
                data = response.json()
                return data[key]
        except httpx.TimeoutException as exc:
            raise AppError(
                f"External API timeout while fetching {key}",
                status_code=504,
            ) from exc
        except httpx.HTTPStatusError as exc:
            raise AppError(
                f"External API returned {exc.response.status_code} for {path}",
                status_code=502,
            ) from exc
        except httpx.HTTPError as exc:
            raise AppError(
                f"Failed to fetch {key} from external API",
                status_code=502,
            ) from exc
