#!/bin/sh
for file in *MOORE_unique
do
        ARQ=$file
	NEWARQ=${ARQ%".pcap.txt.arff.propstrat.weka_MOORE_unique"}
	touch $NEWARQ"_MOORE.arff"
	cat /root/roger/BigFlow/moore_arff_header >> $NEWARQ"_MOORE.arff"
	cat $ARQ >> $NEWARQ"_MOORE.arff"
	echo $NEWARQ
done
#mv *_MOORE.arff moore/
