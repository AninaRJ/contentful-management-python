import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from contentful.add_lyricist import create_lyricist_payload
from contentful.add_singer import create_singer_payload
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Contentful: Add Album Details')
        self.layout = QVBoxLayout()
       
        self.setAlbumAdditionLayout()

        self.setLayout(self.layout)

    def on_lyricist_button_click(self):
        create_lyricist_payload()
    
    def on_singer_button_click(self):
        create_singer_payload()
    
    def setAlbumAdditionLayout(self):
        self.lyricist_add_btn = QPushButton('Add Lyricists')
        self.lyricist_add_btn.clicked.connect(self.on_lyricist_button_click)

        self.singer_add_btn = QPushButton('Add Singers')
        self.singer_add_btn.clicked.connect(self.on_singer_button_click)
        self.layout.addWidget(self.singer_add_btn)
        self.layout.addWidget(self.lyricist_add_btn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
