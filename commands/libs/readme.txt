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
command :  python3 demoCommand.py

This [line](https://github.com/Spiros-Dimitriou/Dobot-Gregor-Chair/blob/d735c89336a4fd60277219558d43411092ad6310/commands/libs/DobotDllType.py#L466) may have to be changed
