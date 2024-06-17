from crontab import CronTab

from datetime import datetime

with open("/home/rk/Documents/newpython/output.log", "a") as log_file:
    log_file.write(f"Script ran at {datetime.now()}\n")

# Define the command to run the script
python_interpreter = "/usr/bin/python3"  # Update with the correct path if necessary
script_path = "/home/rk/Documents/newpython/data.py"  # Update with the correct path to your script

# Create a new cron job
cron = CronTab(user=True)  # Use user=True for current user or specify the user

# Remove any existing jobs with the same command to avoid duplicates
for job in cron:
    if job.command == f'{python_interpreter} {script_path}':
        cron.remove(job)

# Add new cron job
job = cron.new(command=f'{python_interpreter} {script_path}', comment="Run dat.py daily at 9:08 AM")
# job.setall('* * * * *')
job.setall('8 9 * * *')  # Set to run at 9:08 AM every day

# Write the job to the crontab
cron.write()

print("Cron job created: ", job)
