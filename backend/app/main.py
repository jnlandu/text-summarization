
#  Personal imports
from app.app import app
from routers import auth, chat,routines,workouts


@app.get("/")
async def root():
    return {"message": "Healthy"}

app.include_router(auth.router)
app.include_router(chat.router)


print("Server is running correctly")


