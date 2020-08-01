FROM area51/gdal:2.2.3

RUN apt-get update
RUN apt-get install -y libgdal-dev python3-pip libspatialindex-dev unar bc wget

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

ADD ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

WORKDIR /code/
ADD src/* ./

CMD python3.5 server.py

EXPOSE 8080
