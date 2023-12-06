from fastapi import FastAPI

app = FastAPI()

"""para ejecutar el servidor local en uvicorn hay que poner en terminal: uvicorn main(nombre del fichero):app(nombre 
de la variable a la que hemos asignado fastapi) --reload(para que se recargue automaticamente"""


@app.get("/")  # / es para ponerlo en la raíz, pero podrias ponerlo en cualquier otra página
async def root():  # Se pone asíncrono para no parar todo el programa en lo que tarda en hacer la petición del backend
    return "¡Hola mundo!"


@app.get("/home")
async def home():
    return "¡Bienvenido a casa!"


# Fastapi genera documentación automáticamente, para verla hay que poner en el navegador: direccion/docs o
# direccion/redoc
