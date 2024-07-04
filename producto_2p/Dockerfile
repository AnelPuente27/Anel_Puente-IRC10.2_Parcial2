# Utiliza una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala los paquetes necesarios del sistema
RUN apt-get update && apt-get install -y \
    curl \
    sshpass \
    && rm -rf /var/lib/apt/lists/*

# Instala Ansible
RUN pip install ansible

# Copia los archivos de requerimientos y el código de la aplicación
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto en el que correrá la aplicación Flask
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]
