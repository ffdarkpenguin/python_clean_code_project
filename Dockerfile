FROM python:3.9.6-slim

VOLUME [ "/app" ]

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN chown 1000:100 -R /app

USER 1000:100

CMD [ "uvicorn", "--reload", "--host=0.0.0.0", "projeto.app:app" ]
