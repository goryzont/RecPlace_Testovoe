from fastapi import FastAPI
import g4f


from app.users.router import router as router_users

app = FastAPI(
    title="RecPlace"
)


app.include_router(router_users)
