FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /my_app

COPY requirements.txt dev_requirements.txt ./

RUN pip install --upgrade pip; pip install -r requirements.txt; pip install -r dev_requirements.txt

ADD . /my_app/
