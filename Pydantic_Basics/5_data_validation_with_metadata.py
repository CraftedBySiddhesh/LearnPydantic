from pydantic import AnyUrl, BaseModel, EmailStr, Field
from typing import Annotated, List, Dict, Optional


class Patient(BaseModel):
    name: Annotated[
        str, Field(min_length=1, 
              max_length=100, 
              description="Full name of the patient", 
              title="Patient Name", 
              examples=["John Doe", "Jane Smith"])]
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    linkedin_profile: AnyUrl
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(description="Marital status of the patient",
                                   title="Married Status",
                                   default=False)]
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
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
    "email": "siddhesh@example.com",
    "linkedin_profile": "https://www.linkedin.com/in/siddhesh",
    "weight": 70.5,
    "married": False,
    "allergies": ["pollen", "nuts"],
    "contacts": {"home": "1234567890", "work": "0987654321"}
}

patient_info2 = {
    "name": "Nikita",
    "age": "30",
    "email": "nikita@example.com",
    "linkedin_profile": "https://www.linkedin.com/in/nikita",
    "weight": 70.5,
    "contacts": {"home": "1234567890", "work": "0987654321"}
}

insert_patient_data_6(Patient(**patient_info1))
update_patient_data_6(Patient(**patient_info1))

insert_patient_data_6(Patient(**patient_info2))
update_patient_data_6(Patient(**patient_info2))
