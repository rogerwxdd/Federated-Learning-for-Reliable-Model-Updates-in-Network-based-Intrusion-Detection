#!/bin/sh
for file in *.propstrat
do
        ARQ=$file
	CMD="java -jar /root/roger/BigFlow/target/BigFlow-1.0-SNAPSHOT-jar-with-dependencies.jar stratification $ARQ $ARQ.weka"
	echo $CMD
	eval $CMD
done
