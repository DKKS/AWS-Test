# AWS-Test
## Instructions to execute this script

Command to execute:

1. ansible-playbook -i ./hosts Ec2-Instance-2.yml

 

On the EC2 instance:

2. ssh -i <key.pem> ubuntu@<ipaddress>

3. sudo su -

4. ls

5. cat mostComonWords.txt #most occurrences of the words

6. tail -f docker-stats..log #docker status every 10 seconds
