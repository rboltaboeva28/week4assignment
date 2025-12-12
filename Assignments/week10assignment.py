def analyze_logs(log_entries):
    error_dict = {}
    for entry in log_entries:
        ip, status = entry.split(" - ")
        if ip not in error_dict:
            error_dict[ip] = 0
        if status == "404" or status == "500":
            error_dict[ip] += 1
    return error_dict
 
def flag_suspicious_ips(error_dict):
    for ip, count in error_dict.items():
        if count >= 3:
            print(f"SECURITY ALERT: {ip} has {count} errors.")

log_entries = [
    "192.168.1.1 - 200",
    "10.0.0.5 - 404",
    "192.168.1.1 - 200",
    "10.0.0.5 - 500",
    "172.16.0.1 - 404",
    "10.0.0.5 - 404",
    "192.168.1.1 - 500",
    "10.0.0.5 - 404"
]
result = analyze_logs(log_entries)
print("Error Counts: ")
for ip, count in result.items():
    print(f"{ip}: {count}")
print("--------------------")
flag_suspicious_ips(result)