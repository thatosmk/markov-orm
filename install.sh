#!/bin/bash

NAME=pymarkov
DIR='/usr/local/bin'
CDIR=`pwd`

# check if a local scripts directory exists
if [ -d "$DIR" ]; then
		# install the script at the path
		echo 'Installing pymarkov...'
		touch pysqlmarkov
		echo '#!/bin/bash
		python ~/.markovorm/console.py' >> pysqlmarkov
		sudo chmod a+x pysqlmarkov
		sudo cp markovorm/pymarkov $DIR
		echo 'Setting home directory...'
		cp -r markovorm/* ~/.markovorm
fi

