FROM python:3.11
WORKDIR /pdm_hello_world

RUN mkdir pdm_hello_world
COPY . /pdm_hello_world

RUN pip install --upgrade pip
RUN pip install pdm
RUN pdm install
RUN pdm build