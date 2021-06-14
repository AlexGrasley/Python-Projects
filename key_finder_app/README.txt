
This app will take in a list of words, include only the words of length 16 or less, loop through them and use
each as a key to encrypt some message text until we find the key used to originally encrypt the message

Requirements:

Files:
	collisionfinder.py
	keyfinder.py
	words.txt
	
Env:
	pycryptodome
	
	
Instructions:
	create a virtual python environment in a new folder on the OSU eng servers. I called my folder "key_finder_app"
		"pip install virtualenv"
		"virtualenv key_finder_app"
		"pip install pycryptodome"
		
	change directories to key_finder_app, copy "keyfinder.py" and "words.txt" into the folder
	
	Activate the virtual environment
		"source bin/activate"
		
	Run the keyfinder.py
		"python keyfinder.py"
		

Instructions for collisionfinder.py:
	Set up a virutual environment just like the key_finder_app instruction. Using the same one is even ok, since they have the same dependencies that were already installed in the first step. 