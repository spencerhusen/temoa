#!/bin/bash
echo Enter input file: 
read datafile
cd project
python FileSelector.py $datafile
cd ..
python temoa_model/ --config=temoa_model/config_sample
