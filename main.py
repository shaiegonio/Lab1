from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
def factorial(starting_number: int):
    if starting_number == 0:
        return {"result": False}
    
    result = 1
    num = starting_number
    
    while num > 1:
        result *= num
        num -= 1

    return {"result": result}
