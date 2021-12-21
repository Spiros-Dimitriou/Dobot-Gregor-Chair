Step1: Open the root permission and set the root password.
command : sudo passwd root
Then set your root password,and You must remember your root password!!!

Step2: You should use command to enter the root of raspberry pi.
command : su root
Then enter the password for root.

Step3: Install the library file of serial port in root.
command 1: sudo apt-get install libqt5serialport5
command 2: sudo apt-get install libqt5serialport5-dev.

Step4: Run script file of DobotControl.py
command :  python3 DobotControl.py


