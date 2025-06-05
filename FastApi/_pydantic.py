from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]  

# Function to insert patient data (prints some details)
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {
        "name": "Virat Kolhi",
        "age": 30,
        "weight": 70.5,
        "married": True,
        "allergies": ["pollen", "peanuts"],
        "contact_details": {"phone": "123-456-7890", "email": "kingkolhi@gmail.com"}
    }
    
# Instantiate a Patient object
patient = Patient(**patient_info)
    
# Call the function to insert patient data
insert_patient_data(patient)


patient_data= {
        "name": "Jitesh Sharma",
        "age": 30,
        "weight": 60.7,
        "married": False,
        "allergies": ["pollen", "peanuts"],
        "contact_details": {"phone": "123-456-7890", "email": "kingkolhi@gmail.com"}
    }

# Instantiate a Patient object
patient1 = Patient(**patient_data)
    
# Call the function to insert patient data
update_patient_data(patient1)