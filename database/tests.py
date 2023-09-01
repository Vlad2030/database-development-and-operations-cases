import asyncio
from crud import PetsCRUD
from database import get_async_session, Base, engine
from loguru import logger
import random
import pets_data


pets_amount = 50


async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Pets database created!")

    pets = PetsCRUD(session=await get_async_session())

    for _ in range(pets_amount):
        await pets.create(
            name=random.choice(pets_data.pets_names),
            age=random.randint(1, 20),
            type=random.choice(pets_data.pets_types),
            breed=None,
        )
    logger.success(f"Created {pets_amount} pets!")

    all_database = await pets.get_all()
    print(all_database)
    logger.info("Get all pets!")

    return None


if __name__ == "__main__":
    asyncio.run(main())
