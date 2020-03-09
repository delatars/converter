FROM python:3.7-alpine

COPY ./ /app
WORKDIR /app

ENTRYPOINT ["python", "start.py"]