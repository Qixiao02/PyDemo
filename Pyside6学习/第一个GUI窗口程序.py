import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import 学生管理系统
def main():
    #创建一个QApplicationl类的实例
    app = QApplication(sys.argv)
    #创建窗口
    main = QMainWindow()
    ui = 学生管理系统.Ui_MainWindow()
    ui.setupUi(main)
    #title
    main.setWindowTitle('学生管理系统')
    main.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()