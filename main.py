from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Calculadora")

# Esto permite que tu futuro Frontend (HTML) se conecte a la API sin problemas de seguridad
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a la API de la Calculadora Básica!"}

@app.get("/sumar")
def sumar(num1: float, num2: float):
    return {"resultado": num1 + num2}

@app.get("/restar")
def restar(num1: float, num2: float):
    return {"resultado": num1 - num2}

@app.get("/multiplicar")
def multiplicar(num1: float, num2: float):
    return {"resultado": num1 * num2}

@app.get("/dividir")
def dividir(num1: float, num2: float):
    if num2 == 0:
        return {"error": "No se puede dividir entre cero"}
    return {"resultado": num1 / num2}
