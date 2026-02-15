# Linux File and Directory Permission Hardening

## Scenario
The organization needed to restrict unauthorized file access to ensure system security and data integrity. As a security analyst, I was tasked with reviewing and hardening file and directory permissions on a Linux system.

## Project Description
Performed Linux file and directory permission analysis and hardening by inspecting standard and hidden files, interpreting permission strings, and modifying user, group, and other access using `chmod` to enforce least privilege principles and prevent unauthorized modification or execution.

## Tools Used
- Linux command line
- `ls`, `cd`, `pwd` commands
- `chmod` for permission modification
- Bash shell

## Steps

### 1. Check file and directory details

I used several commands to inspect the current directory structure and file permissions:

```bash
pwd                    # Check current directory
cd projects           # Navigate to projects directory
ls -l                 # List files with permissions
ls -a                 # Show hidden files
ls -la                # Show all files (hidden and normal) with permissions
```

### 2. Understanding the permission string

Linux permissions follow the format: drwxrwxrwx

**Permission string breakdown:**
First character: File type
d = directory
-= regular file
- Characters 2-4: User (owner) permissions
- Characters 5-7: Group permissions
- Characters 8-10: Other (everyone else) permissions

**Permission types:**
r = read permission
w = write permission
x = execute permission
-= permission denied

**Example:** drwxr-xr--
d = directory
rwx = user has read, write, execute
r-x = group has read, execute (no write)
r-- = others have read only

### 3. Change file permissions

I identified that project_k.txt had overly permissive write access for groups and others, violating least privilege:

```bash
ls -l project_k.txt                    # Check current permissions
chmod g-w,o-w project_k.txt           # Remove write for group and others
```
Result: Only the file owner can modify the file, while group and others retain read access.

### 4. Change permissions on hidden files

Hidden files (starting with .) also required permission hardening:

```bash
ls -a                                  # Display hidden files
chmod g-w .project_x.txt              # Remove group write permission
```
Result: Prevents group members from modifying sensitive hidden configuration files.

### 5. Change directory permissions

The drafts subdirectory had unnecessary execute permissions that could allow unauthorized access:

```bash
ls -l                                  # Check directory permissions
chmod u-x,g-x drafts                  # Remove execute for user and group
```
Result: Restricts directory traversal, preventing users and groups from entering the directory while maintaining read permissions for listing contents.

### Summary

I successfully hardened file and directory permissions on a Linux system by:

- Using ls commands to audit current permission configurations
- Interpreting Linux permission strings to identify security risks
- Applying chmod to remove excessive permissions from files and directories
- Enforcing least privilege by restricting write and execute permissions where unnecessary
- Securing both standard and hidden files to prevent unauthorized modification
This implementation reduces the attack surface by ensuring users, groups, and others have only the minimum permissions required for their roles, preventing unauthorized file modification and execution.
