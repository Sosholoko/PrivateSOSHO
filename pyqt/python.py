import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")

        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Welcome ! What's your name ?")

        my_label.setFont(qtg.QFont('Helvetica', 19))
        self.layout().addWidget(my_label)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        my_button = qtw.QPushButton("Click", 
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            my_label.setText(f'Hello {my_entry.text()}')
            my_entry.setText("")
        
        #Show the app
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()