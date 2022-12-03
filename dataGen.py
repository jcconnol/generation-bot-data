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

<<<<<<< HEAD
def generateChains():
	for dataset in os.listdir(os.path.join(sys.path[0], GENERATION_FILEPATH)):
		data_directory = os.path.join(sys.path[0], GENERATION_FILEPATH+"\\"+dataset)
	
	for word in all_lines[index:]: 
		key = all_lines[index - 1].upper()
		word = word.upper()
		if key in chain:
			chain[key].append(word.upper())
		else:
			chain[key] = [word]
		index += 1
	
	return chain

<<<<<<< HEAD
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
   
def generateUploadObjects(generation_object):
    print("generating")
    
    print(generation_object)
    input_chain
    max_message_count = generation_object[""]
    
    generated_text = generateTextFromChain(input_chain, max_message_count)
    
    
    
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
