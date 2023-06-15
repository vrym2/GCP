from google.cloud import storage
from google.api_core.exceptions import BadRequest

class gcloud_auth:
    """Functions related to authentication"""
    def __init__(self, log: isinstance = None) -> None:
        """Initiating the variables

        Args:
            log: Custom logger file
        """
        self.log = log

    def authenticate(self, project_id:str = None):
        """Authenticate Google Cloud

        Args:
            project_id: Project ID
        """
        try:
            self.storage_client = storage.Client(project = project_id)
            self.buckets = self.storage_client.list_buckets()
            self.bucket_names = [bucket.name for bucket in self.buckets]
            return self.bucket_names
        except BadRequest as b:
            self.log.debug("There was a problem with authentication")
            self.log.debug(f"{b}")
        else:
            self.log.info("Authentication successful")

