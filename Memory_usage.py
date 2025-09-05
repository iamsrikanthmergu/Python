import psutil

def check_memory(threashold=75)  :
    memory= psutil.virtual_memory()

    used_percent= memory.percent
    print(f"Memory usage percentage : {used_percent}%")

    if used_percent > threashold:
        print(f"Memory usage exceeded {threashold}%")

    else:
        print("Memory usage is normal")

check_memory()