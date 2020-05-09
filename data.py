from google.cloud import storage


storage_client = storage.Client()

# The name for the new bucket
bucket_name = "bucket-coololow"

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print("Bucket {} created.".format(bucket.name))
