FROM python:3.13.1

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
