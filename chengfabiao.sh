#!/bin/bash

echo "this is a cheng fa biao:"

for((i=1;i<10;i++))
do 
	for((j=1;j<=i;j++))
	do	
	echo -n "$j*$i=$(($i*$j)) "
		if [ $j -eq $i ]
		then
		echo -e '\n'
		fi
	done
done
