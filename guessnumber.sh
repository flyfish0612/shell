#!/bin/bash
price=$( expr $RANDOM % 1000 )
times=0
echo "The price is 0-999 .please guess it."
while true
do
  read -p "Please enter your price: " INT
  let times++
if 
   [ $INT -eq $price ]
then 
  echo "Great! You got it!"
  echo "You guess $times times."
  exit 0
elif
  [ $INT -gt $price ]
then
  echo "Too high!"
else
  echo "Too low!"
fi
done