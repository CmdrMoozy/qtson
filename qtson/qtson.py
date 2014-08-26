import sys
from PyQt4 import QtGui

import qtson.window

def main():
	"""
	This is our application's main entrypoint, which sets up our window and enters the event
	dispatch loop.
	"""

	app = QtGui.QApplication(sys.argv)

	window = qtson.window.QtSONWindow()
	window.show()

	sys.exit(app.exec_())
