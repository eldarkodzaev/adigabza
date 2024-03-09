###########
# BUILDER #
###########

# pull official base image
FROM python:3.10.12-alpine as builder

# set work directory
WORKDIR /usr/src/adigabza

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/adigabza/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.10.12-alpine

# create directory for the app user
RUN mkdir -p /home/adigabza

# create the app user
RUN addgroup -S adigabza && adduser -S adigabza -G adigabza

# create the appropriate directories
ENV HOME=/home/adigabza
ENV ADIGABZA_HOME=/home/adigabza/site
RUN mkdir $ADIGABZA_HOME
WORKDIR $ADIGABZA_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/adigabza/wheels /wheels
COPY --from=builder /usr/src/adigabza/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $ADIGABZA_HOME

# chown all the files to the app user
RUN chown -R adigabza:adigabza $ADIGABZA_HOME

# change to the app user
USER adigabza
