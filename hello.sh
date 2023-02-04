#!/bin/bash

a=2
b=2
c=$((a + b))

echo "Bash says: Hello, World!"
echo "$a + $b = $c"

echo ""
echo "Part 2 Starts:"

# Loop was inspired by content from thread: 
# https://stackoverflow.com/questions/8880603/loop-through-an-array-of-strings-in-bash

declare -a userArr=("User1" "User2" "User3")

for i in "${userArr[@]}"
do
	echo "$i"
done
