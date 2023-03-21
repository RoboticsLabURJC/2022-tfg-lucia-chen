#!/bin/bash

sudo docker build -f Dockerfile.base -t humble_base .
sudo docker build -f Dockerfile.ram  -t new_ram .