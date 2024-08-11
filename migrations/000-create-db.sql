CREATE
DATABASE tracker WITH OWNER postgres ENCODING 'UTF8';


\connect tracker postgres;


CREATE
EXTENSION IF NOT EXISTS "uuid-ossp";

DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts
(
    uid          uuid PRIMARY KEY   DEFAULT uuid_generate_v4(),
    email        VARCHAR(255) NULL UNIQUE,
    name         VARCHAR(255) NULL,
    password     VARCHAR(255) NULL,
    created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at   TIMESTAMP NULL,
    deleted_at   TIMESTAMP NULL,
    blocked_till TIMESTAMP NULL
);
--
CREATE INDEX ON accounts (created_at);
CREATE INDEX ON accounts (blocked_till);
CREATE INDEX ON accounts (deleted_at);
--
COMMENT ON TABLE accounts is 'Аккаунты (Подтвержденные)';
COMMENT ON COLUMN accounts.uid is 'uuid';
COMMENT ON COLUMN accounts.email is 'Подтвержденный емейл';
COMMENT ON COLUMN accounts.created_at is 'Создание по UTC';
COMMENT ON COLUMN accounts.updated_at is 'Обновление по UTC';
COMMENT ON COLUMN accounts.deleted_at is 'Удален по UTC';
COMMENT ON COLUMN accounts.blocked_till is 'Снятие блокировки по UTC';
