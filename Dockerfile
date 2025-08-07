FROM python:3.13.6

WORKDIR /app

COPY app/* /app/

ENTRYPOINT ["python", "app"]
