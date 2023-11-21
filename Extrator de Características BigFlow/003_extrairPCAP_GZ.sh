#!/bin/sh

ARQ=`ls -1 | egrep ".gz"`

for arquivo in $ARQ ; do
   echo $arquivo
   gunzip $arquivo
done 
