from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def deleteObject():

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

    args = parser.parse_args()

    try:
        s3_client.head_bucket(Bucket=args.bucket_name)
        
        s3_client.delete_object(Bucket=args.bucket_name,
                      Key=args.key_name)

        print(f"Object {args.key_name} deleted successfully!")

    except ClientError:
        print(f"Bucket {bucket.name} does not exist!")
        

if __name__ == '__main__':
    deleteObject()

