FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN apk add build-base
RUN apk add alpine-sdk
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN chmod +x /app/entrypoint.sh
ENV HOME=/var/cache/
ENV APP_HOME=/var/cache/djanredis
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
ENTRYPOINT ["sh", "/app/entrypoint.sh" ]