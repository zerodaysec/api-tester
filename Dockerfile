FROM python:3.12.4

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
