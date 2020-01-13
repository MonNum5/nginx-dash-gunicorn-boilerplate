FROM python:3.6.2

RUN mkdir -p /home/project/dash
WORKDIR /home/project/dash
COPY requirements.txt /home/project/dash
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . /home/project/dash

