from fastapi import APIRouter, HTTPException, Response, status

from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO, RequestsDAO
from app.users.schemas import SUserAuth

from app.chek_gpt import ask_gpt, run_provider
from app.chatgpt import ask_gpt as chatopenai


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Регистрация & Requests"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token


@router.get('/get_user')
async def get_user(id: int):
    user = await UsersDAO.find_one_or_none(id=id)
    if not user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    return user


@router.post("/request")
async def post_request(request: str, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    result = chatopenai(request)
    await RequestsDAO.add(body_request=request, id_owner_request=user.id, answer_request=result)
    return result


@router.get("/last_three")
async def get_last_three(id: int):
    result = await RequestsDAO.last_3_request(id_owner_request=id)
    return result

