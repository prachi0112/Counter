from moviepy.editor import VideoFileClip
import os
import mutagen


def console():
    try:
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
                if file.endswith(("mp4", "avi", "flv", "wmv", "mov", "mkv")):
                    video = VideoFileClip(root+"/"+file)
                    print(file, end=" ")
                    print("{:.2f}".format(video.duration/60))
                    count_mp4 += video.duration
                    video.reader.close()
                    video.audio.reader.close_proc()
                    # del video.reader
                elif file.endswith("mp3"):
                    song = mutagen.File(root+"/"+file)
                    print(file, end=" ")
                    print("{:.2f}".format(song.info.length / 60))
                    count_mp3 += song.info.length
        print("{} {:.2f}".format("count_mp4", count_mp4/60))
        print("{} {:.2f}".format("count_mp3", count_mp3/60))
    except BaseException as err:
        print(err)
        
    finally:
        print("Thanks for using Counter. Hope you liked it :)")


if __name__ == '__main__':
    console()
