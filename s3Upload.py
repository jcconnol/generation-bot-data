import boto3
import random
import json

#TODO read movie data, build markov object and save to movie-[genre].json
#TODO read song data, build markov object and save to song-[genre].json

def main():
    print("starting build...")
    bucket_name = "bot-gen"
    
    s3FileArray = [
        {
            "object_path": "tweets.json",
            "list_file": "lists/siteList.txt",
            "word_limit": 50
        },
        {
            "object_path": "poem.json",
            "list_file": "lists/poemList.txt",
            "word_limit": 100
        },
        {
            "object_path": "site-ramseysolutions.json",
            "list_file": "lists/siteList.txt",
            "word_limit": 500
        },
    ]

    
    for file in s3FileArray:
        file_text = open(file["list_file"], "r").read()
        file_text = ''.join([i for i in file_text if not i.isdigit()]).replace("\n", " ").split(' ')

        index = 0
        chain = {}
        prev_word = ""

        for word in file_text:
            if index == 0:
                prev_word = word
            else:
                key = file_text[index - 1]
                if key in chain:
                    chain[key].append(word)
                else:
                    chain[key] = [word]
            index += 1

        word1 = random.choice(list(chain.keys())) #random first word
        message = word1.capitalize()
        
        while len(message.split(' ')) < file["word_limit"]:
            word2 = random.choice(chain[word1])
            word1 = word2
            message += ' ' + word2

        json_object_body = json.dumps(chain, indent = 4)

        print("starting upload...")

        sendDataTos3(bucket_name, file["object_path"], json_object_body)
        sendDataToDB(json_object_body)
        
        print("Completed!")



# send to s3 bucket
def sendDataTos3(bucket_name, s3_object, s3_object_body):
    s3_resource = boto3.resource("s3")

    upload_result = s3_resource.Object(bucket_name, s3_object).put(Body=s3_object_body)
    print(upload_result)
    assert upload_result["ResponseMetadata"]["HTTPStatusCode"] == 200

    text_file_from_s3 = (
        s3_resource.Object(bucket_name, s3_object).get()["Body"].read().decode("utf-8")
    )

    assert s3_object_body == text_file_from_s3

def sendDataToDB(data_object):
    print("db")


if __name__=="__main__":
    main()