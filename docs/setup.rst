===================
GPIO Workshop Setup
===================

How to setup the Dragonboard 410c for this workshop

Install Linux
-------------
The latest Linux build based on Debian 8.0 (aka jessie) is available from

http://www.96boards.org/products/ce/dragonboard410c/downloads/

There is also a great getting started guide over there also.

Change the keyboard layout
--------------------------
The above release has a US based keyboard configuration. If you need something different then use:

.. code-block:: none

    sudo dpkg-reconfigure keyboard-configuration

You will need to restart the Dragonboard if you change the keyboard configuration.

Load the libsoc GPIO library
----------------------------
Check that the correct and update packages are on the system.

.. code-block:: none

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get dist-upgrade
    sudo apt-get install man-db
    sudo apt-get install manpages manpages-dev
    sudo apt-get install autoconf automake libtool
    sudo apt-get install libpython-dev libpython3-dev
    sudo apt-get install python-support
    sudo apt-get install python3-tk
    wget https://github.com/jackmitch/libsoc/archive/0.8.1.tar.gz
    gtar -ztvf 0.8.1.tar.gz
    cd libsoc-0.8.1
    ./autogen.sh
    ./configure --enable-board=dragonboard410c --enable-python=3 |& tee py3_conf.log
    make V=1 |& tee make.log
    sudo make install
    sudo ldconfig -v -N

One more library
----------------
The examples in this workshop use a library that attempts to remove some of the boilerplate code required to interact
with the GPIO components in the kit. To install the libsoc_zero library.

.. code-block:: none

    sudo apt-get install python3-pip
    pip3 install libsoc_zero


Change PYTHONPATH
-----------------
The PYTHONPATH needs to be updated to include the libsoc library. This is best done in the .bashrc in your home
directory if you are using the default Linux install.
Use your favourite editor. If you do not have one then :code:`leafpad ~/.bashrc` is a good place to start.
We are also going to set the architecture in the .bashrc also.

.. code-block:: none

    export PYTHONPATH="$PYTHONPATH:/usr/local/lib/python3.4/site-packages"
    export ARCH=arm64


To interact with the GPIO Python scripts will need to be run as sudo. This means that super user needs
    the PYTHONPATH environment variable set also.
    This will need to be done with a special command. To open for edit type :code:`sudo visudo`

The line that you need to add is:

.. code-block:: none

    Defaults env_keep += "PYTHONPATH"

This has to be done using the :code:`vi` editor. This can be a tricky editor for the casual user.
Use the cursor keys to move around then press the :code:`i` key to be able to start typing. Use :code:`ESC` key to stop typing.
To save and exit it is :code:`:wq` key sequence. (If you get in mess then to quit without saving it is :code:`ESC`
followed by :code:`:q!`

Installing Python Editor (IDE)
------------------------------
if you have a favourite editor and want to run your Python scripts from the command line then go ahead. If this is
all new to use then maybe take a look at the default Python integrated development environment. To install.

.. code-block:: none

    sudo apt-get install idle3

As super user access is required for the GPIO then when you start the tool you will need to do :code:`sudo idle3 <file>`
Enter one of the examples elsewhere in this documentation and then select run.
If you want to come back and run your files later without editing them then this can be done with
:code:`sudo python3 <file>`
