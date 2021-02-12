FROM python:latest

WORKDIR /app
ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
