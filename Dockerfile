# Dockerfile

# pull the official docker image
FROM python:3.12.1-slim AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock README.md /project/
COPY src/ /project/src


WORKDIR /project

RUN pdm install

EXPOSE 8080
CMD ["pdm", "run", "start"]