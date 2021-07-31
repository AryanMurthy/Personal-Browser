import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('http://google.com'))
		self.setCentralWidget(self.browser)
		self.showMaximized()

		navbar = QToolBar() # navigation bar
		self.addToolBar(navbar)

		back_button = QAction('Back', self) # back button
		back_button.triggered.connect(self.browser.back)
		navbar.addAction(back_button)

		forward_button = QAction('Forward', self) # forward button
		forward_button.triggered.connect(self.browser.forward)
		navbar.addAction(forward_button)

		reload_button = QAction('Reload', self) # reload button
		reload_button.triggered.connect(self.browser.reload)
		navbar.addAction(reload_button)

		home_button = QAction('Home', self) # home button
		home_button.triggered.connect(self.navigate_home)
		navbar.addAction(home_button)

		self.url_bar = QLineEdit() # url bar
		self.url_bar.returnPressed.connect(self.navigate_to_url)
		navbar.addWidget(self.url_bar)

		self.browser.urlChanged.connect(self.update_url) #to update url bar when pressed back or forward button

	def navigate_home(self):
		self.browser.setUrl(QUrl('http://github.com/AryanMurthy')) #homepage

	def navigate_to_url(self):
		url = self.url_bar.text()
		self.browser.setUrl(QUrl(url))

	def update_url(self, q):
		self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('porridge') # Name of the browser
window = MainWindow()
app.exec_()
