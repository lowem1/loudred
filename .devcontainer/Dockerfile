FROM mcr.microsoft.com/devcontainers/python:0-3.10-bullseye

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
