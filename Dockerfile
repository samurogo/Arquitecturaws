# Usamos una imagen base de Python ligera
FROM python:3.9-slim-buster

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos e instalamos las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de la aplicación
COPY . .

# Exponemos el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación usando Gunicorn (servidor de producción)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]