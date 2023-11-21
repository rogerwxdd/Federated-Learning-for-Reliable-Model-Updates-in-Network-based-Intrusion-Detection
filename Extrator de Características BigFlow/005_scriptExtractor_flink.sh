#!/bin/sh
NRUNNING=0
RODOU=0
MAX_JOBS=3

DATASET='/home/viegas/Bases4/scripts/2017_MAWI/txt'
FLINK='/root/roger/flink-1.3.1/flink-1.3.1/bin/flink'
BIGFLOW='/root/roger/BigFlow'

for FILE in $DATASET/2017*.txt
do
        RODOU=0
        while [ $RODOU != 1 ];
        do
                        NRUNNING=$($FLINK list)
                        if echo "$NRUNNING" | egrep "RUNNING|running"
                        then
                                        echo "Consulta nao deu pau"
                                        NRUNNING=$($FLINK list | grep RUNNING | wc -l)
                                        echo "  Quantidade de jobs: " $NRUNNING
                                        if [ "$NRUNNING" -lt "$MAX_JOBS" ]
                                        then
                                                        ARQ=$FILE
                                                        DESC="echo $ARQ | cut -c1-50"
                                                        DESC=$(eval $DESC)
                                                        DESC=$DESC"_anomalous_suspicious.csv"
                                                        ARFF=$FILE
                                                        EXEC="$FLINK run -p 16 $BIGFLOW/target/BigFlow-1.0-SNAPSHOT-jar-with-dependencies.jar extractor $ARQ $DESC $ARFF"".arff"
                                                        echo $EXEC
                                                        eval $EXEC &
                                                        RODOU=1
                                        else
                                                        echo "esperando terminar algum job..."
                                        fi
                        else
                                        echo "Deu pau na consulta"
                        fi
                        sleep 2m
        done
done




