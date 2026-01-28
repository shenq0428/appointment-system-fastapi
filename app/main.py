from fastapi import FastAPI

from app.api.endpoints import appointments

from app.database.session import engine,Base

from app.models import appointment

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 将 appointments 路由挂载到主程序，并加上前缀
app.include_router(appointments.router, prefix="/appointments",tags=["预约管理"])
@app.get("/health")
def health_check():
    return {"status": "healthy"}