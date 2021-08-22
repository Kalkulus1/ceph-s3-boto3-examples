from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def listObjects():

    parser = ArgumentParser(description='Bucket name')
    parser.add_argument(
                        '--bucket-name',
                        dest='bucket_name',
                        action='store',
                        required=True,
                        help='the name of the bucket'
                        )

    args = parser.parse_args()

    objects = s3_client.list_objects_v2(Bucket=args.bucket_name)

    try:
        s3_client.head_bucket(Bucket=args.bucket_name)
        
        for item in objects['Contents']:
            print(item['Key'])

        print(f"Object {args.key_name} uploaded successfully for {args.data}!")

    except ClientError:
        print(f"Bucket {bucket.name} does not exist!")
        


if __name__ == '__main__':
    listObjects()

