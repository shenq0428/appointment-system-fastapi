from fastapi import APIRouter
# 从我们之前写的 schemas 里导入模板
from app.schemas.appointment import AppointmentCreate

router = APIRouter()

# 模拟一个临时数据库（程序重启后数据会清空，后续我们会学如何连真数据库）
fake_appointment_db = []

@router.post("/")
def create_appointment(item: AppointmentCreate):
    fake_appointment_db.append(item)
    return {"message": "make appointment successfully","data": item}

@router.get("/")
def get_all_appointment():
    return fake_appointment_db
