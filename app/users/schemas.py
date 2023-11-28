from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserRequests(SUserAuth):
    last_request: int
    quantity_requests: int
    requests: list[str]


class SRequest(BaseModel):
    body_request: str
    owner_request: str
