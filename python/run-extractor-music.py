from subprocess import call
from subprocess import check_call
from os import listdir
from os.path import isfile, join
import os

def extractLowLevelDescriptors (filenamePath, filename):
	check_call(["essentia_streaming_extractor_music", filenamePath, "./output/low_level/" + filename + ".profile"])
	return;

cwd = os.getcwd()
print cwd
dirname = os.path.dirname(os.getcwd())
trackspath = cwd + '/tracks'

print "Tracks path:" +  trackspath

from os import walk

f = []
d = []
for dirpath, dirnames, filenames in walk(trackspath):
	for filename in filenames:
		filenamePath = os.path.join(dirpath, filename)
 		extractLowLevelDescriptors(filenamePath, filename)
    	break

# check_call(["essentia_streaming_extractor_music", "./tracks/ANW2590_04_Un-Sospiro.wav", "./output/low_level/ANW2590.profile"])
