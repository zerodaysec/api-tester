FROM python:3.13.4

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
