FROM python:3.6-alpine
LABEL author="Diemesleno Souza Carvalho <diemesleno@gmail.com>"

RUN apk update && apk add --no-cache \
        build-base \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev \
        bash \
    && rm -rf /var/cache/apk/*

ENV INSTALL_PATH /project
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "project.app:create_app()"
