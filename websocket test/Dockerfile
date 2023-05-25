FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# Make all NVIDIA GPUS visible
ARG NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES all

# Setup NON INTERACTIVE ENVIRONMENT
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3-pip \
  && rm -rf /var/lib/apt/lists/*

# websocket server dependency
RUN pip3 install websocket_server posix-ipc django djangorestframework==3.13.1 django-webpack-loader==1.5.0
RUN python3.10 -m pip install websockets asyncio

# pip install dependencies
RUN python3.10 -m pip install pylint transitions pydantic websocket-client opencv-python

COPY ./broker.py /
RUN chmod +x broker.py

# WebRtc
EXPOSE 8765

WORKDIR /
#CMD ["python3 ./broker.py"]