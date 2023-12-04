FROM python:3.9

WORKDIR /app/backend
RUN import os
RUN print(os.getcwd())
RUN pip3 install -r requirements.txt

COPY . /app/backend

EXPOSE 8000

CMD python /app/backend/manage.py runserver 0.0.0.0:8000
