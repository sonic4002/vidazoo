#! /bin/bash

DAY=`date +%d`
MON=`date +%m`
YEA=`date +%y`

echo -n "Hi , Enter your name and Date of Birth [Enter] : "
read line

if [[ $line =~ ^(.*)' '([0-9]{2})/([0-9]{2})/([0-9]{2})$ ]];then
	if [[ ${BASH_REMATCH[2]} == $DAY ]] && [[ ${BASH_REMATCH[3]} == $MON ]] && [[ ${BASH_REMATCH[4]} == $YEA ]];then
		echo "Happy B-Day! ${BASH_REMATCH[1]}"
	else
		echo "No gifts for you... NEXT!!!"
	fi
else
	echo "incorrect input"
fi