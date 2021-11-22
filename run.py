#!/usr/bin/env python3

import os
import requests

source = os.getcwd() + "/data/feedback"
post_url = "www.example.com"

def get_source_files():
	return []

def process_file_to_json(file):
	return ""

def post_json(json):
	return 200

if __name__ == "__main__":
	files = get_source_files()
	for file in files:
		json = process_file_to_json(file)
		http_response = post_json(json)
		print "{}, {}".format(file, http_response)
