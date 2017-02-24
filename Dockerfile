FROM python:2.7
MAINTAINER Zipho Mashologu "zipho@sanbi.ac.za"
 
RUN apt-get update -y --fix-missing \
    && apt-get upgrade -y \
    && apt-get -y install redis-server, rabbitmq-server \
    && mkdir -p /src \
    && pip install -U pip 
 
COPY requirements.txt /src
RUN pip install -r /src/requirements.txt
 
COPY . /src
WORKDIR /src
CMD ["celery" , "-A". "tasks", "worker","--loglevel=info"]                                            