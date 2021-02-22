from basic_defs import cloud_storage, NAS

import os
import sys

class AWS_S3(cloud_storage):
    def __init__(self):
        # TODO: Fill in the AWS access key ID
        self.access_key_id = ""
        # TODO: Fill in the AWS access secret key
        self.access_secret_key = ""
        # TODO: Fill in the bucket name
        self.bucket_name = ""

    # Implement the abstract functions from cloud_storage

class Azure_Blob_Storage(cloud_storage):
    def __init__(self):
        # TODO: Fill in the Azure key
        self.key = ""
        # TODO: Fill in the Azure connection string
        self.conn_str = ""
        # TODO: Fill in the account name
        self.account_name = "csce678s21"
        # TODO: Fill in the container name
        self.container_name = ""

    # Implement the abstract functions from cloud_storage

class Google_Cloud_Storage(cloud_storage):
    def __init__(self):
        # TODO: Download and place the Credential JSON file
        self.credential_file = "gcp-credential.json"
        # TODO: Fill in the container name
        self.bucket_name = ""

    # Implement the abstract functions from cloud_storage

class RAID_on_Cloud(NAS):
    def __init__(self):
        self.backends = [
                AWS_S3(),
                Azure_Blob_Storage(),
                Google_Cloud_Storage()
            ]

    # Implement the abstract functions from NAS

