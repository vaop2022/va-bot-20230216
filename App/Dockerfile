FROM python:latest

WORKDIR /usr/bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .