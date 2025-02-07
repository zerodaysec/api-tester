FROM python:3.13.2

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
