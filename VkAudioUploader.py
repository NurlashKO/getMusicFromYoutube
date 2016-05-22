from getAudioFromYoutube import getAudioFromYoutube
import threading
from AuthToVK import auth_to_vk

def main():
    print("Hi!")
    print("Enter song names you would like to download")
    print("To complete the list write DONE")
    while (True):
        print("-"*50)
        s = input("SONG NAME: ")
        if (s.upper()  == "DONE"):
            print("\nPlease, wait until all downloads will be finished")
            break
        getAudioFromYoutube(s)
#        After some experiments its become clear that we don't need
#        multithreading :D
#        thr = threading.Thread(target=getAudioFromYoutube, args=[s], kwargs={})
#        thr.start()
    print("-"*50)
    print("Perfect!\nAll audio files saved to music folder\nEnjoi ;)")

#    s = input("Additinal Option:\n Would you like to upload them to your VK wall?(y/n)")




if __name__ == '__main__':
    main()
