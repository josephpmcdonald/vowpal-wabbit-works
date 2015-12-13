#!/bin/bash

python preproc.py 0.1 1 2
vw -d train.dat -f data.model --cache_file train.cache --loss_function hinge
vw -t -d test.dat -i data.model -p test.pred --cache_file test.cache 
python postproc.py



