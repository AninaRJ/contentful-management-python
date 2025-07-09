import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Contentful: Add New ARR Album')
        self.layout = QVBoxLayout()
       
        self.setAlbumAdditionLayout()

        self.setLayout(self.layout)

    def on_button_click(self):
        self.label.setText('Button Clicked!')
    
    def setAlbumAdditionLayout(self):
        self.label = QLabel('Album Name:')
        self.albumName = QLineEdit('Enter album name here')

        self.button = QPushButton('Add Album')

        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.albumName)
        self.layout.addWidget(self.button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
