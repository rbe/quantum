FROM python:3.6.10-slim-buster AS python
RUN apt-get update
RUN apt-get -y install \
        git \
        gcc g++
RUN apt-get -y install \
        libblas3 libblas-dev \
        liblapack3 liblapack-dev
#&& ln -s /usr/include/locale.h /usr/include/xlocale.h
#&& rm -rf /var/cache/apk/*
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools

FROM python AS dwave-demos
# Use volume from docker-compose
#RUN git clone --recursive https://github.com/dwavesystems/demos.git

FROM dwave-demos
#RUN cd /dwave-demos \
#    && git submodule foreach git pull origin master
#RUN cd /dwave-demos/factoring \
#    && pip install -r requirements.txt
ARG DWAVE_TOKEN=
RUN mkdir -p /root/.config/dwave \
    && echo <<EOF\
[defaults]\
client = qpu\
\
[prod]\
token = ${DWAVE_TOKEN}\
EOF >/root/.config/dwave/dwave.conf
WORKDIR /dwave-demos
CMD ["tail", "-f", "/dev/null"]
