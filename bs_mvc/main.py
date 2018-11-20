from view import Ui_Dialog, QtWidgets
from model import Model

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    model = Model()
    url = "https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181114"
    model.exec(url)
    sys.exit(app.exec_())

