import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from conftest import async_session, async_client, event_loop, users, profiles


@pytest.mark.asyncio
async def test_create_users(
    async_client: AsyncClient,
    async_session: AsyncSession,
    users,
    profiles,
):
    responses = []
    for user in users:
        response = await async_client.post(
            "/api/users/auth/register",
            json=users.model_dump(),
        )
        responses.append(response)

    assert all([r.status_code == 201 for r in responses])
