#We've detected a computer on our network which we beleive to be taken over by an attacker
# We have reason to beleive that the computer with the highest amout of UNIQUE connections
#is the one that is compromised
#Provided with a text file "Hosts_log.txt" which lists connections made on the network
# in the form of: source,destination find which source had the most unique connections 
max_key = 0 
max_index = 0

def findHosts(host_line,host_counter,max_key):
	source = host_line.split(",")[0]
	destination = host_line.split(",")[1]

	if source in host_counter:
		host_counter[source].add(destination)

	else:
		host_counter[source] = set()
		host_counter[source].add(destination)
	if len(host_counter[source]) > max_key:
		max_key = len(host_counter[source])
		max_index = source
	return max_key



def parser(log_file):
	host_file = open(log_file,"r")
	host_counter = {}
	
	for line in host_file.readlines(): #readlines splits at newline char
		num_connections = findHosts(line,host_counter,max_key)
	return num_connections
print(parser("Hosts_log.txt"))

