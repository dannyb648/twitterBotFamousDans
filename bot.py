import glob 
import os
import random
import csv
import sys
import tweepy
from OAuthSettings import settings

CONSUMER_KEY = settings['consumer_key']
CONSUMER_SECRET = settings['consumer_secret']
ACCESS_KEY = settings['access_token_key']
ACCESS_SECRET = settings['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def setList():
	pictures = []
	os.chdir("/Users/danny/documents/codingProjects/danTwitter")
	for file in glob.glob("*.jpg"):
		pictures.append(file)
	return pictures

def setNames(pictures):
	x = 0
	pictureName = []
	for pic in pictures:
		pictureName.append(str(pictures[x]))
		x = x + 1
	return pictureName

def fixNames(pictureName):
	for x in range(0,len(pictureName)):
		pictureName[x] = pictureName[x].replace('_',' ')
		temp = pictureName[x]
		pictureName[x] = temp[:-4]
	return pictureName

def generateTweet(pictureNames, pictures):
	num = random.randint(0,(len(pictureNames) - 1))
	tweet = str(pictureNames[num]) + " " + "#dan"
	photo_path = str(pictures[num])
	return tweet, photo_path

def main():
	pictures = setList()
	pictureName = setNames(pictures)
	pictureName = fixNames(pictureName)
	tweet, photo_path = generateTweet(pictureName, pictures)
	api.update_with_media(photo_path, status=tweet) 
	
if __name__ == '__main__':
	main()
