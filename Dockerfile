FROM python:3.13.3

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
