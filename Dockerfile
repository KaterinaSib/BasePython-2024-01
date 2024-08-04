FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /meter_app

COPY requirements.txt dev_requirements.txt ./

RUN pip install --upgrade pip; pip install -r requirements.txt; pip install -r dev_requirements.txt

ADD . /meter_app/

RUN python manage.py collectstatic --noinput

CMD ["python manage.py migrate", "python manage.py create_db_meters"]