import os
import glob

def cleanup_temp_files (path = "/tmp/*.log") :
    files= glob.glob(path)

    if not files:
        print ("no temp files found")
        return[]
    for file in files :
        try:
            os.remove (file)
            print("removed: {file}")

        except Exception as e:
            print(f"failed to removed {file}: {e}")

cleanup_temp_files("/tmp/*.log")