import boto3

AWS_REGION = "us-east-1"
session = boto3.Session(
    aws_access_key_id="ASIARKMKKCQ3GU3PIQFS",
    aws_secret_access_key="4zjyrOTVLn6GPEnX6CFIT10WWbYObgvGa3gfP/YJ",
    aws_session_token="FwoGZXIvYXdzEGQaDA1Ofi4/zwCODr/zzSLIAtYEQhi8SaTeXlW2eDTsn8eOSsndQaGOjXrYm3BFH+Cz/7cPbOYSx"
                      "/4yxvTE4IgE7KZbx4kiE9TBpqqXUKNdYyNclmqSL0TtkGa2WykLOY6QaoaFUqujiti2QbqfOguY9lLUFlVRO8WOyUag5Yh"
                      "/2N2QEqDngDnjQCtnewepzXDEFiX7CM7vAqs0RrxGmb6t0a8AmlVNSIorLRVmzmLLaxwmDCMInlAD3bw0wRTYOlaVUihadnbUt7HgrTh+zcdRyXZZDJRyjWoPs3X0PahCOKOd3G253eCGJSKnf84UKFeJqNntSEuUhNuuzciobWh54JqY1/+oU+THOfke73WDRhXuSliIDQihSFMycstFpUwEGlu8tdMb6jiGRKDxcD33grm9OST/6j+Ph9y/b8eXJtXKvngfPBvxoeGSfjwmvV9lITZxYd3lv2corsq+vgYyL00+KXVRRstnjQdiw1j8WauWX3PEPIb/qFgfqMa6RG5XAnqr9r7oaNTPZCS/oywz",
    region_name=AWS_REGION,
)
s3_client = session.client("s3")

# File to upload/download
LOCAL_FILE = "example.txt"
S3_OBJECT_NAME = "uploaded_example.txt"

BUCKET_NAME = "test-bucket-1234"

# 2️. Upload a File to S3


def upload_file():
    try:
        s3_client.upload_file(LOCAL_FILE, BUCKET_NAME, S3_OBJECT_NAME)
        print(f"File '{LOCAL_FILE}' uploaded as '{S3_OBJECT_NAME}'!")
    except Exception as e:
        print(f"Error uploading file: {e}")

#
# # -------------------------------
# # 3️⃣ Download a File from S3
# # -------------------------------
#
#
# def download_file():
#     try:
#         s3_client.download_file(BUCKET_NAME, S3_OBJECT_NAME, f"downloaded_{LOCAL_FILE}")
#         print(f"File '{S3_OBJECT_NAME}' downloaded successfully!")
#     except Exception as e:
#         print(f"Error downloading file: {e}")
#
#
# # -------------------------------
# # 4️⃣ List Objects in Bucket
# # -------------------------------
#
#
# def list_objects():
#     try:
#         response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
#         if "Contents" in response:
#             print("Objects in S3 Bucket:")
#             for obj in response["Contents"]:
#                 print(f" - {obj['Key']}")
#         else:
#             print("No objects found.")
#     except Exception as e:
#         print(f"Error listing objects: {e}")
#
#
# # -------------------------------
# # 5️⃣ Delete an Object from S3
# # -------------------------------
#
#
# def delete_object():
#     try:
#         s3_client.delete_object(Bucket=BUCKET_NAME, Key=S3_OBJECT_NAME)
#         print(f"File '{S3_OBJECT_NAME}' deleted from bucket!")
#     except Exception as e:
#         print(f"Error deleting object: {e}")
#
#
# # -------------------------------
# # 6️⃣ Enable Versioning
# # -------------------------------
#
#
# def enable_versioning():
#     try:
#         s3_client.put_bucket_versioning(
#             Bucket=BUCKET_NAME,
#             VersioningConfiguration={"Status": "Enabled"},
#         )
#         print(f"Versioning enabled for '{BUCKET_NAME}'!")
#     except Exception as e:
#         print(f"Error enabling versioning: {e}")
#
#
# # -------------------------------
# # 7️⃣ Enable Server-Side Encryption
# # -------------------------------
#
#
# def enable_encryption():
#     try:
#         s3_client.put_bucket_encryption(
#             Bucket=BUCKET_NAME,
#             ServerSideEncryptionConfiguration={
#                 "Rules": [
#                     {
#                         "ApplyServerSideEncryptionByDefault": {
#                             "SSEAlgorithm": "AES256"
#                         }
#                     }
#                 ]
#             },
#         )
#         print(f"Encryption enabled for '{BUCKET_NAME}'!")
#     except Exception as e:
#         print(f"Error enabling encryption: {e}")


if __name__ == "__main__":
    upload_file()
    # list_objects()
    # download_file()
    # delete_object()
    # enable_versioning()
    # enable_encryption()
