#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os   # need this for popen
import time # for sleep
from kafka import KafkaConsumer  # consumer of events
import json
import couchdb

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
consumer = KafkaConsumer (
    "Neighbors",
    bootstrap_servers="129.114.26.25:9092"
)
#couch = couchdb.Server('http://127.0.0.1:5984/')

#couch.resource.credentials = ("cperkinsyan","couchdbpassword");

#db = couch['neighbors']

#db=couch.create('neighbors')

print(" starting the consumer")




# we keep reading and printing
for msg in consumer:
    # what we get is a record. From this record, we are interested in printing
    # the contents of the value field. We are sure that we get only the
    # utilizations topic because that is the only topic we subscribed to.
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    #
    # convert the value field into string (ASCII)
    #
    entry = json.loads(msg.value)
    #db.save(entry)

    
    # Note that I am not showing code to obtain the incoming data as JSON
    # nor am I showing any code to connect to a backend database sink to
    # dump the incoming data. You will have to do that for the assignment.
    print ("{} lives in the neighborhood".format(json.loads(msg.value)))

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close ()
    