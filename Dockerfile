FROM python:3.9.6-slim

WORKDIR /home/projeto

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN chown 1000:100 -R /home/projeto

USER 1000:100

CMD [ "uvicorn", "--reload", "--host=0.0.0.0", "app:app" ]
