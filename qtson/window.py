from PyQt4.QtCore import Qt
from PyQt4 import QtGui, QtWebKit

import qtson.format
import qtson.highlight

class QtSONWindow(QtGui.QMainWindow):
	"""
	This class defines a QMainWindow which will contain all of our application's interface
	components.
	"""

	__central_widget = None
	__layout = None
	__splitter = None

	__input_group_box = None
	__input_layout = None
	__input_text_edit = None

	__output_group_box = None
	__output_layout = None
	__output_web_view = None

	def __init__(self, parent = None):
		"""
		This constructor initializes this window instance.
		"""

		super(QtSONWindow, self).__init__(parent)

		self.setWindowTitle('QtSON - A Simple JSON Formatter')

		self.__init_widgets()

	def format_json(self):
		"""
		This is a slot which reformats whatever JSON is currently in the "input" text
		field.
		"""

		json = qtson.format.format_json(str(self.__input_text_edit.toPlainText()))
		json = qtson.highlight.highlight_json(json)
		self.__output_web_view.setHtml(json)

	def __init_widgets(self):
		"""
		This is a small utility function which initializes all of the widgets that make up
		our application's UI.
		"""

		# Initialize our central widget.

		self.__central_widget = QtGui.QWidget(self)
		self.__layout = QtGui.QGridLayout(self.__central_widget)

		self.__splitter = QtGui.QSplitter(Qt.Vertical, self.__central_widget)

		self.__layout.addWidget(self.__splitter, 0, 0, 1, 1)

		# Initialize our input widgets.

		self.__input_group_box = QtGui.QGroupBox('Input', self.__splitter)
		self.__input_layout = QtGui.QGridLayout(self.__input_group_box)

		self.__input_text_edit = QtGui.QPlainTextEdit(self.__input_group_box)

		self.__input_layout.addWidget(self.__input_text_edit, 0, 0, 1, 1)
		self.__input_group_box.setLayout(self.__input_layout)
		self.__splitter.addWidget(self.__input_group_box)

		# Initialize our output widgets.

		self.__output_group_box = QtGui.QGroupBox('Output', self.__splitter)
		self.__output_layout = QtGui.QGridLayout(self.__output_group_box)

		self.__output_web_view = QtWebKit.QWebView(self.__output_group_box)

		self.__output_layout.addWidget(self.__output_web_view, 0, 0, 1, 1)
		self.__output_group_box.setLayout(self.__output_layout)
		self.__splitter.addWidget(self.__output_group_box)

		# Set our central widget.

		self.__central_widget.setLayout(self.__layout)
		self.setCentralWidget(self.__central_widget)

		# Connect various signals and slots.

		self.__input_text_edit.textChanged.connect(self.format_json)
