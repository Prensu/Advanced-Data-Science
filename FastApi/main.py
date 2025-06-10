from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in meters')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kg')]

    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @property
    def verdict(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Normal'
        elif bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

def load_data():
    try:
        with open('patients.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)

@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', examples=['P001'])):
    data = load_data()
    if patient_id in data:
        patient = Patient(id=patient_id, **data[patient_id])
        response = patient.model_dump()
        response['id'] = patient.id
        response['bmi'] = patient.bmi
        response['verdict'] = patient.verdict
        return response
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='Sort by height, weight, or bmi'),
    order: str = Query('asc', description='Sort order: asc or desc')
):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field. Choose from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order. Choose between asc and desc')

    data = load_data()
    patients = []

    for pid, pdata in data.items():
        patient = Patient(id=pid, **pdata)
        info = patient.model_dump()
        info['id'] = pid
        info['bmi'] = patient.bmi
        info['verdict'] = patient.verdict
        patients.append(info)

    reverse = order == 'desc'
    sorted_patients = sorted(patients, key=lambda x: x.get(sort_by, 0), reverse=reverse)

    return sorted_patients

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    data[patient.id] = patient.model_dump(exclude={'id'})
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient created successfully'})
