FROM python:3.8.13-slim-buster

RUN mkdir /opt/fast
WORKDIR  /opt/fast
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","app.py"]