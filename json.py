import sublime
import sublime_plugin
import json

class JsonCommand(sublime_plugin.TextCommand):	

	@staticmethod
	def try_convert_to_int(v):
		try:
			v = int(v)
		except:
			a = ""
			# Do nothing. Not an int so don't convert type
		return v

	@staticmethod
	def try_convert_to_double(v):
		try:
			v = double(v)
		except:
			a = ""
			# Do nothing. Not an int so don't convert type
		return v


	@staticmethod
	def clean_json(d):
	    d =  {k: v for k, v in d.items() if v is not None }	    
	    d =  {k: v for k, v in d.items() if v != [] }

	    for k,v in d.items():
	    	if isinstance(v, str):
	    		d[k] = JsonCommand.try_convert_to_int(v)
	    	# if isinstance(v, str):
	    	# 	d[k] = JsonCommand.try_convert_to_double(v)
	    	if isinstance(v, list):
	    		newList = [JsonCommand.try_convert_to_int(x) for x in v]
	    		d[k] = newList
	    return d


	def run(self, edit):
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		bqJson = json.loads(contents, object_hook=JsonCommand.clean_json)
		bidRequest = bqJson["bidRequest"]
		json_object = json.dumps(bidRequest, indent = 4) 
		self.view.replace(edit, sublime.Region(0, self.view.size()), json_object)

