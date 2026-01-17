from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1.address.city)
print(patient1.address.pin)

temp = patient1.model_dump(include={'address'})
print(temp)
print(type(temp))

temp2 = patient1.model_dump(include='address')
temp3 = patient1.model_dump(exclude={'name', 'gender'})
print(temp3)
print(temp2)


patient_dict_2 = {'name': 'nitish', 'age': 35, 'address': address1}

patient2 = Patient(**patient_dict_2)
temp5 = patient2.model_dump(exclude_unset=True)
print(temp5)
# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed