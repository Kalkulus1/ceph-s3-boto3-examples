from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def copyObject():

    parser = ArgumentParser(description='Copy object from one bucket to another')
    parser.add_argument(
                        '--source',
                        dest='bucket_source',
                        action='store',
                        required=True,
                        help='the name of the bucket source'
                        )
    parser.add_argument('--source-key',
                        dest='source_key',
                        action='store',
                        required=True,
                        help='the object name from source bucket'
                        )
    parser.add_argument('--destination',
                        dest='bucket_destination',
                        action='store',
                        required=True,
                        help='the name of the destination bucket')
    parser.add_argument('--destination-key',
                        dest='destination_key',
                        action='store',
                        required=False,
                        help='the object name to store in the destination bucket (optional)'
                        )

    args = parser.parse_args()

    source = {
                'Bucket': (args.bucket_source).lower(),
                'Key': args.source_key
            }

    bucket = s3_resource.Bucket((args.bucket_destination).lower())

    try:
        s3_client.head_bucket(Bucket=bucket.name)
        s3_client.head_bucket(Bucket=(args.bucket_destination).lower())

        if args.destination_key != '': 
            bucket.copy(source, args.destination_key)
        else:
            bucket.copy(source, args.source_key)

        print(f"Object {args.source_key} copied from {args.bucket_source} to {args.bucket_destination} successfully!")

    except ClientError:
        print(f"A bucket or all buckets do not exist!")
        

if __name__ == '__main__':
    copyObject()

