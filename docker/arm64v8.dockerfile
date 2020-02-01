FROM area51/gdal:arm64v8-2.2.3
COPY qemu-arm-static /usr/bin

RUN uname -a

RUN apt-get update
RUN apt-get install -y libgdal-dev python3-pip libspatialindex-dev unar bc

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

ADD ./requirements.txt .
RUN pip3 install -r requirements.txt

RUN mkdir /code
ADD . /code/
WORKDIR /code

CMD python3.5 server.py

EXPOSE 8080
