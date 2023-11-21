#!/bin/bash


MOORE=008_scriptgeneratearffMOORE.sh
NIGEL=008_scriptgeneratearffNIGEL.sh
ORUNADA=008_scriptgeneratearffORUNADA.sh
VIEGAS=008_scriptgeneratearffVIEGAS.sh

sh $MOORE
while ps aux | egrep "*/bkpsibrax\.sh$" >/dev/null
do
	echo "executando"
done
echo "FINALIZOU MOORE"


sh $NIGEL
while ps aux | egrep "*/bkpsibrax\.sh$" >/dev/null
do
	echo "executando"
done
echo "FINALIZOU NIGEL"

sh $ORUNADA
while ps aux | egrep "*/bkpsibrax\.sh$" >/dev/null
do
	echo "executando"
done
echo "FINALIZOU ORUNADA"

sh $VIEGAS
while ps aux | egrep "*/bkpsibrax\.sh$" >/dev/null
do
	echo "executando"
done
