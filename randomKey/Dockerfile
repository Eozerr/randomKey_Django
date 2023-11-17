FROM python:3.11.4-alpine

WORKDIR /application

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /application/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /application/entrypoint.sh

COPY . /application

ENTRYPOINT [ "/application/entrypoint.sh" ]