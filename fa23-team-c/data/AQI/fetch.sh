#!/bin/bash

for x in {20210101..20211231}; do
    wget "https://s3-us-west-1.amazonaws.com/files.airnowtech.org/airnow/2021/$x/HourlyAQObs_${x}00.dat"
done