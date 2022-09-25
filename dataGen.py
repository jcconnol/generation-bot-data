import random
import sys
import json 
import os

GENERATION_FILEPATH = "generation_sets"
RESULT_FILEPATH = "result_objects"

def clean_array(dirty_array):
    clean_array = []
    for elem in dirty_array:
        clean_string = elem.replace('[', '')
        clean_string = clean_string.replace(']', '')
        clean_array.append(clean_string)
        
    return clean_array

def generateChain():
	for dataset in os.listdir(os.path.join(sys.path[0], GENERATION_FILEPATH)):
		data_directory = os.path.join(sys.path[0], GENERATION_FILEPATH+"\\"+dataset)
	
		all_lines = []

		for generation_file in os.listdir(data_directory):		
			file_path = os.path.join(sys.path[0], GENERATION_FILEPATH+"\\"+dataset+"\\"+generation_file)
	
			lines = open(file_path, "r").read()
			lines = ''.join([i for i in lines if not i.isdigit()]).replace("\n", " ").split(' ')
			lines = clean_array(lines)
			all_lines.extend(lines)

		index = 1
		chain = {}
		count = 200 # Desired word count of output
		print(len(lines))
		for word in all_lines[index:]: 
			key = all_lines[index - 1]
			if key in chain:
				chain[key].append(word)
			else:
				chain[key] = [word]
			index += 1

		chain_file_path = os.path.join(sys.path[0], RESULT_FILEPATH+"\\"+dataset+".json")
		chain_json = json.dumps(chain, indent = 4)
		with open(chain_file_path, "w") as file:
			file.write(chain_json)