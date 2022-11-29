FROM humble_base

# Turtlebot2 simulated
WORKDIR /home
RUN mkdir -p turtlebot2_ws/src
COPY ./turtlebot2 /home/turtlebot2_ws/src
WORKDIR /home/turtlebot2_ws
RUN sudo rosdep fix-permissions 
RUN rosdep update && rosdep install --from-paths src --ignore-src -r -y
RUN colcon build --symlink-install
COPY empty_world_robot /home/turtlebot2_ws
