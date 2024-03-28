import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Create sub-layouts
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        # Create buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        # Add buttons to top layout
        top_layout.addWidget(button1)
        top_layout.addWidget(button2)

        # Add button3 to bottom layout
        bottom_layout.addWidget(button3)

        # Add sub-layouts to main layout
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        self.setWindowTitle('Layout Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())
