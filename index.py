from dataGen import generateChains
from s3Upload import s3Upload
from dataGen import generateUploadObjects

bucket_name = "bot-gen"

def main():
    s3_file_array = [
        {
            "object_path": "tweets.json",
            "list_file": "./chain_objects/poems.json",
            "upload_file": "./upload_objects/poems.json",
            "word_limit": 50
        },
        {
            "object_path": "rapSongs.json",
            "list_file": "./chain_objects/rapSongLyrics.json",
            "upload_file": "./upload_objects/rapSongLyrics.json",
            "word_limit": 500
        },
        {
            "object_path": "tweets.json",
            "list_file": "./chain_objects/tweets.json",
            "upload_file": "./upload_objects/tweets.json",
            "word_limit": 500
        }
    ]
    
    generateChains()
    
    for generation_object in s3_file_array:
        print(generation_object)
        generateUploadObjects(generation_object)
        # s3Upload(bucket_name, generation_object["object_path"], generation_object["list_file"])

if __name__=="__main__":
    main()