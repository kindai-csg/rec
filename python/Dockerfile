FROM python:3.6-alpine

ADD requirements.txt ./

RUN apk add gcc musl-dev && \
    pip install -r requirements.txt && \
    rm -f requirements.txt