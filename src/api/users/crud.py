# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select
# from sqlalchemy.engine import Result
#
# from src.models.user import User
# from .schemas import UserSchema, UserCreateSchema
# from .utils import hash_password
#
#
# async def get_users(session: AsyncSession) -> list[User]:
#     query = select(User).order_by(User.id)
#     result: Result = await session.execute(query)
#     users = result.scalars().all()
#     return list(users)
#
#
# async def create_user(session: AsyncSession, user_in: UserCreateSchema) -> User:
#     hashed_password = await hash_password(user_in.password)
#     user = User(
#         **user_in.model_dump(exclude={"password"}),
#         password=hashed_password,
#     )
#     session.add(user)
#     await session.commit()
#     return user
