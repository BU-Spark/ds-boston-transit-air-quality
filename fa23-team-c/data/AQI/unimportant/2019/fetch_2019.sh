#!/bin/bash

# https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/2019/20190101/HourlyData_2019010100.dat

y=2019

for hour in {0..9}; do
    for d in {1..9}; do
        for m in {1..9}; do
            # echo $y
            wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}0${m}0${d}/HourlyData_${y}0${m}0${d}0${hour}.dat"
        done

        for m in {10..12}; do
            # echo $y
            wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}${m}0${d}/HourlyData_${y}${m}0${d}0${hour}.dat"
        done
    done 

    for d in {10..31}; do
        for m in {1..9}; do
            # echo $y
            wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}0${m}${d}/HourlyData_${y}0${m}${d}0${hour}.dat"
        done

        for m in {10..12}; do
            # echo $y
            wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}${m}${d}/HourlyData_${y}${m}${d}0${hour}.dat"
        done
    done 
done

for hour in {10..23}; do
    for d in {1..9}; do
        for m in {1..9}; do
            # echo $y
            wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}0${m}0${d}/HourlyData_${y}0${m}0${d}${hour}.dat"
        done

        for m in {10..12}; do
            # echo $y
            wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}${m}0${d}/HourlyData_${y}${m}0${d}${hour}.dat"
        done
    done 

    for d in {10..31}; do
        for m in {1..9}; do
            # echo $y
            wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}0${m}${d}/HourlyData_${y}0${m}${d}${hour}.dat"
        done

        for m in {10..12}; do
            # echo $y
            wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/$y/${y}${m}${d}/HourlyData_${y}${m}${d}${hour}.dat"
        done
    done 
done

mkdir $y
mv *.dat $y
