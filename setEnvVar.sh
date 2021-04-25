#!/bin/bash
file="tokensandkeys.txt"
set -o allexport
while read line; do
	if [[ $line =~ ^[[:space:]]*\#.*$ ]]; then
		true
	else
		export $line
	fi
done < $file
set +o allexport
echo "Export Successfull!"
bash
