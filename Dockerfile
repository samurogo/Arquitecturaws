# Usa una imagen base de Python
FROM python:3.9-slim-buster

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu aplicación
COPY . .

# Expone el puerto que usa Flask
EXPOSE 5000

# Define la variable de entorno para Flask
ENV FLASK_APP=app.py

# Comando para iniciar la aplicación
CMD ["python", "app.py"]