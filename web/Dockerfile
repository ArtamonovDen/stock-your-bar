FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1 

COPY ./requirements.txt requirements.txt
COPY ./app /app
COPY ./entrypoint.sh /entrypoint.sh

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev netcat \
  --no-install-recommends \
  && adduser --disabled-password --gecos '' user


RUN pip install -r requirements.txt

WORKDIR /app

USER user

ENTRYPOINT ["sh", "/entrypoint.sh"]