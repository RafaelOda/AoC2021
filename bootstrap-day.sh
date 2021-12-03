#!/bin/bash

DAY=`printf day%02d $1`
echo "Bootstrapping $DAY";

mv "${HOME}/Downloads/input-${DAY}.txt" "./inputs/${DAY}.txt"

cat > "solutions/${DAY}.py"  <<- EOF
def part1(input_data):
    pass
def part2(input_data):
    pass
EOF