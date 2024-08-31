FROM python:3

RUN mkdir -p /home/project/app
WORKDIR /home/project/app
COPY requirements.txt /home/project/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/app
