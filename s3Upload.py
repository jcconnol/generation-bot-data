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


# send to s3 bucket
def sendDataTos3(bucket_name, s3_object, s3_object_body):
    s3_resource = boto3.resource("s3")
    s3_object_body = hashlib.sha256(s3_object_body.encode('utf-8')).hexdigest()

    upload_result = s3_resource.Object(bucket_name, s3_object).put(Body=s3_object_body)
    print(upload_result)
    assert upload_result["ResponseMetadata"]["HTTPStatusCode"] == 200

    text_file_from_s3 = (
        s3_resource.Object(bucket_name, s3_object).get()["Body"].read().decode("utf-8")
    )

    assert s3_object_body == text_file_from_s3
