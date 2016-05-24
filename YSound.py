from getAudioFromYoutube import getAudioFromYoutube
import threading

def main():
    print("Hi!")
    print("Enter song names you would like to download")
    print("To complete the list write DONE")
    while (True):
        print("-"*50)
        print("\n"*2)
        s = input("SONG NAME: ")
        if (s.upper()  == "DONE"):
            print("\nPlease, wait until all downloads will be finished")
            break
        getAudioFromYoutube(s)
#        After some experiments its become clear that we don't need
#        multithreading :D
#        But sometimes it could be useful(If you downloading 50 min album).
#        Uncomment if you need it.
#        thr = threading.Thread(target=getAudioFromYoutube, args=[s], kwargs={})
#        thr.start()
    print("-"*50)
    print("Perfect!\nAll audio files saved to music folder\nEnjoi ;)")

if __name__ == '__main__':
    main()
