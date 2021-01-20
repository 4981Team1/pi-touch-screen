# How to run a Kivy app on your Raspberry PI

## Kivy requires python 3.6 or greater on your machine, we will first be installing Python 3.8.0

1. Open terminal and run: 

	```sudo apt-get update```

2. Install the prerequisites for Python 3.8:

	```sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim```

3. Download Python 3.8 from the official website:

	```wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz```

4. Extract and Install Python 3.8:

	```sudo tar zxf Python-3.8.0.tgz```
	```cd Python-3.8.0```
	```sudo ./configure --enable-optimizations```
	```sudo make -j 4```
	```sudo make altinstall```

5. Ensure that Python 3.8 has been installed:

	```python3.8 -V```

6. Make Python 3.8 the default:

	```echo "alias python=/usr/local/bin/python3.8" >> ~/.bashrc```
	```source ~/.bashrc```

7. Ensure that Python 3.8 is the default:

	```python -V```

	note: the output should be "Python 3.8.0"

Next we will be installing [kivy](https://kivy.org/doc/stable/gettingstarted/installation.html) and its [dependencies](https://kivy.org/doc/stable/installation/installation-rpi.html#install-source-rpi). Instructions are taken from the following kivy documentation links

