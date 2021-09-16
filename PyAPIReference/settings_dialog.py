from PyQt5.QtWidgets import QWidget, QLabel, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QStyle
from PyQt5.QtCore import Qt
from qtwidgets import AnimatedToggle
from multipledispatch import dispatch

class FormLayout(QVBoxLayout):
	"""This layout will work as QFormLayout but this will center the two columns vertically.
	QFormLayout:
		--- ___
	This:
		--- ---
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	@dispatch(QWidget, QWidget)
	def addRow(self, widget1: QWidget, widget2: QWidget):
		row = QWidget()
		row.setLayout(QHBoxLayout())
		
		row.layout().addWidget(widget1)
		row.layout().addWidget(widget2)

		self.addWidget
		self.addWidget(row)

	@dispatch(str, QWidget)
	def addRow(self, string: str, widget: QWidget):
		row = QWidget()
		row.setLayout(QHBoxLayout())
		
		row.layout().addWidget(QLabel(string))
		row.layout().addWidget(widget)

		self.addWidget(row)

	@dispatch(QWidget)
	def addRow(self, widget: QWidget):
		self.addWidget(widget)

def create_settings_dialog(prefs, *, title="Settings dialog", parent=None):
	def apply_changes():
		dark_theme_toggle_state = dark_theme_toggle.checkState()
		
		if dark_theme_toggle_state == 0:
			prefs.write_prefs("theme", "light")
		elif dark_theme_toggle_state == 2:
			prefs.write_prefs("theme", "dark")		

		dialog.done(1)

	dialog = QDialog(parent=parent)
	dialog.setWindowTitle(title)
	dialog.setLayout(FormLayout())
	dialog.setMaximumSize(0, 0)

	dark_theme_toggle = AnimatedToggle()
	if prefs.file["theme"] == "light":
		state = 0
	elif prefs.file["theme"] == "dark":
		state = 1
		
	dark_theme_toggle.setCheckState(state)

	apply_button = QPushButton(icon=dialog.style().standardIcon(QStyle.SP_DialogApplyButton), text="Apply")
	apply_button.clicked.connect(apply_changes)

	# Add widgets to layout
	dialog.layout().addRow("Dark theme: ", dark_theme_toggle)

	dialog.layout().addRow(apply_button)

	return dialog.exec_()
