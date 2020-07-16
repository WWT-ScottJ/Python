#!/usr/bin/env python
# process_yaml.py file

import yaml
import json

with open(r'/Users/scott/fruits.yaml') as file:
 # The FullLoader parameter handles the conversion from YAML
 #scalar values to Python the dictionary format
	fruits_list = yaml.load(file, Loader=yaml.FullLoader)

	print(fruits_list)
