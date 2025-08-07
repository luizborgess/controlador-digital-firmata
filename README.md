![License: GPL v3](https://img.shields.io/github/license/luizborgess/controlador-digital-firmata)
[![Python](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

# Firmata Digital Controller

# Overview

Firmata Digital Controller is an educational control software used in conjunction with an Arduino board.

This software was developed to be used in practical control systems classes, and with it, it is possible to perform open-loop and closed-loop tests using PID.

![](Images/4.gif)

# Docs

Access the documentation through this [link](https://luizborgess.github.io/controlador-digital-firmata/).

# Installation

## Windows

Download the executable file or the zip file from this [link](https://github.com/luizborgess/controlador-digital-firmata/releases)

## MacOS

To proceed with the installation on MacOS, open the terminal and use the following commands:
```
cd <folder_where_you_want_to_install>

curl -JLO https://github.com/luizborgess/controlador-digital-firmata/archive/main.zip

unzip controlador-digital-firmata-main.zip

cd controlador-digital-firmata-main

chmod 755 install_mac.sh

./install_mac.sh
```

To start, use the command:

```
cd <program-folder>
python3 main.py
```

## Linux

To run the software on Linux, it is assumed that Linux is already updated with the latest version of Python3. If so, just use the commands below to download the software and install the dependencies:

```
wget https://github.com/luizborgess/controlador-digital-firmata/archive/main.zip

unzip main.zip

cd controlador-digital-firmata-main

python3 -m pip install -r requirements.txt

sudo apt-get install --reinstall libxcb-xinerama0

python3 main.py
```

To open the software, enter the following commands in the terminal:

```
cd <program-folder>

python3 main.py
```

# Dependencies

Python 3.9+

pyFirmata 1.1.0

numpy 1.20.3

pyqtgraph 0.12.1

PyQt5 5.15+

pyserial 3.5

# License

MIT license
