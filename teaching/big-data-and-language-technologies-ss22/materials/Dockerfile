FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
	python3.8 \
    python3.8-distutils \
    curl

# set python3.8 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# install pip
RUN curl -Ss https://bootstrap.pypa.io/get-pip.py | python3

# upgrade pip to newest version
RUN python3 -m pip install --upgrade pip && python3 -m pip install setuptools --no-cache-dir

# copy requirements
COPY requirements.txt .

# install requirements
RUN python3 -m pip install -r requirements.txt --no-cache-dir
