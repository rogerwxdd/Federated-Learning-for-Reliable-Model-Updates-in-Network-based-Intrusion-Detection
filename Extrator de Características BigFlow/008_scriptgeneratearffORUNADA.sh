#!/bin/sh
for file in *ORUNADA_unique
do
        ARQ=$file
	NEWARQ=${ARQ%".pcap.txt.arff.propstrat.weka_ORUNADA_unique"}
	touch $NEWARQ"_ORUNADA.arff"
	cat /root/roger/BigFlow/orunada_arff_header >> $NEWARQ"_ORUNADA.arff"
	cat $ARQ >> $NEWARQ"_ORUNADA.arff"
	echo $NEWARQ
done
#mv *_ORUNADA.arff orunada/
