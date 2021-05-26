FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get -y install libpq-dev gcc

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]