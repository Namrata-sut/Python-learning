import boto3

AWS_REGION = "us-east-1"
BUCKET_NAME = "test-bucket-1234"
session = boto3.Session(
    aws_access_key_id="ASIARKMKKCQ3GU3PIQFS",
    aws_secret_access_key="4zjyrOTVLn6GPEnX6CFIT10WWbYObgvGa3gfP/YJ",
    aws_session_token="FwoGZXIvYXdzEGQaDA1Ofi4/zwCODr/zzSLIAtYEQhi8SaTeXlW2eDTsn8eOSsndQaGOjXrYm3BFH+Cz/7cPbOYSx"
                      "/4yxvTE4IgE7KZbx4kiE9TBpqqXUKNdYyNclmqSL0TtkGa2WykLOY6QaoaFUqujiti2QbqfOguY9lLUFlVRO8WOyUag5Yh"
                      "/2N2QEqDngDnjQCtnewepzXDEFiX7CM7vAqs0RrxGmb6t0a8AmlVNSIorLRVmzmLLaxwmDCMInlAD3bw0wRTYOlaVUihadnbUt7HgrTh+zcdRyXZZDJRyjWoPs3X0PahCOKOd3G253eCGJSKnf84UKFeJqNntSEuUhNuuzciobWh54JqY1/+oU+THOfke73WDRhXuSliIDQihSFMycstFpUwEGlu8tdMb6jiGRKDxcD33grm9OST/6j+Ph9y/b8eXJtXKvngfPBvxoeGSfjwmvV9lITZxYd3lv2corsq+vgYyL00+KXVRRstnjQdiw1j8WauWX3PEPIb/qFgfqMa6RG5XAnqr9r7oaNTPZCS/oywz",
    region_name="us-east-1",
)
s3_client = session.client("s3")


def create_bucket():
    try:
        # breakpoint()
        response = s3_client.create_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket '{BUCKET_NAME}' created successfully!")
        print(response)

    except Exception as e:
        print(f"Error creating bucket: {e}")


create_bucket()

# print(session.region_name)
