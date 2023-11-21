#!/bin/sh

echo "INICIANDO........"

for FILE in *.arff
do
	ARQ=$FILE
	DESC="echo $ARQ | cut -c1-8"
	DESC=$(eval $DESC)
	DESC=$DESC"_anomalous_suspicious.csv"
	#echo $FILE
	#echo $DESC
	
	if [ -e $DESC ] ; then 
	   a=OK
	else
	   echo "$DESC Nao encontrado"
	fi
done

echo "FIM TXT"

for FILE in *.csv
do
	ARQ=$FILE
	DESC="echo $ARQ | cut -c1-8"
	DESC=$(eval $DESC)
	DESC=$DESC"*.arff"
	#echo $FILE
	#echo $DESC
	
	if [ -e $DESC ] ; then 
	   a=OK
	else
	   echo "$DESC Nao encontrado"
	fi
done

echo "FIM CSV"
