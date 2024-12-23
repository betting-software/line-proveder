FROM python:3.10
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . . 