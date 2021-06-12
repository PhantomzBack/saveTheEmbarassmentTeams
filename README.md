# saveTheEmbarassmentTeams

A tool to prevent you from embarassing yourself in a teams meeting.

## What it does

Well, it checks if you are unmuted every second, and if you are, it creates an overlay window, alerting you that you are unmuted on teams. Currently, it only supports the browser version of teams.

## Set it Up

You don't need to much to get it up and running.
- Ensure you have python 3.x installed and added to the PATH.
- Use pip to get the following libraries: 
  * `PyQt5`
  * `Selenium`

- Lastly, according to the browser you use, fetch the driver for it, following this:https://selenium-python.readthedocs.io/installation.html#drivers. Also ensure that you've installed the driver for your corresponding version.
- After installing the driver, place it in a folder and add that folder to your PATH variable.

That's all! Run the python script, and prevent yourself from farting into your mic or something😉.
