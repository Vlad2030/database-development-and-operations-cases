import typing

from models import PetsDatabase
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class PetsCRUD:
    def __init__(self, session) -> None:
        self.session: AsyncSession = session

    async def create(
            self,
            name: str = None,
            age: int = None,
            type: str = None,
            breed: str = None,
    ) -> None:
        new_values = {}
        if name is not None:
            new_values["name"] = name
        if age is not None:
            new_values["age"] = age
        if type is not None:
            new_values["type"] = type
        if breed is not None:
            new_values["breed"] = breed
        query = insert(PetsDatabase).values(**new_values)
        await self.session.execute(query)
        await self.session.commit()

    async def update(
            self,
            name: str = None,
            age: int = None,
            type: str = None,
            breed: str = None,
    ) -> None:
        update_values = {}
        if name is not None:
            update_values["name"] = name
        if age is not None:
            update_values["age"] = age
        if type is not None:
            update_values["type"] = type
        if breed is not None:
            update_values["breed"] = breed
        query = update(PetsDatabase).values(**update_values)
        await self.session.execute(query)
        await self.session.commit()

    async def delete_by_id(
            self,
            id: int,
    ) -> typing.Union[PetsDatabase, None]:
        query = delete(PetsDatabase).where(PetsDatabase.id==id)
        result = await self.session.execute(query)
        if result is None:
            return result
        await self.session.flush()
        await self.session.commit()
        return result

    async def get_all(self) -> typing.List[PetsDatabase]:
        query = select(PetsDatabase)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_id(
            self,
            id: int,
    ) -> typing.Union[PetsDatabase, None]:
        query = select(PetsDatabase).where(PetsDatabase.id==id)
        result = await self.session.execute(query)
        response = result.scalars().first()
        return response
