from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
@app.get("/{number1}/{operator}/{number2}/")
def calculator(number1: int, operator: str, number2: int):
    if operator == '+':
        return {number1 + number2}
    elif operator == '-':
        return {number1 - number2}
    elif operator == '*':
        return {number1 * number2}
    elif operator == '^':
        return {number1 ** number2}
    elif operator == ":":
        if number2 != 0:
            return {number1 / number2}
        else:
            reurn {""}
    else:
        return {"error"}
#работа Вейнмайера Андрея