# Docker con Turtlebot2 simulado

Se necesita que esté en una misma carpeta los Dockerfile y la carpeta turtlebot2, brain_turtle, robotics_academy
- El docker tiene como base Ubuntu 22.04 e incluye ros2 humble y Gazebo 11

## Modo de uso
Para crear la imagen (base nvidia con ubuntu 22.04)
~~~
./build.sh
~~~

Para crear el contenedor 
* No todos los puertos se están usando. En el caso que se utilice [esta plantilla html](https://github.com/RoboticsLabURJC/2022-tfg-lucia-chen/tree/main/frontend), los puertos utilizados son: 6080 para gzclient, 1108 para terminal, 2303 para rviz2 y 1905 para la ventana GUI.
~~~
./run.sh
~~~
o 
~~~
sudo docker run --gpus all --rm -it -p 7681:7681 -p 2303:2303 -p 1905:1905 -p 8765:8765 -p 6080:6080 -p 1108:1108 turtlebot2
~~~

Para entrar en la máquina con bash:
~~~
sudo docker exec -it [ID] /bin/bash
~~~

### Dentro del contenedor 

Para lanzar xserver, vnc y novnc
~~~
./xserver.sh [display]
~~~
~~~
./vnc_novnc.sh [display] [in_port] [out_port]
~~~
* Ejemplo (importante el orden)
~~~
./xserver.sh :0
./vnc_novnc.sh :0 5900 6080
~~~

Para lanzar el robot en un mundo vacío, abrir gzclient y rviz2
~~~
./empty_world_robot
~~~

Para teleoperar el robot:
~~~
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/cmd_vel -p use_sim_time:=true
~~~
