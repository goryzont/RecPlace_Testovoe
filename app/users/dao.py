from app.dao.base import BaseDAO
from app.users.models import Users, Request


class UsersDAO(BaseDAO):
    model = Users


class RequestsDAO(BaseDAO):
    model = Request
