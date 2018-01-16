FROM python:3.6-jessie
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y python3 python3-pip build-essential gettext python-dev zlib1g-dev libtiff5-dev libjpeg62-turbo-dev libfreetype6-dev libwebp-dev graphviz-dev python-setuptools python3-dev automake libtool libreadline6 libreadline6-dev libreadline-dev libsqlite3-dev libxml2 libxml2-dev libssl-dev libbz2-dev libboost-python-dev bzr gcc
RUN apt-get install -y uwsgi uwsgi-plugin-python3
RUN mkdir /app
WORKDIR /app
ADD src/requirements.txt /app/
RUN pip install -r requirements.txt

# py2exif
RUN apt-get install -y libexiv2-dev libboost-python-dev
WORKDIR /tmp/
RUN bzr branch lp:py3exiv2
WORKDIR /tmp/py3exiv2/py3exiv2/
RUN python3 configure.py
RUN ./build.sh
RUN ./build.sh -i
WORKDIR /app

# for russian version
EXPOSE 8001
# for english version
EXPOSE 8002
