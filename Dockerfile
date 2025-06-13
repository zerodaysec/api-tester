FROM python:3.13.5

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
