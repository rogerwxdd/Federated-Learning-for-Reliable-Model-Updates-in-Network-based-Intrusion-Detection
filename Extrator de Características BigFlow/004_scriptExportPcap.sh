#!/bin/sh
for file in *.pcap
do
	ARQ=$file
	CMD="pcapreaderlibpcap $ARQ $ARQ"".txt"
	echo $CMD
	eval $CMD
	#rm $ARQ
	#eval $ARQ
	#sleep 10m 
done
