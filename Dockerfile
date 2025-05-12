FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia archivos primero para aprovechar cache de Docker en builds repetidos
COPY requirements.txt .

# Instala dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código al contenedor
COPY . .

# Expone el puerto
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

