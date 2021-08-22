from conn import s3_client

def listBuckets():

    response = s3_client.list_buckets()

    if response['Buckets'] == []:
        print("You do not have any bucket!\nYou might wanna create one.")
        
    else:
        for item in response['Buckets']:
            print(item['CreationDate'], item['Name'])


if __name__ == '__main__':
    listBuckets()