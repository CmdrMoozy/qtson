import shutil
from subprocess import Popen, PIPE

def format_json(json):
	"""
	This is a very simple function which formats (i.e., inserts line breaks and tabs and etc.)
	the given JSON string using the "json_reformat" executable from the yajl JSON library. If
	the executable can't be found, we throw an exception.

	:param json: the JSON code to format
	:returns: the formatted JSON code as a plain string.
	"""

	# Locate the json_reformat command from the yajl package.

	yajl = shutil.which('json_reformat')

	if yajl is None:
		raise Exception('Couldn\'t locate yajl json_reformat executable.')

	# Reformat the JSON string we were given.

	outs = None
	errs = None

	with Popen([yajl], stdout=PIPE, stdin=PIPE, stderr=PIPE) as p:
		outs, errs = p.communicate(input=json.encode('utf-8'), timeout=15)

	return outs
