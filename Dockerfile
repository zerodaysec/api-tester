FROM python:3.12.7

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
