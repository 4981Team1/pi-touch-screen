# How to run a Kivy app on your Raspberry PI

## Installing Python 3.8

1. Open terminal and run: 

	```sudo apt-get update```

2. Install the prerequisites for Python 3.8:

	```sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim```

3. Download Python 3.8 from the official website:

	```wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz```

4. Extract and Install Python 3.8:

	```
	sudo tar zxf Python-3.8.0.tgz
	cd Python-3.8.0
	sudo ./configure --enable-optimizations
	sudo make -j 4
	sudo make altinstall
	```

5. Ensure that Python 3.8 has been installed:

	```python3.8 -V```

6. Make Python 3.8 the default:

	```
	echo "alias python=/usr/local/bin/python3.8" >> ~/.bashrc
	source ~/.bashrc
	```

7. Ensure that Python 3.8 is the default:

	```python -V```

	note: the output should be "Python 3.8.0"
	
## Installing Kivy
Next install [kivy](https://kivy.org/doc/stable/gettingstarted/installation.html) and its [dependencies](https://kivy.org/doc/stable/installation/installation-rpi.html#install-source-rpi). Instructions are taken from the following kivy documentation links

## Running The Program and Casting a Vote

1. Pull the code in this repository, starting from the voting_machine_ui directory

2. Place the directory into your pi

3. Navigate to your working directory and 'cd' into the folder

4. Run the program by running

	```
	python vm_machine.py
	```
	Note: This requires Python and Kivy to be installed on the pi
	
When ran, the program will be forced into full-screen mode. The only way to exit out of this is the Exit button in the homescreen

5. Enter your created user account's email and password

6. Select one of the elections

7. Select an option

8. Confirm the vote details

9. When the vote is cast, you will go back to the elections list screen and the election in which you just placed the vote will be gone. This is to prevent multiple votes in the same election
