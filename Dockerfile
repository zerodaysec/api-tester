FROM python:3.12.6

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
