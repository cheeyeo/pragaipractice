"""
S3 methods for PAWS library
"""

import boto3
from sensible.loginit import logger

log = logger("Paws")

def boto_s3_resource():
	"""Create boto s3 resource"""
	return boto3.resource("s3")

def download(bucket, key, filename, resource=None):
	"""Downloads file from S3"""
	if resource is None:
		resource = boto_s3_resource()

	log_msg = "Attempting to download {}, {}, {}".format(bucket, key, filename)

	log.info(log_msg)

	resource.meta.client.download_file(bucket, key, filename)

	return filename

