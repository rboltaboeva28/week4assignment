log_data = """[INFO] System started successfully
[WARNING] Memory usage high
[ERROR] Database connection failed
[INFO] User logged in
[ERROR] Payment gateway timeout
[INFO] Scheduled backup complete
[ERROR] Disk space critical"""

with open("server_log.txt", "w") as f:
    f.write(log_data)


counter = 0
with open("server_log.txt", "r") as file, open ("urgent_alerts.txt","w") as file2:
    for line in file:
        if "ERROR" in line:
            file2.write(f"{line}")
            counter += 1

print(f"Scan complete. Found {counter} errors.\nPlease check urgent_alerts.txt.")
