from pydantic import BaseModel, EmailStr, computed_field, model_validator
from typing import List, Dict, Any

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='before')
    @classmethod
    def normalize_input(cls, data: Any):
        # BEFORE validator runs on RAW input data (dict)
        # Used for normalization / preprocessing

        # Example: strip spaces from name if present
        if 'name' in data and isinstance(data['name'], str):
            data['name'] = data['name'].strip()

        # Example: ensure contact_details exists as dict
        if 'contact_details' in data and data['contact_details'] is None:
            data['contact_details'] = {}

        return data

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        # AFTER validator runs on fully constructed model (self)

        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')

        return self
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')
