FROM python:2

ARG APP_PATH=/tinbot

#RUN apk --update add python py-pip python-dev build-base linux-headers
#RUN apk --update add  openssl python3 python-dev build-base linux-headers
#RUN update-ca-certificates

RUN wget -O /tmp/models.tar.gz https://storage.googleapis.com/puzzle-models/models.tar.gz
RUN mkdir -p $APP_PATH/tfb
RUN tar -xzvf /tmp/models.tar.gz -C $APP_PATH/tfb
RUN rm /tmp/models.tar.gz

#ENV LOAD_MODELS=false
ENV PYTHONUNBUFFERED 1

#RUN apk --update add python py-pip python-dev build-base linux-headers py-gevent
# py-gevent
COPY requirements.txt $APP_PATH/requirements.txt
#COPY requirements-web.txt $APP_PATH/requirements-web.txt
RUN pip install -r $APP_PATH/requirements.txt
#RUN pip install -r $APP_PATH/requirements-web.txt
#RUN CFLAGS="$CFLAGS -L/lib" pip install uwsgi
RUN pip install uwsgi

COPY . $APP_PATH

WORKDIR $APP_PATH

ENV LOAD_MODELS=true

CMD ["uwsgi", "--http", ":8000", "--module", "tfb:app"]

