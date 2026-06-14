# SOC Log Analyzer v1
# This script reads a security log file, analyzes login events,
# detects suspicious IP addresses, calculates risk levels,
# and generates a SOC-style report.

# Log file that contains security events
log = "security_log.txt"

# Open and read the log file
with open(log, "r") as file:

    file_log = file.read()

# Split the full text into individual log lines
file_log = file_log.split("\n")

# Dictionary used to count failed login attempts by IP address
suspect_counter = {}

# Dictionary used to count each type of security event
counters = {
    "LOGIN_FAILED": 0,
    "LOGIN_SUCCESS": 0,
    "ACCOUNT_LOCKED": 0,
    "PASSWORD_CHANGED": 0
}

# Analyze each log line
for i in file_log:
    # Split each line into fields: timestamp, level, IP, user, event
    partes = i.split(",")
    event = partes[4]

    # If the event is a failed login, count it and track the IP address
    if event == "LOGIN_FAILED":
        ip = partes[2]
        counters[event] += 1

        # Count how many failed attempts each suspicious IP has
        if ip not in suspect_counter:
            suspect_counter[ip] = 1
        else:
            suspect_counter[ip] += 1

    # Count all other known event types
    elif event in counters:
        counters[event] += 1

# Print summary in the terminal
print("Summary:")
for event, amount in counters.items():
    print(f"{event}: {amount}")

print("suspicious ips are:")
for ip, amount in suspect_counter.items():
    if amount > 20:
        risk = "HIGH RISK"
    elif amount >= 10:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"
    print(f"{ip} had {amount} failed attempts. Risk: {risk}")

# Calculate the total number of events analyzed
total_events = sum(counters.values())

# Separator used to make the report easier to read
separator = "\n\n" + "=" * 25 + "\n\n"

# Create a SOC report file
with open("soc_report.txt", "w") as file:

    file.write(f"SOC REPORT\nGenerated: 2026-06-14\nBy: Elieser{separator}SUMMARY\n\n")
    
    for event, amount in counters.items():
        file.write(f"{event}: {amount}\n")
    
    file.write(f"\nTotal events: {total_events}{separator}suspicious ips are:\n\n".upper())

    for ip, amount in suspect_counter.items():
        if amount > 20:
            risk = "HIGH RISK"
        elif amount >= 10:
            risk = "MEDIUM RISK"
        else:
            risk = "LOW RISK"
        if amount > 3:
            file.write(f"{ip}\nattemps:{amount}\nrisk: {risk}".upper())

    file.write(f"{separator}")
    for ip, amount in suspect_counter.items():
        if amount > 20:
            risk = "HIGH RISK"
            file.write(f"TOP ATTACKER:\n\nIP:\n{ip}\n\nAttempts:\n{amount}\n\nRisk:\n{risk}".upper())

    # Add basic SOC recommendations based on failed login activity
    file.write(f"{separator}SOC RECOMMENDATIONS\n\n")
    for ip, amount in suspect_counter.items():
        if amount > 20:
            file.write(f"- Block {ip}\n")
        elif amount >= 10:
            file.write(f"- Monitor {ip}\n")
    file.write(f"- Review account lockouts.\n- Investigate brute force attempts.")    
    file.write(f"{separator}END OF REPORT")





