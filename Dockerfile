FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install --upgrade pip setuptools
RUN apt-get update && apt-get install -y build-essential python3-dev libpcre3 libpcre3-dev
COPY requirements.txt /code/
RUN pip install -r requirements.txt


COPY . /code/