# Google Cloud Platform (GCP)
Functions and Information related to Google Cloud Services

### Google CLI authentication
* In order to authenticate gcloud cli in the remote machine, you have to have the [google cloud project](https://developers.google.com/workspace/marketplace/create-gcp-project) setup on the GCP platform.
* Make sure to install [gcloud sdk](https://cloud.google.com/sdk/docs/install) in bot the local and remote machine
* Run `gcloud auth login --no-browser` on the remote machine terminal, and copy the `gcloud auth login --remote-bootstrap=......` link in the local machine with web browser, after choosing an account, copy the link `https://localhost:......` on to the remote machine to complete the authentication process.
* After authentication you can see the active accounts using the command `gcloud auth list`, in which there is a `*` on the active account. Along with this you can see projects using `gcloud projects list`, and set a default project using `gcloud config set project 'PROJECT_ID'`
* To set GCP SSH in config, you need to have [Google SDK](https://cloud.google.com/sdk/docs/install) installed in your system first, after installing open Google SDK console and follow the instructions, then set Google VM SSH in `config` by running `gcloud compute config-ssh`.
* Run `ssh-keygen -t rsa -f C:\Users\WINDOWS_USER\.ssh\KEY_FILENAME -C USERNAME -b 2048` to generate public and private keys, replace `USERNAME` and `KEY_FILENAME` with your username and `google_compute_engine` respectively.

### TODO
* `gcloud` authentication of `github` - [link](https://github.com/marketplace/actions/authenticate-to-google-cloud#examples)

### GCP storage
* Articles that help for large data download from cloud - [link](https://towardsdatascience.com/streaming-big-data-files-from-cloud-storage-634e54818e75)

### GitHub Action Workflow
* Github actions google cloud auth - [link](https://github.com/google-github-actions/auth)