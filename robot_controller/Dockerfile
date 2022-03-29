FROM python:alpine

WORKDIR /app

COPY robot_controller/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ../lib lib/

COPY robot_controller/app.py robot_controller/composites.py robot_controller/primitives.py ./

CMD [ "python3", "app.py"]
