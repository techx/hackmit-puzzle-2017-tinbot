FROM python:2

ARG APP_PATH=/hack-store

#RUN apk --update add python py-pip python-dev build-base linux-headers

COPY requirements.txt $APP_PATH/requirements.txt
RUN pip install -r $APP_PATH/requirements.txt
RUN pip install gevent uwsgi

COPY . $APP_PATH

WORKDIR $APP_PATH

CMD ["uwsgi", "--gevent", "10", "--http", ":8000", "--module", "tfb:app"]

