#!/bin/bash


graphFiles=`ls ./data/ | grep .graph`

for graph in ${graphFiles}
do
	filename=`echo ${graph} | cut -d'.' -f1`
	echo ${graph} ${filename}
	python3 ./src/test.py -inst ./data/${graph}  -alg Approx -time 3 -seed 5


done
