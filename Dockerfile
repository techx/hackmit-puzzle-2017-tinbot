#FROM python:2
FROM alpine:3.6

ARG APP_PATH=/tinbot

#RUN apk --update add python py-pip python-dev build-base linux-headers

#RUN curl -o /tmp/models.tar.gz https://storage.googleapis.com/tinbot-models/models.tar.gz
#RUN mkdir -p $APP_PATH/tfb
#RUN tar -xzvf /tmp/models.tar.gz -C $APP_PATH/tfb
#RUN rm /tmp/models.tar.gz

ENV LOAD_MODELS=false
ENV PYTHONUNBUFFERED 1

RUN apk --update add python py-pip python-dev build-base linux-headers py-gevent
#COPY requirements.txt $APP_PATH/requirements.txt
COPY requirements-web.txt $APP_PATH/requirements-web.txt
#RUN pip install -r $APP_PATH/requirements.txt
RUN pip install -r $APP_PATH/requirements-web.txt
RUN CFLAGS="$CFLAGS -L/lib" pip install uwsgi

COPY . $APP_PATH

WORKDIR $APP_PATH

CMD ["uwsgi", "--gevent", "10", "--http", ":8000", "--module", "tfb:app"]

