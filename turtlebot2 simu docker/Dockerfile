FROM ubuntu:22.04 

ENV DEBIAN_FRONTEND=noninteractive

# Install ROS2 and RVIZ2
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    sudo \
  && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null \
  && apt-get update && apt-get install -y \
    ros-humble-ros-base \
    python3-argcomplete \
    ros-humble-desktop \
    ros-humble-joint-state-publisher \
    ros-humble-rviz2 \
  && rm -rf /var/lib/apt/lists/*

ENV ROS_DISTRO=humble
ENV AMENT_PREFIX_PATH=/opt/ros/humble
ENV COLCON_PREFIX_PATH=/opt/ros/humble
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/gazebo-11/plugins:/opt/ros/humble/opt/rviz_ogre_vendor/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/opt/ros/humble/lib:/usr/share/gazebo/../../lib/x86_64-linux-gnu/gazebo-11/plugins:
ENV PATH=/opt/ros/humble/bin:$PATH
ENV PYTHONPATH=/opt/ros/humble/lib/python3.10/site-packages
ENV ROS_PYTHON_VERSION=3
ENV ROS_VERSION=2

RUN apt-get update && apt-get install -y \
  bash-completion \
  build-essential \
  cmake \
  git \
  pylint \
  python3-colcon-common-extensions \
  python3-pip \
  python3-rosdep \
  python3-vcstool \
  vim \
  wget \
  && rm -rf /var/lib/apt/lists/* \
  && rosdep init

# Install gazebo
RUN apt-get update && apt-get install -q -y \
  gnupg \
  && wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null \
  && rosdep update \
  && apt-get update && apt-get install -q -y \
    ros-humble-gazebo* \
  && rm -rf /var/lib/apt/lists/*


# Include and build our Robot
RUN echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc

WORKDIR /home
RUN mkdir -p turtlebot2_ws/src
COPY ./turtlebot2 /home/turtlebot2_ws/src
WORKDIR /home/turtlebot2_ws
RUN sudo rosdep fix-permissions 
RUN rosdep update && rosdep install --from-paths src --ignore-src -r -y
RUN colcon build --symlink-install
