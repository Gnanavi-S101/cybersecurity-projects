# SQL Security Investigation

## Scenario
As a security analyst, I was tasked with investigating potential security threats by examining the organization's database. The database contains employee information and login attempt records that need to be analyzed to identify suspicious activity.

## Project Description
Examined the organization's database containing `employees` and `log_in_attempts` tables. Used SQL filters (AND, OR, NOT, LIKE) to retrieve records from different datasets and investigate potential security threats including failed login attempts, suspicious login patterns, and unauthorized access attempts.

## Database Structure

**log_in_attempts table:**
- event_id
- username
- login_date
- login_time
- country
- ip_address
- success (Boolean: 0 = failed, 1 = successful)

**employees table:**
- employee_id
- device_id
- username
- department
- office

## Tools Used
- SQL
- Database querying
- Logical operators (AND, OR, NOT, LIKE)

## Investigation Steps

### 1. Retrieve after-hours failed login attempts

**Objective:** Identify all unsuccessful login attempts that occurred after business hours (after 18:00/6:00 PM).

```sql
SELECT * 
FROM log_in_attempts 
WHERE login_time > '18:00' AND success = 0;
```

**Analysis:**
- login_time > '18:00' - Filters for attempts after 6 PM
- success = 0 - Filters for failed attempts (0 = false/failed)
- AND operator - Ensures both conditions must be met simultaneously
- Security significance: After-hours failed login attempts may indicate unauthorized access attempts when fewer staff are present to notice suspicious activity.

### 2. Retrieve login attempts on specific dates

**Objective:** Investigate a suspicious event that occurred on 2022-05-09 by retrieving all login attempts from that day and the day before.

```sql
SELECT * 
FROM log_in_attempts 
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
```

**Analysis:**
- OR operator - Returns results where either condition is met
- Captures login activity across both dates for pattern analysis
- Security significance: Examining login patterns around suspicious events helps identify related incidents and potential attack timelines.
  
### 3. Retrieve login attempts outside of Mexico

**Objective:** Identify login attempts that did not originate from Mexico to investigate potential unauthorized access from unexpected locations.

```sql
SELECT * 
FROM log_in_attempts 
WHERE NOT country LIKE 'Mex%';
```

**Analysis:**
- NOT operator - Negates the condition, returning all records that don't match
- LIKE 'Mex%' - Pattern matching for country names starting with "Mex" (accounts for variations like "Mexico" and "Mexican")
- % wildcard - Matches any characters after "Mex"
- Security significance: Geographic anomalies in login attempts can indicate compromised credentials or unauthorized access.
  
### 4. Retrieve employees in Marketing department (East building)

**Objective**: Obtain information about employees in the Marketing department located in East building offices for a targeted security update.

```sql
SELECT * 
FROM employees 
WHERE department = 'Marketing' AND office LIKE 'East%';
```
**Analysis:**
- AND operator - Both conditions must be true
- LIKE 'East%' - Matches all East building offices (East-170, East-320, etc.)
- Security significance: Enables targeted security communications and access reviews for specific department locations.

### 5. Retrieve employees in Finance or Sales department

**Objective**: Retrieve records for employees in Finance or Sales departments for a security policy update.

```sql
SELECT * 
FROM employees 
WHERE department = 'Finance' OR department = 'Sales';
```

**Analysis:**
- OR operator - Returns employees from either department
- Security significance: Allows security team to apply department-specific security measures to sensitive business units.

### 6. Retrieve all employees not in IT department

**Objective:** Retrieve records for all employees outside the Information Technology department.

```sql
SELECT * 
FROM employees 
WHERE NOT department = 'Information Technology';
```

**Analysis:**
- NOT operator - Excludes IT department employees
- Useful for identifying users who require additional security training
- Security significance: Non-IT staff may require different security protocols and awareness training.

### Summary
I successfully investigated potential security threats by:
- Analyzing failed login attempts after business hours to identify suspicious access patterns
- Investigating login activity around specific dates related to security incidents
- Identifying geographic anomalies in login attempts through location-based filtering
- Using SQL logical operators (AND, OR, NOT) to create complex queries for targeted investigations
- Applying pattern matching with LIKE operator for flexible filtering
- Retrieving employee data for targeted security measures and communications
These SQL queries enabled efficient identification of security risks, suspicious login patterns, and support for implementing role-based and location-based security controls.
