import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QMovie, QPainter, QColor, QPolygon, QPen, QFont, QImage
from PyQt5.QtCore import Qt, QPoint, QTimer
from math import cos as qCos, sin as qSin, radians as qDegreesToRadians
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from gauge import AnalogGaugeWidget
import folium




class MapWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()

        self.setWindowTitle("Map")
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()

        #displaying the map
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_map(self):
        map_center = [37.568512, -122.3087851]
        m = folium.Map(location=map_center, zoom_start=14)

        #Folium marker at the map center
        folium.Marker(map_center, tooltip='Your Location').add_to(m)

        #Folium map to html string
        map_html = m._repr_html_()

        #html content QWebEngineView
        self.web_view.setHtml(map_html)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        

        self.initUI()
    
    def open_map_window(self):
        map_window = MapWindow()
        map_window.show()
        map_window.show_map()
    def initUI(self):
        self.setWindowTitle("Alef Dashboard")
        self.setGeometry(200, 200, 1117, 636)
        self.setStyleSheet("background-color: rgb(30, 31, 40);")

        self.gif_label = QLabel(self)
        self.gif_label.setGeometry(0, 0, 1117, 636)
        self.gif_label.setAlignment(Qt.AlignCenter)
        self.gif_label.setStyleSheet("background-color: black;")

        

        file_path = "background2.gif"
        self.movie = QMovie(file_path)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.gif_label.setMovie(self.movie)
        self.movie.start()

       

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(306, 60, 521, 61))
        self.frame.setStyleSheet("QFrame{\n"
"background:None;\n"
"}\n"
"\n"
"QPushButton{\n"
"    \n"
"    background-color: rgba(0, 150, 255, 200);\n"
"    border:None;\n"
"    color:#000000;\n"
"    font: 12pt;\n"
"\n"
"}\n"
"QPushButton:Hover{\n"
"\n"
"    \n"
"    background-color: rgba(0, 150, 255, 200);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"    \n"
"    \n"
"background-color: rgba(0, 150, 255, 200);\n"
"\n"
"}")

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_dash = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dash.sizePolicy().hasHeightForWidth())
        self.btn_dash.setSizePolicy(sizePolicy)
        self.btn_dash.setObjectName("btn_dash")
        self.horizontalLayout.addWidget(self.btn_dash)
        self.btn_ac = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(sizePolicy)
        self.btn_ac.setObjectName("btn_ac")
        self.horizontalLayout.addWidget(self.btn_ac)
        self.btn_music = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_music.sizePolicy().hasHeightForWidth())
        self.btn_music.setSizePolicy(sizePolicy)
        self.btn_music.setObjectName("btn_music")
        self.horizontalLayout.addWidget(self.btn_music)
        self.btn_map = QPushButton("Map", self.frame)
        self.btn_map.setSizePolicy(sizePolicy)
        self.btn_map.setObjectName("btn_map")
        self.horizontalLayout.addWidget(self.btn_map)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_map.sizePolicy().hasHeightForWidth())
        self.btn_map.setSizePolicy(sizePolicy)
        self.btn_map.setObjectName("btn_map")
        self.horizontalLayout.addWidget(self.btn_map)
        self.frame_dashboard = QtWidgets.QFrame(self)
        self.frame_dashboard.setEnabled(True)
        self.frame_dashboard.setGeometry(QtCore.QRect(350, 150, 411, 411))
        self.frame_dashboard.setStyleSheet("QFrame{\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:0, y1:1, "
                                   "stop:0 rgb(0, 0, 0), stop:1 rgb(0, 0, 69));\n"
                                   "border-radius: 200px;\n"
                                   "}")
        self.frame_dashboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dashboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dashboard.setObjectName("frame_dashboard")
        self.speed = AnalogGaugeWidget(self.frame_dashboard)
        self.speed.setGeometry(QtCore.QRect(50, 60, 311, 281))
        self.speed.setStyleSheet("background-color: rgb(100, 100, 127);\n"
"border-radius:o px;")
        self.speed.setObjectName("speed")
        self.rpm = AnalogGaugeWidget(self.frame_dashboard)
        self.rpm.setGeometry(QtCore.QRect(630, 50, 311, 281))
        self.rpm.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"border-radius:o px;")
        self.rpm.setObjectName("rpm")
        self.frame_2 = QtWidgets.QFrame(self.frame_dashboard)
        self.frame_2.setGeometry(QtCore.QRect(350, 30, 263, 38))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgba(85, 85, 127,80);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLabel{\n"
"background:None;\n"
"}")
                
        self.frame_range = QtWidgets.QFrame(self)
        self.frame_range.setGeometry(QtCore.QRect(10, 10, 300, 100))
        self.frame_range.setStyleSheet("QFrame{\n"
                                       "background-color: rgba(100, 0, 0, 0);\n"
                                       "border-radius: 15px;\n"
                                       "}")
        
        layout = QVBoxLayout(self.frame_range)

        warning_label = QLabel(self.frame_range)
        image = QPixmap("warning2.png")  
        warning_label.setPixmap(image.scaled(self.frame_range.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        warning_label.setAlignment(Qt.AlignCenter)

        warning_button = QPushButton("Acknowledge Warning", self.frame_range)

        layout.addWidget(warning_label)
        layout.addWidget(warning_button)

        self.btn_map.clicked.connect(self.open_map_window)
        
        self.btn_map = QPushButton("Map", self.frame)
        self.btn_map.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.btn_map.setObjectName("btn_map")
        self.horizontalLayout.addWidget(self.btn_map)

        

    def open_map_window(self):
        self.map_window = MapWindow()
        self.map_window.show()
        self.map_window.show_map() 




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())