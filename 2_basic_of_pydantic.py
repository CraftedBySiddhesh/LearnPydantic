from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

patient_info1 = {"name": "Siddhesh", "age": 30}
# patient_info2 = {"name": "Siddhesh", "age": "Thirty"}
patient_info3 = {"name": "Siddhesh", "age": '30'}

patient1 = Patient(**patient_info1)
# patient2 = Patient(**patient_info2)
patient3 = Patient(**patient_info3)

def insert_patient_data_5(Patient: Patient):
    print(Patient.name)
    print(Patient.age)
    print('Inserted in data base')

insert_patient_data_5(patient1)
# insert_patient_data_5(patient2)
insert_patient_data_5(patient3)