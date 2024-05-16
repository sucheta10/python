#Addition of two numbers using fastapi
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/add/")
async def add_numbers(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}
