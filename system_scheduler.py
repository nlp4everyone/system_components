import datetime
import time
import schedule
# For more information, go to this website (https://schedule.readthedocs.io/en/stable/examples.html)

# Do action with specific time
def my_function():
    print("Hello, World!")

# Set the time for the function to run
run_time = datetime.time(hour=10, minute=39, second=0)

# Define a function to schedule the job
def schedule_job():
    schedule.every().day.at(str(run_time)).do(my_function)

# Schedule the job
schedule_job()

# Loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)