# Dobot-Gregor-Chair

### Summary

A NodeJS / Python project that creates an ```HTTP API``` with functionality abstraction. Then use that ```API``` to create higher abstraction levels and do more complicated tasks. The lowest level (primitive) microservices control the robotic arm, therefore all uS can be called Cyber-*Physical* Microservices.

### General Structure

##### About the primitive (1st level) microservices:

```HTTP GET``` and ```HTTP POST``` requests make subprocesses that run ```python3``` scripts, which control the arm. Higher levels of abstraction use the previously mentioned ```HTTP``` endpoints to extend the functionality. The whole point is reusability and easy customization.

##### About higher level microservices:

*soon™*

### About

This is a project using software (robotic arm API) provided by [Dobot](https://www.dobot.cc/) aiming to control a Dobot Magician robotic arm in collaboration with two other robotic arms and perform a series of tasks on two testbenches. This is also part of my integrated master thesis on [Cyber Physical Microservices](https://sites.google.com/view/cyber-physical-microservice/gregor-chair) under the supervision of prof. Kleanthis Thramboulidis.

### Run it!

Clone this repo on your RPi
```
npm install
node server.js
```
Then on your favourite browser, go to http://your-raspberry-pi.ip:8080/demo
