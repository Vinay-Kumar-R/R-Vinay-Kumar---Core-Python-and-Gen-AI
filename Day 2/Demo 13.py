hosts = [] # empty list
print(f"Number of elements in the list:{len(hosts)}") # display number of elements in the list

c = 0
while c < 5:
    h = input("Enter a hostname:")
    hosts.append(h) # append the hostname to the list
    c = c + 1

print(f"\nNumber of elements in the list:{len(hosts)}") # display number of elements in the list

for var in hosts:
    print(var) # iterate through the list and display each hostname
    

host_name  = input("Enter a hostname:")
if host_name in hosts:
    hosts[-1] = host_name 
else:
    hosts.append(host_name) # add the hostname to the list

print("\n") # empty line
for var in hosts:
    print(var) # display the list of hostnames
    
