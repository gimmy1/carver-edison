# base image
FROM python:3.6.5-alpine


# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# set working directory
WORKDIR /twt/src/app

# add and install requirements
COPY ./requirements.txt /twt/src/app/requirements.txt
RUN pip install -r requirements.txt

# new
# add entrypoint.sh
COPY ./entrypoint.sh /twt/src/app/entrypoint.sh
RUN chmod +x /twt/src/app/entrypoint.sh

# add app
COPY . /twt/src/app

# run server
CMD ["/twt/src/app/entrypoint.sh"]