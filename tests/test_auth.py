from src import gcloud_auth
import logging
from logging import config
config.fileConfig('logger.ini')

def test_authentication():
    """Testing authentication"""
    gcloud = gcloud_auth(log = logging)
    gcloud.authenticate()
    assert len(gcloud.bucket_names) !=0