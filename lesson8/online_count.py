# Task 2: Online Count
# Author: Ahmet
# Description: Counts how many people are online in a dictionary of names and statuses.
def online_count(statuses):
    count = 0
    for status in statuses.values():
        if status == "online":
            count += 1
    return count
# Example dictionary to test the function
statuses = {
    "Alicia": "online",
    "Niani": "offline",
    "Shavar": "online"
}
# Run and print the result
print(online_count(statuses))