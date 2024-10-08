FROM python:3.13.0

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
