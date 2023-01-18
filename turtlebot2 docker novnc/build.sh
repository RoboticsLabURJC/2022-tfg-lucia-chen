#!/bin/bash

docker build -f Dockerfile.base -t humble_base .
docker build --no-cache=true -f Dockerfile.turtlebot -t turtlebot2 .
