#! /usr/bin/env python3

import os
import sys
import json
import boto3
from botocore.client import ClientError
from argparse import ArgumentParser

with open('cred.json', 'r') as fd:
    cred = json.loads(fd.read())

s3_client = boto3.client('s3',
                    endpoint_url=cred['endpoint_url'],
                    aws_access_key_id=cred['access_key'],
                    aws_secret_access_key=cred['secret_key'])


s3_resource = boto3.resource('s3',
                    endpoint_url=cred['endpoint_url'],
                    aws_access_key_id=cred['access_key'],
                    aws_secret_access_key=cred['secret_key'])

# print(s3)