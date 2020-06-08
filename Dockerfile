FROM python:3.8

WORKDIR /app/Gamein/

COPY requirements.txt /app/Gamein
ENV PIP_NO_CACHE_DIR 1
RUN pip install -r requirements.txt

COPY . .
