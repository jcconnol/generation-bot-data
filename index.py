from dataGen import generateChain
from s3Upload import s3Upload

bucket_name = "bot-gen"

def main():
    s3_file_array = [
        {
            "object_path": "tweets.json",
            "list_file": "./result_objects/poems.json",
            "word_limit": 50
        },
        {
            "object_path": "rapSongs.json",
            "list_file": "./result_objects/rapSongLyrics.json",
            "word_limit": 500
        },
        {
            "object_path": "tweets.json",
            "list_file": "./result_objects/tweets.json",
            "word_limit": 500
        }
    ]
    
    generateChain()
    
    for generated_chain in s3_file_array:
        print(generated_chain)
        s3Upload(bucket_name, generated_chain["object_path"], generated_chain["list_file"])


if __name__=="__main__":
    main()