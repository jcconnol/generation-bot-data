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
        clean_string = clean_string.replace('(', '')
        clean_string = clean_string.replace(')', '')
        clean_string = clean_string.replace(',', '')
        clean_string = clean_string.replace('\'', '')
        clean_string = clean_string.replace('"', '')
        clean_array.append(clean_string)
        
    return clean_array

def generateChain(object):
	
	
	all_lines = []
	data_directory = os.getcwd() + object["set_generation"]
	print(data_directory)
	for generation_file in os.listdir(data_directory):		
		file_path = os.path.join(sys.path[0], data_directory+"\\"+generation_file)

		lines = open(file_path, "r").read()
		lines = ''.join([i for i in lines if not i.isdigit()]).replace("\n", " ").split(' ')
		lines = clean_array(lines)
		all_lines.extend(lines)

	index = 1
	chain = {}
	
	for word in all_lines[index:]: 
		key = all_lines[index - 1]
		if key in chain:
			chain[key].append(word)
		else:
			chain[key] = [word]
		index += 1
	
	return chain

def generateTextFromChain(input_chain, max_message_count):
    
	word1 = random.choice(list(input_chain.keys())) #random first word

	message = word1.capitalize()
	while len(message.split(' ')) < max_message_count:
		if word1 in input_chain:
			word2 = random.choice(input_chain[word1])
			word1 = word2
			message += ' ' + word2
		else:
			break

	return message