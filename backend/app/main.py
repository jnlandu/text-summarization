
from fastapi.staticfiles import StaticFiles

#  Personal imports
from app.app import app
from routers import auth, chat, hello




@app.get("/")
async def root():
    return {"message": "Healthy"}

@app.get('/admin')
async def admin():
    return {"message": "Admin page"}


app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(hello.router)




print("Server is running correctly")


