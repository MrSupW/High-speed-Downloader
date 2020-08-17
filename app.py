from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox

import globals as g
from threads import MultiThreadDownload
from ui.main import Ui_Window


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Window()
        self.ui.setupUi(self)
        self.ui.lineEdit_dir.setText('./')
        # 绑定槽函数
        self.ui.button_select_dir.clicked.connect(self.selectTargetDir)
        self.ui.button_start.clicked.connect(self.startDownload)
        self.multi_download_thread = MultiThreadDownload(self.dealTextAndProgressSignal)
        self.multi_download_thread.text_and_progress_signal.connect(self.dealTextAndProgressSignal)
        self.multi_download_thread.download_finished.connect(self.downloadFinished)

    def selectTargetDir(self):
        target_dir = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
        if target_dir != '':
            g.download_target_dir = target_dir
            self.ui.lineEdit_dir.setText(g.download_target_dir)
        else:
            QMessageBox(QMessageBox.Warning, '警告', '选择的文件夹为空！！').exec_()

    def dealTextAndProgressSignal(self, info, value):
        self.ui.plainTextEdit_result.appendPlainText(info)
        new_value = self.ui.progressBar.value() + value
        if new_value > 99:
            new_value = 99
        self.ui.progressBar.setValue(new_value)

    def downloadFinished(self):
        self.ui.progressBar.setValue(100)

    def startDownload(self):
        g.download_thread_num = int(self.ui.comboBox.currentText())
        g.download_url = self.ui.lineEdit_url.text()
        self.ui.progressBar.setValue(0)
        g.is_start = False
        if g.download_url == '' or g.download_target_dir == '':
            QMessageBox(QMessageBox.Warning, '警告', '网址和存储文件夹均不能为空！！').exec_()
            return
        self.ui.plainTextEdit_result.setPlainText('下载链接: \n{}\n'.format(g.download_url) + '\n正在解析该链接......')
        self.multi_download_thread.start()


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
