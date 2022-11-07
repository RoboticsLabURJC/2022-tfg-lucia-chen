# Docker con Turtlebot2 simulado

Se necesita que esté en una misma carpeta el Dockerfile y la carpeta turtlebot2.
- El docker tiene como base Ubuntu 22.04 e incluye ros2 humble y Gazebo 11

## Modo de uso
Para crear la imagen
~~~
$ sudo docker build -t turtlebot2 .
~~~

Para crear el contenedor
~~~
$ xhost +
$ sudo docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix turtlebot2
~~~

Tras parar el contenedor acordarse de hacer:
~~~
$ xhost -
~~~

Para entrar en la máquina con un bash:
~~~
$ sudo docker exec -it [ID] /bin/bash
~~~

Para teleoperar el robot:
~~~
$ ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/cmd_vel -p use_sim_time:=true
~~~
