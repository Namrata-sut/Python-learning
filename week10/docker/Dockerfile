#Dockerfile: Blueprint for building image
#image: template for running container
#container: running process with our application

FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
