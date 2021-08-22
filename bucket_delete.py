from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def deleteBucket():

    parser = ArgumentParser(description='Delete a bucket')
    parser.add_argument(
        '--bucket-name',
        dest='bucket_name',
        action='store',
        required=True,
        help='the name of the bucket'
        )
    args = parser.parse_args()

    bucket = s3_resource.Bucket((args.bucket_name).lower())

    try:
        s3_client.head_bucket(Bucket=bucket.name)
        bucket.delete()

        print(f"Bucket {bucket.name} deleted successfully!")

    except ClientError:
        print(f"Bucket {bucket.name} does not exist!")
        


if __name__ == '__main__':
    deleteBucket()

