#!/bin/sh

i=$1
j=1
while [ $j -le 31 ];
do
        if [ "$i" -lt 10 ]
        then
			 ARQ="wget -c -t 10 http://mawi.nezu.wide.ad.jp/mawi/samplepoint-F/2017/20170$i"
        else
			ARQ="wget -c -t 10 http://mawi.nezu.wide.ad.jp/mawi/samplepoint-F/2017/2017$i"
        fi
        if [ "$j" -lt 10 ]
        then
			ARQ="$ARQ""0$j"
        else
			ARQ="$ARQ""$j"
        fi

        ARQ="$ARQ""1400.pcap.gz"

        echo $j
        echo $ARQ
        eval $ARQ

        j=$((j+1))

done

