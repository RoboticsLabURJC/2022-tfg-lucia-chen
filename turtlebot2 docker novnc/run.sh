#!/bin/bash

sudo docker run --gpus all --rm -it -p 7681:7681 -p 2303:2303 -p 1905:1905 -p 8765:8765 -p 6080:6080 -p 1108:1108 turtlebot2
