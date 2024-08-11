import asyncpg
from pydantic_settings import BaseSettings
from contextlib import asynccontextmanager
from uuid import UUID
from .dto import QCreateAccount, QUpdateAccount, UUID4
from .dto import XOk, XAccount, XAccountCreated

from random import randint
class AccountRepo:
    
    def __init__(self, cfg: BaseSettings):
        # сборка конфигурации подключения к БД
        self.cfg = cfg
        self.dsn = "postgresql://{usr}:{pwd}@{host}:{port}/{db}".format(
            usr=self.cfg.POSTGRES_USER,
            pwd=self.cfg.POSTGRES_PASSWORD,
            host=self.cfg.POSTGRES_HOST,
            port=self.cfg.POSTGRES_PORT,
            db=self.cfg.POSTGRES_DBN,
        )
        self._pool = None

    # асинхронный контекстный менеджер для получения соединения с БД
    @property
    @asynccontextmanager
    async def pool(self):
        if not self._pool:
            self._pool = await asyncpg.create_pool(
                self.dsn, min_size=1, max_size=2, max_inactive_connection_lifetime=500.0
            )
        yield self._pool


    async def get_all_accounts(self) -> list:
        # запрос в бд
        async with self.pool as p, p.acquire() as cn:
            conn: asyncpg.Connection = cn
            q = """
            SELECT 
                a.uid
                , a.email
                , a.name
                , a.password
            FROM accounts as a
            LIMIT 100;
            """
            accounts = await conn.fetch(q)
            return accounts

    async def get_account_by_id(self, req: UUID4) -> XAccount:
        # запрос в бд
        async with self.pool as p, p.acquire() as cn:
            conn: asyncpg.Connection = cn
            q = """
                SELECT 
                    a.uid
                    , a.email
                    , a.name 
                    , a.password    
                FROM accounts AS a
                WHERE a.uid=($1);
            """
            try:
                account = await conn.fetchrow(q, req)
            except asyncpg.exceptions.DataError:
                raise KeyError("invalid uid")

            if account is None:
                raise ValueError("account not found")

            return XAccount(**account)

    async def create_account(self, req: QCreateAccount) -> XAccountCreated:
        # запрос в бд
        async with self.pool as p, p.acquire() as cn:
            conn: asyncpg.Connection = cn
            q = """
                INSERT INTO accounts (
                    email
                    , name
                    , password
                )
                VALUES ($1, $2, $3)
                RETURNING uid;
            """
            args = [req.email, req.name, req.password]
            try:
                uid = await conn.fetchval(q, *args)
            except asyncpg.exceptions.UniqueViolationError:
                raise KeyError("email busy")
            return XAccountCreated(uid=uid)
    
    async def update_account(self, uid: UUID4, req: QUpdateAccount) -> XOk:
        # запрос в бд
        async with self.pool as p, p.acquire() as cn:
            conn: asyncpg.Connection = cn
            q = """
                UPDATE accounts 
                SET (
                    email
                    , name
                ) = ($2, $3)
                WHERE uid=($1)
                RETURNING uid;
            """
            args = [req.email, req.name]
            try:
                res = await conn.fetchval(q, uid, *args)
            except asyncpg.exceptions.DataError:
                raise KeyError("invalid uid")

            if res is None:
                raise ValueError("account not found")
            else:
                return XOk(message="success")
    
    async def delete_account(self, uid: UUID4) -> XOk:
        # запрос в бд
        async with self.pool as p, p.acquire() as cn:
            conn: asyncpg.Connection = cn
            q = """
                DELETE
                FROM accounts AS a 
                WHERE a.uid=($1);
            """

            try:
                res = await conn.execute(q, uid)
            except asyncpg.exceptions.DataError:
                raise KeyError("invalid uid")

            if res == "DELETE 0":
                return XOk(message="account deleted")
            else:
                return XOk(message="success")