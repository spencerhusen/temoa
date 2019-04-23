#!/bin/bash
cd project
javac FileSelector.java
java FileSelector
cd ..
python temoa_model/ --config=project/config_sample
