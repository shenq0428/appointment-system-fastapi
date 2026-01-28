from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.appointment import AppointmentModel
from app.schemas.appointment import AppointmentCreate
# 从我们之前写的 schemas 里导入模板
from app.schemas.appointment import AppointmentCreate

router = APIRouter()

# 1. 这是一个“依赖项”，用来获取数据库连接
# 就像是给服务员一把进入后厨账本库的钥匙
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_appointment(item: AppointmentCreate, db:Session = Depends(get_db)):
    #
    new_appointment = AppointmentModel(
        patient_name=item.patient_name,
        service_type=item.service_type,
        appointment_time=item.appointment_time,
        notes=item.notes
    )
    try:
        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        return {"Message":"data have been stored!","data":new_appointment}
    except Exception as e:
        db.rollback()
        print(f"connectionfailed/(ㄒoㄒ)/~~{e}")
        return{"Message":"failed to save?!","error":str(e)}

@router.get("/")
def get_all_appointments(db: Session = Depends(get_db)):
    appointments = db.query(AppointmentModel).all()
    return appointments
