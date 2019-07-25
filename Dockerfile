FROM python:3.7-alpine

#set env variables
# 1. remove .pyc files from container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set a directory in Docker
WORKDIR /.code

# install psycopg2
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip3 install --upgrade pip\
    &&pip3 install psycopg2



# copy the requirements file
COPY ./requirements.txt /.code/requirements.txt


#install dependencies
RUN pip3 install -r requirements.txt

# install dependencies
RUN pip install --upgrade pip
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && apk del .build-deps


#copy files
COPY . /code
