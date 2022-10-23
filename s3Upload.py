import boto3
import random
import json
import hashlib

# send to s3 bucket
def s3Upload(bucket_name, object_path, upload_text):
    print("starting upload of {}".format(object_path))
    
    s3_resource = boto3.resource("s3")

    s3_object_body = upload_text.encode('utf-8', errors='ignore')

    upload_result = s3_resource.Object(bucket_name, object_path).put(Body=s3_object_body)

    assert upload_result["ResponseMetadata"]["HTTPStatusCode"] == 200
    
    print("Completed!")

