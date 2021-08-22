from conn import s3_resource, s3_client, sys, os, ClientError, ArgumentParser

def createFolder():

    parser = ArgumentParser(description='Create a folder')
    parser.add_argument('--bucket-name',
                        dest='bucket_name',
                        action='store',
                        required=True,
                        help='the name of the bucket')
    parser.add_argument('--folder-name',
                        dest='folder_name',
                        action='store',
                        required=True,
                        help='the folder name')

    args = parser.parse_args()

    bucket = s3_resource.Bucket((args.bucket_name).lower())

    try:
        s3_client.head_bucket(Bucket=bucket.name)

        bucket.put_object(Bucket=args.bucket_name,
                      Key=args.folder_name,
                      Body='')
        print(f"Folder {args.folder_name} was created in {bucket.name}")

    except ClientError:
        print(f"Bucket {bucket.name} does not exist!")
        


if __name__ == '__main__':
    createFolder()

