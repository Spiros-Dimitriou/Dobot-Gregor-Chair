# Dobot-Gregor-Chair

## Summary

A Python project that creates an `HTTP API` with functionality abstraction. These microservices control the robotic arm, therefore can be called Cyber-*Physical* Microservices.

## General Structure

### About the primitive (1st level) microservices:

`HTTP GET` and `HTTP POST` requests call `python3` functions, which control the arm. Higher levels of abstraction use the previously mentioned `HTTP` endpoints to extend the functionality. The whole point is reusability and easy customization.

### About composite (higher level) microservices:

The higher level microservices are implemented using the functions of the primitive microservices.

Future self talking here, when a composite service uses a primitive I should've hit it with http, would've been more cloud-y that way.

## About

This project is part of my integrated master thesis on [Cyber Physical Microservices](https://sites.google.com/view/cyber-physical-microservice/gregor-chair) under the supervision of prof. Kleanthis Thramboulidis.
This is a project using documentation (communication API) provided by [Dobot](https://www.dobot-robots.com) aiming to control three Dobot Magician robotic arms in collaboration and perform a series of tasks on two testbenches.
Big thanks to Alex Gustafsson for the communication API implementation as seen [here!](https://github.com/AlexGustafsson/dobot-python)

## Run it!
- Clone this repo on your RPi
- Install Flask and pyserial
- Execute `flask run`

Finally on your browser, go to http://your-raspberry-pi.ip:5000/demo
