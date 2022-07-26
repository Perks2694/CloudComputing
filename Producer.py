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
#    In this example, we use the "top" command and use it as producer of events for
#    Kafka. The consumer can be another Python program that reads and dumps the
#    information into a database OR just keeps displaying the incoming events on the
#    command line consumer (or consumers)
#
from faker import Faker
import os   # need this for popen
import time # for sleep
import json
from kafka import KafkaProducer  # producer of events


fake = Faker();

def get_fake_neighbor():
    return {
        "Owner": fake.name(),
        "address": fake.address(),
        "Built in": fake.year()

    }


    if __name__ == "__main__":
        print(get_fake_neighbor())


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs




# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)
producer = KafkaProducer (bootstrap_servers="10.0.2.15:9092", value_serializer=json_serializer,
                                          acks=1)  # wait for leader to write to log

# say we send the contents 100 times after a sleep of 1 sec in between
for i in range (100):
    
    # get the output of the top command
    process = get_fake_neighbor()
    

    # send the contents under topic utilizations. Note that it expects
    # the contents in bytes so we convert it to bytes.
    #
    # Note that here I am not serializing the contents into JSON or anything
    # as such but just taking the output as received and sending it as bytes
    # You will need to modify it to send a JSON structure, say something
    # like <timestamp, contents of top>
    #
    producer.send ("Neighbors", process)
    producer.flush ()   # try to empty the sending buffer

    # sleep a second
    time.sleep (1)

# we are done
producer.close ()
    