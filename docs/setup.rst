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
The above release has a US based keyboard configuration. If you need chang it then use:

.. code-block:: none

    sudo dpkg-reconfigure keyboard-configuration

You will need to restart Dragonboard if you change the keyboard configuration.

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
    git clone https://github.com/jackmitch/libsoc.git
    cd libsoc
    ./autogen.sh
    ./configure --enable-board=dragonboard410c --enable-python3 |& tee py3_conf.log
    make V=1 |& tee make.log
    sudo make install
    sudo ldconfig -v -N


Change PYTHONPATH
-----------------
The PYTHONPATH needs to be updated to include the libsoc library
This can be set system wide in the /etc/environment file. This can be edited with `sudo` and your favourite editor.

.. code-block:: none

    PYTHONPATH=/usr/local/lib/python3.4/site-packages

Also set the architecture:

.. code-block:: none

    ARCH=arm64


To interact with the GPIO Python scripts will need to be run as sudo. This means that super user needs
    the PYTHONPATH environment variable set also.
    This will need to be done with a special command. To open for edit type

.. code-block:: none

    sudo visudo

The line that you need to add is:

.. code-block:: none

    Defaults env_keep += "PYTHONPATH"


The experiments in the workshop will be run in the following manner:

.. code-block:: none

    sudo python3 my_code.py
