#!/bin/bash

module purge
module load python/gcc/3.7.9

python MrJob_CommonFriends.py ../Friends.csv -r hadoop \
       --hadoop-streaming-jar $HADOOP_LIBPATH/$HADOOP_STREAMING \
       --output-dir common_friends \
       --python-bin /share/apps/peel/python/3.7.9/gcc/bin/python \
