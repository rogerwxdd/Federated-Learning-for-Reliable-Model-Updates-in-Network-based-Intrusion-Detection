#!/bin/sh
for file in *NIGEL_unique
do
        ARQ=$file
	NEWARQ=${ARQ%".pcap.txt.arff.propstrat.weka_NIGEL_unique"}
	touch $NEWARQ"_NIGEL.arff"
	cat /root/roger/BigFlow/nigel_arff_header >> $NEWARQ"_NIGEL.arff"
	cat $ARQ >> $NEWARQ"_NIGEL.arff"
	echo $NEWARQ
done
#mv *NIGEL.arff nigel/
