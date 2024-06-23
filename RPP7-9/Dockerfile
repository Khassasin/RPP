FROM python:3

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /App

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "WebProject/manage.py", "runserver", "0.0.0.0:8000"]