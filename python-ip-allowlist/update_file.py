# Assign import_file to the name of the file
import_file = "allow_list.txt"

# Assign remove_list to a list of IP addresses that are no longer allowed access
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Read the initial contents of the file
with open(import_file, "r") as file:
    # Use .read() to read the imported file and store it in ip_addresses
    ip_addresses = file.read()

# Use .split() to convert ip_addresses from a string to a list
ip_addresses = ip_addresses.split()

# Use list comprehension to remove restricted IPs (safer than .remove() in loop)
ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]

# Convert ip_addresses back to a string so it can be written to the file
ip_addresses = "\n".join(ip_addresses)

# Rewrite the original file with updated allowlist
with open(import_file, "w") as file:
    file.write(ip_addresses)

# Read and display the updated file to verify
with open(import_file, "r") as file:
    text = file.read()

print("Updated allow list:")
print(text)
