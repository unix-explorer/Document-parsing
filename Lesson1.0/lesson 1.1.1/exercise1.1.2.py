log_data = """
ERROR: Database connection failed at 2024-01-15 10:31:22
INFO: User john_doe logged in successfully
WARNING: CPU usage above 80%
INFO: Backup completed successfully
"""

lines = log_data.strip().split('\n')

for line in lines:
    if line:
        level, message = line.split(':',1)
        print(f"Level:{level.strip().replace(':','')} Message: {message.strip()}")