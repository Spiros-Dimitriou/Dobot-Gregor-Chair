# Dobot-Gregor-Chair

### Summary

A Python project that creates an ```HTTP API``` with functionality abstraction. These (primitive) microservices control the robotic arm, therefore all uS can be called Cyber-*Physical* Microservices.

### General Structure

##### About the primitive (1st level) microservices:

```HTTP GET``` and ```HTTP POST``` requests call ```python3``` functions, which control the arm. Higher levels of abstraction use the previously mentioned ```HTTP``` endpoints to extend the functionality. The whole point is reusability and easy customization.

##### About higher level microservices:

The higher level microservices are to be implemented using Argo Workflows.

### About

This project is part of my integrated master thesis on [Cyber Physical Microservices](https://sites.google.com/view/cyber-physical-microservice/gregor-chair) under the supervision of prof. Kleanthis Thramboulidis.
This is a project using documentation (communication API) provided by [Dobot](https://www.dobot.cc/) aiming to control a Dobot Magician robotic arm in collaboration with two other robotic arms and perform a series of tasks on two testbenches.
Big thanks to Alex Gustafsson for the communication API implementation as seen [here!](https://github.com/AlexGustafsson/dobot-python)

### Run it!
- Clone this repo on your RPi
- Install Flask and pyserial
- Run the following
```
flask run
```

Finally on your browser, go to http://your-raspberry-pi.ip:5000/demo
