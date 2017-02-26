FROM ubuntu:16.04

RUN apt update && \
    apt upgrade -y && \
    apt install -y python3 python3-pip time

RUN pip3 install bottle

ENV LANG C.UTF-8
RUN apt install -y software-properties-common && \
    add-apt-repository ppa:ondrej/php && \
    apt update
RUN apt install -y php5.6 php5.6-curl php5.6-dev

WORKDIR /src
