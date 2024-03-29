FROM humble_base

# RAM and src directory
COPY ./scripts/manager/src /src
COPY ./scripts/manager/src/manager/manager.py /

# copy scripts for vnc displays
COPY ./scripts/start_vnc.sh /
COPY ./scripts/kill_all.sh /
COPY ./scripts/entrypoint.sh /
COPY ./scripts/start_vnc_gpu.sh /
COPY ./scripts/check_device.py /

# give execution permissions
RUN chmod +x /start_vnc.sh /kill_all.sh /entrypoint.sh /manager.py /start_vnc_gpu.sh

# environment
COPY ./.env /.env

# RoboticsAcademy
COPY ./RoboticsAcademy /RoboticsAcademy
# Custom Robot Repository
RUN mkdir -p /opt/jderobots 
COPY ./CustomRobots /opt/jderobots/CustomRobots

# create workspace and add Robot packages
RUN mkdir -p /home/ws/src
RUN cp -r /opt/jderobots/CustomRobots /home/ws/src/

# Compile workspace
WORKDIR /home/ws
RUN sudo rosdep fix-permissions && rosdep update
RUN rosdep install --from-paths src --ignore-src -r --rosdistro humble -y
RUN colcon build --symlink-install

# Django server
EXPOSE 8000
# Manager websocket
EXPOSE 7163

# Exercise websocket
EXPOSE 1905
# GUI websockets
EXPOSE 2303

# noVNC Console
EXPOSE 1108
# noVNC Gazebo
EXPOSE 6080
# noVNC Rviz
EXPOSE 6081
# noVNC GUI
EXPOSE 6082

# WebRtc
EXPOSE 1831

WORKDIR /
CMD ["./entrypoint.sh"]