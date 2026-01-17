from pydantic import BaseModel
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contacts: Dict[str, str]


def insert_patient_data_6(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts)
    print('Inserted in data base')

def update_patient_data_6(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts)
    print('Updated in data base')

patient_info1 = {
    "name": "Siddhesh",
    "age": "30",
    "weight": 70.5,
    "married": False,
    "allergies": ["pollen", "nuts"],
    "contacts": {"home": "1234567890", "work": "0987654321"}
}

patient_info2 = {
    "name": "Nikita",
    "age": "30",
    "weight": 70.5,
    "contacts": {"home": "1234567890", "work": "0987654321"}
}

insert_patient_data_6(Patient(**patient_info1))
update_patient_data_6(Patient(**patient_info1))

insert_patient_data_6(Patient(**patient_info2))
update_patient_data_6(Patient(**patient_info2))
