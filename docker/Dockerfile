FROM raspbian/stretch:latest

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update

RUN apt-get upgrade -y

RUN apt-get install -y gdal-bin python3-pip libgdal-dev

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal

ENV C_INCLUDE_PATH=/usr/include/gdal

ADD ./requirements.txt .

RUN pip3 install -r requirements.txt

RUN apt-get install -y libspatialindex-dev unar bc

RUN mkdir /code

ADD . /code/

WORKDIR /code

CMD python server.py

EXPOSE 8080
