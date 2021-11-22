#!/usr/bin/env python3

import os
import json
import requests

source = os.getcwd() + "/data/feedback"
post_url = "www.example.com"

def get_source_files():
	return os.listdir(source)

def process_file_to_json(file):
	with open("{}/{}".format(source,file)) as f:
		lines = f.read().splitlines()
		dict = {"title": lines[0], "name": lines[1], "date": lines[2], "feedback": lines[3:]}
		return json.dumps(dict)

def post_json(p_json):
	response = requests.post(post_url, json = p_json)
	return response.text

if __name__ == "__main__":
	files = get_source_files()
	for file in files:
		p_json = process_file_to_json(file)
		http_response = post_json(p_json)
		print ("{}, {}".format(file, http_response))
