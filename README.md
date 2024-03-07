<h1>Microservicio contruido con Python & FastApi</h1>

![image](https://github.com/alxxr/Microservicio/assets/79178497/a1e44d8b-fcec-4b89-b42b-7208c4d2d0f9)


![image](https://github.com/alxxr/Microservicio/assets/79178497/aa030559-9683-40e8-8f24-ba4b57c7220a)


<h1>Instrucciones de ejecución</h1>
Para poder ejecutar el proyecto correctamente, sigue los siguientes pasos:

<h2>1. Configurar la variable de entorno PYTHONPATH</h3>
Es necesario agregar los directorios /app y /src a la variable PYTHONPATH para que Python pueda encontrar los módulos y paquetes correctamente.

<h3>En PowerShell (Windows):</h3>

Comando en PowerShell: $env:PYTHONPATH = "$env:PYTHONPATH;C:\Users\Alex Rosas\Dev Personales\Python\Microservicio\app\src"

<h3>En CMD (Windows):</h3>

Comando en CMD: set PYTHONPATH=%PYTHONPATH%;C:\"Users\Alex Rosas\Dev Personales\Python\Microservicio\app\src"


<h2>2. Ejecutar el servicio</h2>
El archivo main.py debe estar en el directorio interfaces.

<h3>Comando para ejecutar el servicio con Uvicorn:</h3>

uvicorn main:app

Este comando inicia el servidor utilizando Uvicorn y carga la aplicación FastAPI definida en main.py. Asegúrate de ejecutar este comando desde el directorio interfaces del proyecto.



