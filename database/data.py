import enum

import utils


class Database(enum.Enum):
    def __str__(self) -> str:
        return str(self.value)

    DATABASE_HOST = utils.Environs.get("POSTGRES_CONTAINER_HOST")
    DATABASE_PORT = utils.Environs.get("POSTGRES_CONTAINER_PORT")
    DATABASE_DB = utils.Environs.get("POSTGRES_DB")
    DATABASE_USER = utils.Environs.get("POSTGRES_USER")
    DATABASE_PASSWORD = utils.Environs.get("POSTGRES_PASSWORD")
