import datetime, os, sys

if os.getuid() != 0:
	print("You must run this script as a root privilege !")
	sys.exit()

else:
	def log_message():
	    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	    log_text = f"{timestamp}"

	    with open("/var/log/auto-cron.log", "a") as file:
	        file.write(log_text + "\n")

	log_message()
