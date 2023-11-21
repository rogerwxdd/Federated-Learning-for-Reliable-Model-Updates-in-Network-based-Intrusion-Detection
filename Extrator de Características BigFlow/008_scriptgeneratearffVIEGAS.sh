#!/bin/sh
for file in *VIEGAS_unique
do
        ARQ=$file
	NEWARQ=${ARQ%".pcap.txt.arff.propstrat.weka_VIEGAS_unique"}
	touch $NEWARQ"_VIEGAS.arff"
	cat /root/roger/BigFlow/viegas_arff_header >> $NEWARQ"_VIEGAS.arff"
	cat $ARQ >> $NEWARQ"_VIEGAS.arff"
	echo $NEWARQ
done
#mv *_VIEGAS.arff viegas/
