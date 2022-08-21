import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(600, 600)

    w.setWindowTitle('第一个PythonGUI程序')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()