from pydantic import BaseModel, EmailStr, ConfigDict, UUID4

#---------------- Запросы API ----------------

class QCreateAccount(BaseModel):
    email: EmailStr
    name: str
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "example@example.com",
                "name": "username",
                "password": "password123",
            }
        }
    )

class QUpdateAccount(BaseModel):
    email: EmailStr
    name: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "email": "example@example.com",
                "name": "username",
            }
        }
    )

#---------------- ответы API ----------------

class ZAccount(BaseModel):
    uid: UUID4
    email: EmailStr
    name: str
    password: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "uid": "123e4567-e89b-12d3-a456-426614174000",
                "email": "example@example.com",
                "name": "username",
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
                        "name": "username",
                        "password": "password123",
                    },
                    {
                        "uid": "234e5678-e89b-12d3-a456-426614174001",
                        "email": "example2@example.com",
                        "name": "username",
                        "password": "password456",
                    },
                    {
                        "uid": "345e6789-e89b-12d3-a456-426614174002",
                        "email": "example3@example.com",
                        "name": "username",
                        "password": "password789",
                    },
                ]
            }
        }
    )

class ZOk(BaseModel):
    status: str = "ok"
    message: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "status": "ok",
            }
        }
    )

class ZError(BaseModel):
    status: str = "error"
    message: str
    status_code: int

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "status": "error",
                "message": "Error message",
            }
        }
    )

#---------------- ответы бд ----------------

class XAccountCreated(BaseModel):
    uid: UUID4

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "uid": "123e4567-e89b-12d3-a456-426614174000",
            }
        }
    )

class XAccount(BaseModel):
    uid: UUID4
    email: EmailStr
    name: str
    password: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "uid": "123e4567-e89b-12d3-a456-426614174000",
                "email": "example@example.com",
                "name": "username",
                "password": "password123",
            }
        }
    )

class XOk(BaseModel):
    status: str = "ok"
    message: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "status": "ok",
            }
        }
    )