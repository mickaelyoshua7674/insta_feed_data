FROM python:3.12-alpine3.19
LABEL maintainer="mickaelyoshua7674"

# copy files to image
COPY ./requirements.txt /tmp/requirements.txt
COPY ./bot /bot
WORKDIR /bot

ENV PYTHONUNBUFFERED=1
    # the output of python will be printed directly on console

RUN apk update && apk upgrade && \
    # remove apk cache
    rm -rf /var/cache/apk/* && \
    # create virtual environment
    python -m venv /venv && \
    # upgrade pip
    /venv/bin/pip install  --upgrade pip && \
    # install requirements
    /venv/bin/pip install  -r /tmp/requirements.txt && \
    # remove temporary folder
    rm -rf /tmp 

ENV PATH="/venv/bin:$PATH"