import shutil

def check_disk_usage(path = "/", threshold=80) :
    total, used, free = shutil.disk_usage(path)
    percent_used = (used/total) *100

    print (f"Disk usage at {path} : {percent_used:.2f}")

    if percent_used > threshold :
        print(f" Disk usage exceeded {threshold}%")

    else:
        print(f"Disk usage is normal")

check_disk_usage("/")