#Convert the time entered in hh,min and sec into seconds.
hours = int(input("Enter Hours:"))
minutes = int(input("Enter Minutes:"))
seconds = int(input("Enter Seconds:"))

total_seconds = (hours * 3600) + (minutes * 60) + seconds

print("Total Seconds =",total_seconds)