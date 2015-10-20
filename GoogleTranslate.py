#!/usr/bin/python

import sublime, sublime_plugin
import json
from googleapiclient.discovery import build
service = build('translate', 'v2', developerKey='AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0')

class GoogleTranslateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		result = ''
		for region in self.view.sel():
			if not region.empty():
				v = self.view
				selection = v.substr(region).encode('utf-8')
				resp = service.translations().list(source='en', target='de', q=selection.decode()).execute()

				if (resp and len(resp['translations'])):
					result = resp['translations'][0]['translatedText']

				if result:
					v.replace(edit, region, result)
