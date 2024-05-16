# Calculator using fastapi
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    n1: float
    n2: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple Calculator API!"}

@app.post("/calculate/")
async def calculate_numbers(numbers: Numbers, operator: str):
    result = None
    if operator == '+':
        result = numbers.n1 + numbers.n2
    elif operator == '-':
        result = numbers.n1 - numbers.n2
    elif operator == '*':
        result = numbers.n1 * numbers.n2
    elif operator == '/':
        if numbers.n2 == 0:
            return {"error": "Division by zero is not allowed"}
        result = numbers.n1 / numbers.n2
    else:
        return {"error": "Invalid operator"}

    return {"result": result}
