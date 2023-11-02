#!/bin/bash

#https://files.airnowtech.org/?prefix=airnow/2014/20140101/


for x in {2020..2023}; do
    # echo $x

    for y in {1..9}; do
        # echo $y
        wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$x/${x}0${y}01/HourlyAQObs_${x}0${y}0100.dat"
    done

    for y in {10..12}; do
        # echo $y
        wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$x/${x}${y}01/HourlyAQObs_${x}${y}0100.dat"
    done

done