#!/bin/bash
echo Enter input file: 
read datafile
cd project
python FileSelector.py $datafile
cd ..
python temoa_model/ --config=project/config_sample
