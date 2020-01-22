FROM alpine AS builder
RUN apk update
RUN apk add curl
WORKDIR /qemu
RUN curl -L https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-arm.tar.gz | tar zxvf - -C . && mv qemu-3.0.0+resin-arm/qemu-arm-static .

FROM area51/gdal:arm64v8-2.2.3
COPY --from=builder /qemu/qemu-arm-static /usr/bin

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
