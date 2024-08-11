from PySide6.QtWidgets import (QApplication, 
	QMainWindow,
	QTabWidget, 
	QWidget, 
	QVBoxLayout, 
	QHBoxLayout,
	QLabel,
	QTextEdit,
	QPushButton,
	QLineEdit,
	QTableWidget, 
	QTableWidgetItem, 
	QCheckBox, 
	QHeaderView)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('PyTwitch')

		# Tab widget for the main content
		self.tabWidget = QTabWidget()
		self.view1 = self.createDashboardView()
		self.view2 = self.createConfigureView()
		# self.view3 = self.createView('This is View 3')

		# Add views as tabs
		self.tabWidget.addTab(self.view1, 'Dashboard')
		self.tabWidget.addTab(self.view2, 'Configure')
		# self.tabWidget.addTab(self.view3, 'About Me')

		# Set the tab widget as the central widget
		self.setCentralWidget(self.tabWidget)

	def createView(self, text):
		"""Helper function to create views."""
		view = QWidget()
		layout = QVBoxLayout()
		label = QLabel(text)
		layout.addWidget(label)
		view.setLayout(layout)
		return view

	def createDashboardView(self):
		"""Specific function to create the Dashboard view with a terminal log and a Start button."""
		view = QWidget()
		layout = QVBoxLayout()

		# Terminal log display
		terminalLog = QTextEdit()
		terminalLog.setReadOnly(True)  # Make the QTextEdit read-only to simulate a terminal log
		terminalLog.setPlaceholderText("Terminal log will be displayed here...")

		# Start button
		startButton = QPushButton("Start")

		# Add the terminal log and start button to the layout
		layout.addWidget(terminalLog)
		layout.addWidget(startButton)

		view.setLayout(layout)
		return view

	def createConfigureView(self):
		"""Function to create configure view"""
		view = QWidget()
		layout = QVBoxLayout()

		inputLayout = QHBoxLayout()
		accessTokenLabel = QLabel('Twitch OAuth Access Token <span style="font-size:8pt;">[?]</span>: ')
		accessTokenLabel.setToolTip("Your Twitch OAuth access token is required for authentication.")
		accessTokenText = QLineEdit()

		inputLayout.addWidget(accessTokenLabel)
		inputLayout.addWidget(accessTokenText)

		layout.addLayout(inputLayout)

		# Create the table
		table = QTableWidget()
		table.setColumnCount(2)  # Set the number of columns
		table.setHorizontalHeaderLabels(["Activate", "User"])
		table.setRowCount(3)  # Example row count

		header = table.horizontalHeader()
		header.setSectionResizeMode(QHeaderView.Fixed)

		# Populate the table with checkboxes and user strings
		for row in range(table.rowCount()):
			# Activate column with checkbox
			checkBox = QCheckBox()
			table.setCellWidget(row, 0, checkBox)

			# User column with string
			userItem = QTableWidgetItem(f"User {row + 1}")
			table.setItem(row, 1, userItem)

		layout.addWidget(table)  # Add the table to the main layout
		
		saveButton = QPushButton("Save")
		layout.addWidget(saveButton)
		
		view.setLayout(layout)
		return view

  

if __name__ == "__main__":
	app = QApplication([])
	window = MainWindow()
	window.show()
	app.exec()