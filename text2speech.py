from __future__ import unicode_literals
import requests
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import codecs
import sys  
reload(sys)  

#---------------------------------------------------------------------------------------#
#---------------------------initialized global variables     ---------------------------#
#---------------------------------------------------------------------------------------#
sys.setdefaultencoding('utf8')
url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/voices/en-US_MichaelVoice'
username=' ',
password=' '
text = 'hello Australia'
voice = 'en-GB_KateVoice'
accept = ''
say_this = 'the quick brown fox jumped over the lazy dog at IBM headquarters'
#-----------------------Text To Speech API credentials go here--------------------------#
text_to_speech = TextToSpeechV1(username=' ',password=' ')
#---------------------------------------------------------------------------------------#

#-----------------------Do You wish to see the latest API summary-----------------------#
show_me_the_api_summary = 'yes'           #set to yes or no
#---------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------#
#---------------------------extract the information from the texttospeech API       ----#
#---------------------------------------------------------------------------------------#

def see_api_list(input):

		x = text_to_speech.voices()
		all_voices_in_dictionary = x['voices']
		name_voices = []
		y = len(all_voices_in_dictionary)
		i = 0
		for i in range (y):
			record = all_voices_in_dictionary[i]
			print '********** Voices Types ****************'
			print '********** Voice Number ' + str(i+1) + '**************'
			for key in record.keys():
				try:

					g = record[key]
					str(g).strip( unicode( codecs.BOM_UTF8, "utf8" ) )
					g = g.decode('utf-8')
				except AttributeError:
					str(g).strip( unicode( codecs.BOM_UTF8, "utf8" ) )
					g = str(g)
				except UnicodeEncodeError:
					g.encode('utf-8','ignore')
				if input == 'yes':
					print "the API key name is " + key + " and its value is " + g.encode('utf-8')  #.encode('ascii','ignore')
				if key == 'name':
					name_voices.append(g.encode('utf-8'))
		return(name_voices)

if __name__ == "__main__":
	if show_me_the_api_summary == 'yes':
		name_voices = see_api_list('yes')

x = len(name_voices)
i = 0
for i in range (x):
	fn = 'output_'+name_voices[i]+'.wav'
	with open(join(dirname(__file__), '../Documents/'+fn), 'wb') as audio_file:
	    audio_file.write(text_to_speech.synthesize(say_this,voice=name_voices[i]))

