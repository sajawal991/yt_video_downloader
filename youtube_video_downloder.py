import requests
from pytube import YouTube
import pyfiglet
from os import system ,name
from time import sleep
def original_code():
    video_link=str(input("Enter youtube video link : "))
    link=YouTube(video_link)
    video=link.streams.get_highest_resolution()
    print()
    print("PLEASE WAIT YOUR VIDEO DOWNLOADING.....")
    video.download()
    sleep(2)
    print()
    print()
    print("Done...")
def beauty2():
    print("=======================")
def beauty():
     print("   =====================================================================================")
def curent_working_dir():
	if name == 'nt':
		_ = system('cd')
	else:
		_ = system('pwd')

def banner_for_YT():
    beauty()
    ascii_banner = pyfiglet.figlet_format("      YT_video")
    print(ascii_banner)
    print("                                      Aurthor---->Sajawal Khan Sadozai")
    beauty()
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
sleep(5)
clear()
print("YT video Downloder STARTING PLEASE WAIT....")
sleep(5)
clear()
banner_for_YT()
original_code()
print()
print("Your video location")
beauty2()
curent_working_dir()
beauty2()