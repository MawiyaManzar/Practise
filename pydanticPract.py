from pydantic import BaseModel
from datetime import datetime

class Patient(BaseModel):
    name:str
    age:int
    date: datetime | None

def insert_patient_data(patientObj:Patient):
    
    print(patientObj.name)
    print(patientObj.age)
    print(patientObj.date)
    
    
    
ext_data= {
    'age':123,
    'name':"Umar",
    'date':'2019-06-01 12:22'   
}

patient1= Patient(**ext_data)
insert_patient_data(patient1)

# print(patient1.name)
# print(patient1.model_dump())