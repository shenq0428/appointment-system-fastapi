from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 这是我们的“预约单”模板，只展示需要给用户看的部分,像这里的appointmentcreate model没有展示出id
class AppointmentCreate(BaseModel):
    patient_name: str        # 患者姓名
    service_type: str        # 服务类型（比如：牙科、内科）
    appointment_time: datetime # 预约时间
    notes: Optional[str] = None # 备注（可选）