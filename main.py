from google.cloud import storage

import google.auth

scopes = ['https://www.googleapis.com/auth/cloud-platform']
credentials, project = google.auth.default(scopes=scopes)

# Automatically initializes credentials using credentials.json config file.
client = storage.Client(project=project, credentials=credentials)
# Lookup bucket information.
bucket = client.get_bucket('anna-terraform-states')
print("Bucket {} retrieved.".format(bucket.name))
