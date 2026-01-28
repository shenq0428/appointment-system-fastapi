from sqlalchemy import Column, Integer, String, DateTime
#sqlachemy是数据库里的表结构
from app.database.session import Base

class AppointmentModel(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    service_type = Column(String)
    appointment_time = Column(DateTime)
    notes = Column(String, nullable=True)
