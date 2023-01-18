#!/bin/bash

#sudo docker run --gpus all --rm -it --env="DISPLAY=:0" -p 5900:5900 -p 6080:6080 turtlebot2
sudo docker run --gpus all --rm -it -p 6080:6080 turtlebot2