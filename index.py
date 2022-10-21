from dataGen import generateChain
from dataGen import generateTextFromChain
from s3Upload import s3Upload

bucket_name = "bot-gen"

def main():
    s3_file_array = [
        {
            "object_path": "poems.json",
            "list_file": "./result_objects/poems.json",
            "set_generation": "\\generation_sets\\poems",
            "word_limit": 50
        },
        {
            "object_path": "rapSongs.json",
            "list_file": "./result_objects/rapSongLyrics.json",
            "set_generation": "\\generation_sets\\rapSongLyrics",
            "word_limit": 500
        },
        {
            "object_path": "tweets.json",
            "list_file": "./result_objects/tweets.json",
            "set_generation": "\\generation_sets\\tweets",
            "word_limit": 500
        }
    ]
    
    for object in s3_file_array:
        generated_chain = generateChain(object)

        generated_text = generateTextFromChain(generated_chain, object["word_limit"])
        print(generated_text)
        s3Upload(bucket_name, object["object_path"], generated_text)

if __name__=="__main__":
    main()