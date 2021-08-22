from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def putObject():

    parser = ArgumentParser(description='Bucket name')
    parser.add_argument(
                        '--bucket-name',
                        dest='bucket_name',
                        action='store',
                        required=True,
                        help='the name of the bucket'
                        )
    parser.add_argument('--key-name',
                        dest='key_name',
                        action='store',
                        required=True,
                        help='the object name'
                        )
    parser.add_argument('--data',
                        dest='data',
                        action='store',
                        required=True,
                        help='the object data')

    args = parser.parse_args()

    bucket = s3_resource.Bucket((args.bucket_name).lower())

    try:
        s3_client.head_bucket(Bucket=bucket.name)
        
        bucket.put_object(Bucket=args.bucket_name,
                      Key=args.key_name,
                      Body=args.data)

        print(f"Object {args.key_name} uploaded successfully for {args.data}!")

    except ClientError:
        print(f"Bucket {bucket.name} does not exist!")
        

if __name__ == '__main__':
    putObject()

