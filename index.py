import boto3

def main():
    print("hey there")
    bucket_name = "bot-gen"
    s3_object = "tweets.json"

    #TODO read tweets file, build markov object and save to tweet.json
    #TODO read poem file, build markov object and save to poem.json
    #TODO read movie data, build markov object and save to movie-[genre].json
    #TODO read site data, build markov object and save to movie-[sitename].json
    
    s3_object_body = "Be curious, not judgemental1"

    sendDataTos3(bucket_name, s3_object, s3_object_body)



# send to s3 bucket
def sendDataTos3(bucket_name, s3_object, s3_object_body):
    s3_resource = boto3.resource("s3")

    upload_result = s3_resource.Object(bucket_name, s3_object).put(Body=s3_object_body)
    print(upload_result)
    assert upload_result["ResponseMetadata"]["HTTPStatusCode"] == 200

    text_file_from_s3 = (
        s3_resource.Object(bucket_name, s3_object).get()["Body"].read().decode("utf-8")
    )
    print(text_file_from_s3)
    assert s3_object_body == text_file_from_s3
    
if __name__=="__main__":
    main()