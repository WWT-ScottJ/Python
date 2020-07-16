#!/usr/bin/env python
# process_yaml.py file

import yaml
import json

with open(r'/Users/scott/categories.yaml') as file:
 
	documents = yaml.full_load(file)
	
	for item, doc in documents.items():
	  print(item, ":", doc)
