#!/usr/bin/env python

import yaml
import json

dict_file = {'first_name' : 'Scott',
	'last_name' : 'Johnson',
	'company' : 'WWT',
	'email' : 'scott.johnson@wwt.com',
	'github_username' : 'The-Corfu'}

with open(r'/Users/scott/store_file.yaml', 'w') as file:
	documents = yaml.dump(dict_file, file)
