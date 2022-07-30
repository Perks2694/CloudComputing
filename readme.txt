In order to run the program you must 
1. Connect to the two virtual machines
2. Both VMs have a specified Kafka user to run the kafka broekrs
3. On VM 2 run Zookeeper and Kafka
4. On VM 3 run Kafka and the Consumer code.
5. On Another Machine, (My VM 1) run the producer code to send to the broker on VM 2
6. The consumer on VM 3 will receive the data and send it to the couch db
7. The couch db can be access by  using an HTTP post

Effort Expanded - 

This assignment challenged me immensely. There were many roadblocks for me, mostly relating to the networking aspect of the assignment and various firewall settings that I later realized were not relevant.

I first tried to run Zookeeper on VM1 on my local VM, I spend many hours trying to figure out why this did not work, only to realize it was not possible with my ISP and router configurations.

I attempted to change my personal firewall settings, I setup port forwarding on my router, VM and on my windows OS. I also learned that my router does not allow my public IP to be pinged regardless of any settings that I put in. The manufacturer has disabled it and does not allow it to be configured.

I had some issues with the Kafka configurations in server.properties but those mostly stemmed from me trying every configuration possible after none of the solutions worked due to the way I was attempting to connect to VM1, once I realized that I did not actually need Zookeeper or Kafka to be running on the local VM 1 the assignment was actually not all that difficult.

I had minor issues with the CouchDB database, this was mostly do to unfamiliarity with the service, and was resolved by reviewing the COuchdb documentation.

Overall I spent over 60 hours on this assignment, mostly due to my own frustrations.