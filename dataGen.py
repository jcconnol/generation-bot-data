import random
import sys
import json 
import os

GENERATION_FILEPATH = "generation_sets"
RESULT_FILEPATH = "chain_objects"

def clean_array(dirty_array):
    clean_array = []
    for elem in dirty_array:
        clean_string = elem.replace('[', '')
        clean_string = clean_string.replace(']', '')
        clean_string = clean_string.replace('(', '')
        clean_string = clean_string.replace(')', '')
        clean_string = clean_string.replace(',', '')
        clean_string = clean_string.replace('\'', '')
        clean_string = clean_string.replace('"', '')
        clean_string = clean_string.replace('\n', '')
        clean_string = clean_string.replace('*', '')
        clean_string = clean_string.replace('\t', '')
        clean_string = clean_string.replace(' ', '')
        clean_string = clean_string.replace(':', '')
        clean_array.append(clean_string)
        
    return clean_array

def generateChain(generation_object):
	all_lines = []
	data_directory = os.getcwd() + "\\" + generation_object["generation_path"] 
 
	for generation_file in os.listdir(data_directory):		
		file_path = os.path.join(sys.path[0], data_directory+"\\"+generation_file)

		lines = open(file_path, "r").read()
		lines = remove_non_ascii(''.join([i for i in lines if not i.isdigit()])).replace("\n", " ").split(' ')
		lines = clean_array(lines)
		all_lines.extend(lines)

	index = 1
	chain = {}
	
	for word in all_lines[index:]: 
		key = all_lines[index - 1].upper()
		word = word.upper()
		if key in chain:
			chain[key].append(word.upper())
		else:
			chain[key] = [word]
		index += 1
	
	chain_file_path = os.getcwd() + "\\" + generation_object["upload_file"]
	chain_json = json.dumps(chain, indent = 4)
 
	with open(chain_file_path, "w") as file:
		file.write(chain_json)
   
def generateUploadObjects(generation_object):
	print("generating")
    
	print(generation_object)
	input_chain_path = os.getcwd() + "\\" + generation_object["list_file"]
	max_message_count = generation_object["word_limit"]
    
	input_chain = json.loads(open(input_chain_path, "r").read())
	generated_text = ""
	for i in range(100):
		generated_text += generateTextFromChain(input_chain, max_message_count)
		generated_text += "\n||||||||||||||||||||||||||\n"
    
	upload_file_path = os.getcwd() + "\\" + generation_object["upload_file"]
	with open(upload_file_path, "w") as file:
		file.write(generated_text)
    
    
    
def generateTextFromChain(input_chain, max_message_count):
	word1 = random.choice(list(input_chain.keys())) #random first word
	message = word1
	while len(message.split(' ')) < max_message_count:
		if word1 in input_chain:
			word2 = random.choice(input_chain[word1])
			word1 = word2
			message += ' ' + word2
		else:
			break
		
	return message

def remove_non_ascii(s):
    return "".join(c for c in s if ord(c)<128)
