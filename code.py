import os
import mutagen

path = input("Enter the path to the folder: ")
a = os.walk(path)
extension = []
file_list = []
count_mp4 = 0
count_mp3 = 0
# Finding extension dynamically
for root, folder, files in a:
    for file in files:
        for i in range(len(file)-1, 0, -1):
            if file[i] == ".":
                file_list.append(file[i+1:])
                d = set(file_list)
                if file[i+1:] not in extension:
                    extension.append(file[i+1:])
                    break
                else:
                    break
# print(extension)
# print(file)
for i in range(len(extension)):
    print("{} {}".format(extension[i], file_list.count(extension[i])))

'''for i in extension:
    key = i
    c[key] = 0
print(c)'''

a = os.walk(path)

for root, folder, files in a:
    for file in files:
        if file.endswith("mp4"):
            video = mutagen.File(path+"/"+file)
            count_mp4 += video.info.length
        elif file.endswith("mp3"):
            song = mutagen.File(path+"/"+file)
            count_mp3 += song.info.length
print("{} {}".format("count_mp4", count_mp4/60))
print("{} {}".format("count_mp3", count_mp3/60))
