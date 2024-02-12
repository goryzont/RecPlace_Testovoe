from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserRequests(SUserAuth):
    last_request: int
    quantity_requests: int


class SRequest(BaseModel):
    body_request: str
    answer_request: str
    owner_request: str
