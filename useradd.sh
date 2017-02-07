#!/bin/bash
user="stutest"
i=1
while [ $i -le 20 ]
do
useradd $user$i &> /dev/null
echo "$user$i has been added successfully!"
let i++
done