'''Program to use language translator service to translate text from one language to another'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Function to convert english text to french text'''
    translator_response = language_translator.translate(text=english_text,model_id='en-fr')
    translation = translator_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Function to convert french text to english'''
    translator_response = language_translator.translate(text=french_text,model_id='fr-en')
    translation = translator_response.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
