from dataGen import generateChain
from s3Upload import s3Upload
from dataGen import generateUploadObjects

bucket_name = "bot-gen"

def main():
    s3_file_array = [
        {
            "object_path": "poems.txt",
            "generation_path": "\\generation_sets\\poems\\",
            "list_file": "\\chain_objects\\poems.json",
            "upload_file": "\\upload_objects\\poems.txt",
            "word_limit": 50
        },
        {
            "object_path": "rapSongs.txt",
            "generation_path": "\\generation_sets\\rapSongLyrics\\",
            "list_file": "\\chain_objects\\rapSongLyrics.json",
            "upload_file": "\\upload_objects\\rapSongLyrics.txt",
            "word_limit": 500
        },
        {
            "object_path": "tweets.txt",
            "generation_path": "\\generation_sets\\tweets\\",
            "list_file": "\\chain_objects\\tweets.json",
            "upload_file": "\\upload_objects\\tweets.txt",
            "word_limit": 500
        }
    ]
    
    for generation_object in s3_file_array:
        generateChain(generation_object)
        generateUploadObjects(generation_object)
        s3Upload(bucket_name, generation_object["object_path"], generation_object["upload_file"])

if __name__=="__main__":
    main()