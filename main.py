from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter(prefix="/api")

@router.get("/")
async def index():
    return {"message": "Hello World"}

@router.get("/items/{item_id}")
async def get_item(item_id: float):
    return {"item_id": item_id}

@router.get('/users/me')
async def read_user():
    return {"user_id": "the current user"}

@router.get('/users/{name}')
async def read_user_me(name):
    return {"user_id": f"the current user {name}"}


app.include_router(router)