#!/usr/bin/env python

import sys
import click
import paws
from paws import s3

@click.version_option(paws.__version__)
@click.group()

def cli():
	"""PAWS Tool"""

@cli.command("download")
@click.option("--bucket", required=True, help="Name of s3 bucket")
@click.option("--key", required=True, help="Name of s3 Key")
@click.option("--filename", required=True, help="Name of file to save as")

def download(bucket, key, filename):
	"""Downloads an S3 file

	./pcli.py --bucket gedlt-open-data --key events/1979.csv --filename 1979.csv
	"""

	click.echo(
		"Downloading s3 file with bucket: {}, key {}, filename {}".format(bucket, key, filename)
	)

	res = s3.download(bucket, key, filename)
	click.echo(res)

if __name__ == "__main__":
	cli()