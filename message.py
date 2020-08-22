import os
from time import sleep

#get the words in the lyrics
def get_words():
    with open('lyrics.txt') as lyrics:
        words=[line.strip() for line in lyrics]
        string=" ".join(words)
        return string

#splt the song lyrics into a list of words
def get_list(lyric_string):
    return lyric_string.split()

#sends the lyrics
def send(number, word):
    os.system('osascript send.applescript {} "{}"'.format(number,word))

if __name__ == '__main__':
    song=get_list(get_words())
    #get the phone number from the user
    phonenumber=input()
    #loops through the song lyrics and send them one by one
    for lyric in song:
        send(phonenumber,lyric)
        sleep(.5)
        