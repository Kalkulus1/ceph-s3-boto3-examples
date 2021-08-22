from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def createBucket():

    parser = ArgumentParser(description='Create A Bucket')
    parser.add_argument('--bucket-name',
                        dest='bucket_name',
                        action='store',
                        required=True,
                        help='the name of the bucket to create')
    args = parser.parse_args()

    bucket = s3_resource.Bucket((args.bucket_name).lower())

    try:
        s3_client.head_bucket(Bucket=bucket.name)
        print(f"Bucket {bucket.name} already exists!")

    except ClientError:
        bucket.create()
        print(f"Your bucket {bucket.name} was created on {bucket.creation_date}")
            
        
    
        


if __name__ == '__main__':
    createBucket()

