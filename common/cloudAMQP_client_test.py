from cloudAMQP_client import CloudAMQPClient

# REPLACE URL WITH YOUR OWN
CLOUDAMQP_URL = 'amqp://cphghnay:jUof0j2MyrgneQ1kIShfLy-xszL-4Aah@zebra.rmq.cloudamqp.com/cphghnay'
QUEUE_NAME = 'dataFetcherTaskQueue'

# Initialize a client
client = CloudAMQPClient(CLOUDAMQP_URL, QUEUE_NAME)

# Send a message
client.sendDataFetcherTask({'zpid' : '83154148'})


# Receive a message
#client.getDataFetcherTask()
