FROM python:3.12.5

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
