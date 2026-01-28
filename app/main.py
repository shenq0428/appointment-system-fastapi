from fastapi import FastAPI

from app.api.endpoints import appointments

app = FastAPI()

# 将 appointments 路由挂载到主程序，并加上前缀
app.include_router(appointments.router, prefix="/appointments",tags=["预约管理"])
@app.get("/health")
def health_check():
    return {"status": "healthy"}