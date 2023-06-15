from src import gcloud_auth
import logging
from logging import config
config.fileConfig('logger.ini')

def test_authentication():
    """Testing authentication"""
    project_id = "otd-ml"
    gcloud = gcloud_auth(log = logging)
    gcloud.authenticate(project_id = project_id)
    assert len(gcloud.bucket_names) !=0