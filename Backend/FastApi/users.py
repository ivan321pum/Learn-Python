from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def get_users():
    return "Hola FastAPI"
