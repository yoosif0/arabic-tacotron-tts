import os
with open("temp.csv", encoding="utf-8") as file:
    filtered=[]
    for line in file.readlines():
        if "فِي" in line:
            filtered.append(line)
        else:
            try:
                os.remove(f"./wavs/ARA NORM  {line[:4]}.wav")
            except OSError:
                pass
    with open("temp_filtered.csv", mode="w", encoding="utf-8") as wrFile:
        wrFile.writelines(filtered)