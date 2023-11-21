#!/bin/sh

j=0

while [ $j -le 31 ];
do

		if [ "$i" -lt 10 ]
        then
			i=0$1
		else
			i=$1
		fi
		
		
		if [ "$j" -lt 10 ]
        then
			jj=0$j
		else
			jj=$j
		fi				
		
		ARQ="wget -c -t 10 http://www.fukuda-lab.org/mawilab/v1.1/2017/$i/$jj/2017$i""$jj""_anomalous_suspicious.csv"

        echo $j
        echo $ARQ
        eval $ARQ

        j=$((j+1))

done

