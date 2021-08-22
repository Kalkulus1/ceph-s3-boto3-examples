from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def downloadFile():

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
    parser.add_argument('--file-name',
                        dest='file_name',
                        action='store',
                        required=True,
                        help='the file to download')

    args = parser.parse_args()

    bucket = s3_resource.Bucket((args.bucket_name).lower())

    try:
        s3_client.head_bucket(Bucket=bucket.name)
        
        bucket.download_file(Filename=args.file_name, Key=args.key_name)

        print(f"File {args.key_name} downloaded successfully!")

    except ClientError:
        print(f"Bucket {bucket.name} does not exist!")
        

if __name__ == '__main__':
    downloadFile()

