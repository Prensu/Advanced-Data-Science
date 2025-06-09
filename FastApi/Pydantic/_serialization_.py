from pydantic import BaseModel

# Define Address model
class Address(BaseModel):
    city: str
    state: str
    pin: str

# Define Patient model with default gender
class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address

# Create an address dictionary
address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

# Create an Address object
address1 = Address(**address_dict)

# Create a patient dictionary with a nested address dictionary
patient_dict = {
    'name': 'Sachhyam',
    'age': 23,
    'address': {
        'city': 'Sorakhutte',
        'state': 'Bagmati',
        'pin': '44600'
    }
}

# Create a Patient object
patient1 = Patient(**patient_dict)

# Dump the model as a dict
temp = patient1.model_dump(exclude_unset=True)

# Print results
print(temp)
print(type(temp))
