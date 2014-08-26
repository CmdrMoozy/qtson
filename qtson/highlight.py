from pygments import highlight
from pygments.lexers.web import JsonLexer
from pygments.formatters import HtmlFormatter

def highlight_json(json):
	"""
	This is a very simple function which highlights the given JSON code with the Pygments
	syntax highlighter.

	:param json: the JSON string to highlight
	:returns: the highlighted JSON code, as HTML
	"""

	return highlight(json, JsonLexer(), HtmlFormatter(noclasses=True))
