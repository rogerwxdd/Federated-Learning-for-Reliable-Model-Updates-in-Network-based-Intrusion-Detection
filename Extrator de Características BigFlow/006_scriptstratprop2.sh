#!/bin/bash
#for file in 201307*.arff 201308*.arff 201309*.arff
for file in *.arff
do
        echo $file
        CMD="touch $file"".propstrat"
        eval $CMD
	cat $file | cut -d, -f146 | grep -E "normal|suspicious|anomalous" |sort --parallel=18 | uniq -c > $file".count"
	NNORMAL=$(cat $file".count" | grep normal | sed 's/[^0-9]//g')
	NATTACK=$(cat $file".count" | grep anomalous | sed 's/[^0-9]//g')
	NSUSPICIOUS=$(cat $file".count" | grep suspicious | sed 's/[^0-9]//g')
	rm $file".count"
	NATTACK=$((NATTACK / 100))
	NNORMAL=$((NNORMAL / 100))
	NSUSPICIOUS=$((NSUSPICIOUS/ 100))
	echo "attack: " $NATTACK
	echo "normal: "$NNORMAL
	echo "suspicious: " $NSUSPICIOUS
	echo "greping normal..."
	CMD="LC_ALL=C fgrep normal $file | shuf -n $NNORMAL >> $file.propstrat"
	eval $CMD
	echo "greping anomalous..."
	CMD="LC_ALL=C fgrep anomalous $file | shuf -n $NATTACK >> $file.propstrat"
        eval $CMD
	echo "greping suspicious..."
	CMD="LC_ALL=C fgrep suspicious $file | shuf -n $NSUSPICIOUS >> $file.propstrat"
        eval $CMD
done
