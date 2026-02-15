# Python IP Allowlist Automation

## Scenario
I am a security professional working at a healthcare company. As part of my job, I am required to regularly update a file that identifies the employees who can access restricted content. The contents of the file are based on who is working with personal patient records. Employees are restricted access based on their IP address.

## Project Description
Creating an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. If so, remove those IP addresses from the file containing the allow list.

## Tools Used
- Python 3
- File I/O operations
- String and list manipulation

## Steps

### 1. Open the file

To open the allow list, I assigned it to a variable called `import_file` and used the `with` statement with the `open()` function:

```python
import_file = "allow_list.txt"
with open(import_file, "r") as file:
```

Key concepts:
- **with** keyword - Automatically manages resources and ensures the file is closed, even if an error occurs
- **open()** function - Opens a file in Python
- First parameter: identifies the file to open
- Second parameter: indicates the operation mode
- **'r'** - read the file
- **'w'** - write to the file
- **'a'** - append to the file
- **as file** - Assigns a variable that references the file object for use in the code block

### 2. Read file contents

To read the imported file, I used the `.read()` method and stored the contents in a variable named `ip_addresses`:

```python
ip_addresses = file.read()
print(ip_addresses)
```

Key concepts:
- **.read()** method - Converts the contents of the file into a string format
- Storing in ip_addresses variable allows us to work with the file data
- **print()** displays the file contents to verify successful reading

### 3. Convert string to list

To convert the string into a list, I used the `.split()` method:

```python
ip_addresses = ip_addresses.split()
```

Key concepts:
- **.split()** method - Converts a string into a list by splitting it at whitespace (spaces, newlines)
- This transformation is necessary to iterate through individual IP addresses
- Each IP address becomes a separate element in the list for easier manipulation

### 4. Iterate through the remove list

First, I created a `remove_list` variable containing IP addresses that should no longer have access. Then I used a `for` loop to iterate through each element:

```python
for element in remove_list:
    print(element)
```

Key concepts:
- **for loop** - Iterates through each element in the remove_list
- **element** - Loop variable that represents each IP address during iteration
- This displays all restricted IP addresses that need to be removed from the allow list

### 5. Remove IP addresses that are in the remove list

I used a list comprehension to create a new list containing only allowed IP addresses:

```python
ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]
```

- Safer than modifying during iteration - instead of using .remove() inside a for loop, which can skip elements when modifying a list while iterating
- List comprehension - Creates a new list containing only IPs that are NOT in the remove_list
- More reliable - Critical for healthcare security where missing a restricted IP could be a compliance violation
- More Pythonic - Cleaner, more efficient single-pass solution

Key concepts:
- List comprehension syntax: [expression for item in list if condition]
- if ip not in remove_list - Keeps only IPs that don't exist in the restricted list
- Result: A clean allowlist with all restricted IPs removed, with no risk of iteration bugs

### 6. Update the file with revised list

To update the file, I converted the list back to string format using `.join()` and wrote it back to the file:

```python
ip_addresses = "\n".join(ip_addresses)
with open(import_file, "w") as file:
    file.write(ip_addresses)
```

Key concepts:
- **.join() method** - Concatenates every element of the list into a single string (opposite of .split())
- **"\n"** - Joins elements with newline characters to maintain readable format
- **"w"** parameter - Opens the file in write mode to overwrite existing contents
- **.write() method** - Writes the string data to the specified file
  
The file now contains only the updated allow list with restricted IPs removed

Verification:
```python
with open(import_file, "r") as file:
    text = file.read()
print(text)
```

The output displays the updated file contents, confirming successful removal of restricted IP addresses.

## Summary

I successfully automated the IP allowlist management process using Python file handling and data manipulation techniques:

- Used `with` statement and `open()` function to safely read from and write to files
- Applied `.split()` method to convert the file contents from string to list format for easier manipulation
- Implemented a **list comprehension** to filter out restricted IP addresses, avoiding potential bugs from modifying lists during iteration
- This approach is more reliable for healthcare security compliance where missing a restricted IP could be a serious violation
- Applied `.join()` method to convert the filtered list back to string format for file writing
- Verified the updated file contents to ensure restricted IPs were successfully removed

This automation reduces manual errors, ensures only authorized personnel can access restricted patient records, and uses best practices for Python list manipulation in security-critical applications.
