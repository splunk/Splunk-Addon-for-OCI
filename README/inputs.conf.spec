[oci_logging://<name>]
stream_id =
stream_endpoint =
oci_region = ex: us-phoenix-1
message_limit =
partition = Number of Worker Threads
user_ocid =
tenancy_ocid =
private_key =
private_key_password =
fingerprint =
proxy=
use_instance_principal =
private_key_location =
retry_interval =

# Also declared bare (no "://<name>") to match the scheme-wide default
# values set in default/inputs.conf's [oci_logging] stanza -- without this,
# Splunk's config validator only matches instantiated [oci_logging://<name>]
# stanzas against the block above and logs "Invalid key in stanza
# [oci_logging]" warnings at startup for the bare defaults stanza.
[oci_logging]
stream_id =
stream_endpoint =
oci_region = ex: us-phoenix-1
message_limit =
partition = Number of Worker Threads
user_ocid =
tenancy_ocid =
private_key =
private_key_password =
fingerprint =
proxy=
use_instance_principal =
private_key_location =
retry_interval =