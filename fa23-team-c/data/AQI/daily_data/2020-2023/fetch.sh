#!/bin/bash

#https://files.airnowtech.org/?prefix=airnow/2014/20140101/


for y in {2020..2023}; do

    for hour in {0..9}; do
        for d in {1..9}; do
            for m in {1..9}; do
                # echo $y
                wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}0${m}0${d}/HourlyAQObs_${y}0${m}0${d}0${hour}.dat"
            done

            for m in {10..12}; do
                # echo $y
                wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}${m}0${d}/HourlyAQObs_${y}${m}0${d}0${hour}.dat"
            done
        done 

        for d in {10..31}; do
            for m in {1..9}; do
                # echo $y
                wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}0${m}${d}/HourlyAQObs_${y}0${m}${d}0${hour}.dat"
            done

            for m in {10..12}; do
                # echo $y
                wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}${m}${d}/HourlyAQObs_${y}${m}${d}0${hour}.dat"
            done
        done 
    done

    for hour in {10..23}; do
        for d in {1..9}; do
            for m in {1..9}; do
                # echo $y
                wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}0${m}0${d}/HourlyAQObs_${y}0${m}0${d}${hour}.dat"
            done

            for m in {10..12}; do
                # echo $y
                wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}${m}0${d}/HourlyAQObs_${y}${m}0${d}${hour}.dat"
            done
        done 

        for d in {10..31}; do
            for m in {1..9}; do
                # echo $y
                wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}0${m}${d}/HourlyAQObs_${y}0${m}${d}${hour}.dat"
            done

            for m in {10..12}; do
                # echo $y
                wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}${m}${d}/HourlyAQObs_${y}${m}${d}${hour}.dat"
            done
        done 
    done

    mkdir $y
    mv *.dat $y

done