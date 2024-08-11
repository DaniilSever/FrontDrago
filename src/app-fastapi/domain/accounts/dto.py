from pydantic import BaseModel, EmailStr, ConfigDict, UUID4

#---------------- Запросы API ----------------

class QCreateAccount(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "example@example.com",
                "password": "password123",
            }
        }
    )

class QAccount(BaseModel):
    uid: UUID4

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "uid": "123e4567-e89b-12d3-a456-426614174000",
            }
        }
    )

class QUpdateAccount(BaseModel):
    email: EmailStr

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "email": "example@example.com",
            }
        }
    )

#---------------- ответы API ----------------

class ZAccount(BaseModel):
    uid: UUID4
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "uid": "123e4567-e89b-12d3-a456-426614174000",
                "email": "example@example.com",
                "password": "password123",
            }
        }
    )

class ZAccountList(BaseModel):
    count: int
    items: list[ZAccount]

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "count": 3,
                "items": [
                    {
                        "uid": "123e4567-e89b-12d3-a456-426614174000",
                        "email": "example@example.com",
                        "password": "password123",
                    },
                    {
                        "uid": "234e5678-e89b-12d3-a456-426614174001",
                        "email": "example2@example.com",
                        "password": "password456",
                    },
                    {
                        "uid": "345e6789-e89b-12d3-a456-426614174002",
                        "email": "example3@example.com",
                        "password": "password789",
                    },
                ]
            }
        }
    )

class ZOk(BaseModel):
    status: str = "ok"

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "status": "ok",
            }
        }
    )

class ZError(BaseModel):
    status: str = "error"

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "status": "error",
            }
        }
    )

#---------------- ответы бд ----------------

class XAccount(BaseModel):
    uid: UUID4
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "uid": "123e4567-e89b-12d3-a456-426614174000",
                "email": "example@example.com",
            }
        }
    )

class XOk(BaseModel):
    status: str = "ok"

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "status": "ok",
            }
        }
    )

class XError(BaseModel):
    status: str = "error"

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "status": "error",
            }
        }
    )