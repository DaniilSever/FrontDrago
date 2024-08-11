# import asyncpg
from pydantic_settings import BaseSettings
# from contextlib import asynccontextmanager
from uuid import UUID
from .dto import QCreateAccount, QUpdateAccount, UUID4
from .dto import XOk, XAccount, XAccountCreated

from random import randint
class AccountRepo:
    
    def __init__(self, cfg: BaseSettings):
        # сборка конфигурации подключения к БД
        self.cfg = cfg
        # self.dsn = "postgresql://{usr}:{pwd}@{host}:{port}/{db}".format(
        #     usr=self.cfg.POSTGRES_USER,
        #     pwd=self.cfg.POSTGRES_PASSWORD,
        #     host=self.cfg.POSTGRES_HOST,
        #     port=self.cfg.POSTGRES_PORT,
        #     db=self.cfg.POSTGRES_DBN,
        # )
        self._pool = None

    # асинхронный контекстный менеджер для получения соединения с БД
    # @property
    # @asynccontextmanager
    # async def pool(self):
    #     if not self._pool:
    #         self._pool = await asyncpg.create_pool(
    #             self.dsn, min_size=1, max_size=2, max_inactive_connection_lifetime=500.0
    #         )
    #     yield self._pool


    async def get_all_accounts(self) -> list:
        # запрос в бд
        # async with self.pool as p, p.acquire() as cn:
        #     conn: asyncpg.Connection = cn
        #     q = """
        #     SELECT 
        #         a.id
        #         , a.email
        #         , a.name
        #         , a.password
        #     FROM accounts as a
        #     LIMIT 100
        #     """
        #     accounts = await conn.fetch(q)
        #     return accounts

        return [ # TODO: ЭТО ТЕСТОВАЯ ЗАЛУПА ИБО БД НЕ ПОДКЛЮЧЕНА
            {
                "uid": UUID("592af5b5-4f60-4ddd-b080-be674c82eda8"),
                "email": "example@example.com",
                "name": "username",
                "password": "password123",
            },
            {
                "uid": UUID("592af5b5-4f60-4ddd-b080-be674c82eda8"),
                "email": "example2@example.com",
                "name": "username",
                "password": "password456",
            },
            {
                "uid": UUID("592af5b5-4f60-4ddd-b080-be674c82eda8"),
                "email": "example3@example.com",
                "name": "username",
                "password": "password789",
            },
        ]

    async def get_account_by_id(self, req: UUID4) -> XAccount:
        # запрос в бд
        # async with self.pool as p, p.acquire() as cn:
        #     conn: asyncpg.Connection = cn
        #     q = """
        #         SELECT 
        #             a.id
        #             , a.email
        #             , a.name 
        #             , a.password    
        #         FROM accounts AS a
        #         WHERE a.uid=($1)
        #     """
        #     try:
        #         account = await conn.fetchrow(q, req.uid)
        #     except asyncpg.exceptions.DataError:
        #         raise KeyError("invalid uid")

        #     if account is None:
        #         raise ValueError("account not found")

        #     return XAccount(*account)

        match randint(0, 2): # TODO: ЭТО ТЕСТОВАЯ ЗАЛУПА ИБО БД НЕ ПОДКЛЮЧЕНА
            case 0:
                raise KeyError("invalid uid") 
            case 1:
                return XAccount(
                    uid=UUID("592af5b5-4f60-4ddd-b080-be674c82eda8"),
                    email="example@example.com",
                    name="username",
                    password="password123",
                )
            case 2:
                raise ValueError("account not found")

    async def create_account(self, req: QCreateAccount) -> XAccountCreated:
        # запрос в бд
        # async with self.pool as p, p.acquire() as cn:
        #     conn: asyncpg.Connection = cn
        #     q = """
        #         INSERT INTO accounts (
        #             email
        #             , name
        #         )
        #         VALUES ($1, $2)
        #         RETURNING uid;
        #     """
        #     args = [req.email, req.name]
        #     try:
        #         uid = await conn.fetchval(q, *args)
        #     except asyncpg.exceptions.UniqueViolationError:
        #         raise KeyError("email busy")
        #     return XAccountCreated(uid=uid)

        match randint(0, 1): # TODO: ЭТО ТЕСТОВАЯ ЗАЛУПА ИБО БД НЕ ПОДКЛЮЧЕНА
            case 0:
                raise KeyError("email busy")
            case 1:
                return XAccountCreated( 
                    uid=UUID("592af5b5-4f60-4ddd-b080-be674c82eda8"),
                )
    
    async def update_account(self, uid: UUID4, req: QUpdateAccount) -> XOk:
        # запрос в бд
        # async with self.pool as p, p.acquire() as cn:
        #     conn: asyncpg.Connection = cn
        #     q = """
        #         UPDATE accounts 
        #         SET (
        #             email
        #             , name
        #         ) = ($2, $3)
        #         WHERE uid=($1)
        #         RETURNING uid;
        #     """
        #     args = [req.email, req.name]
        #     try:
        #         res = await conn.fetchval(q, uid, *args)
        #     except asyncpg.exceptions.DataError:
        #         raise KeyError("invalid uid")

        #     if res is None:
        #         raise ValueError("account not found")
        #     else:
        #         return XOk

        match randint(0, 2): # TODO: ЭТО ТЕСТОВАЯ ЗАЛУПА ИБО БД НЕ ПОДКЛЮЧЕНА
            case 0:
                raise KeyError("invalid uid") 
            case 1:
                return XOk(message="success")
            case 2:
                raise ValueError("account not found")

        
    
    async def delete_account(self, uid: UUID4) -> XOk:
        # запрос в бд
        # async with self.pool as p, p.acquire() as cn:
        #     conn: asyncpg.Connection = cn
        #     q = """
        #         DELETE
        #         FROM accounts AS a 
        #         WHERE a.uid=($1)
        #     """

        #     try:
        #         res = await conn.execute(q, uid)
        #     except asyncpg.exceptions.DataError:
        #         raise KeyError("invalid uid")

        #     if res == "DELETE 0":
        #         return {"message": "account not found"}
        #     else:
        #         return XOk

        match randint(0, 1): # TODO: ЭТО ТЕСТОВАЯ ЗАЛУПА ИБО БД НЕ ПОДКЛЮЧЕНА
            case 0:
                raise KeyError("invalid uid") 
            case 1:
                return XOk(message="success")