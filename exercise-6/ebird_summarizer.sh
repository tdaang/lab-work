#! /bin/bash
replace_newlines.sh $1 

sed 's/,\s/ /g' formatted_$1 > reformatted_$1

python does_something.py reformatted_$1