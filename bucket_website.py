from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def websiteBucket():

    parser = ArgumentParser(description='Delete a bucket')
    parser.add_argument(
        '--bucket-name',
        dest='bucket_name',
        action='store',
        required=True,
        help='the name of the bucket'
        )
    args = parser.parse_args()

    try:
        s3_client.head_bucket(Bucket=args.bucket_name)
        bucket_website = s3.BucketWebsite((args.bucket_name).lower())

        print(f"Bucket {args.bucket_name} website created successfully!\nUrl is: {bucket_website}")

    except ClientError:
        print(f"Bucket {args.bucket_name} does not exist!")
        


if __name__ == '__main__':
    websiteBucket()

