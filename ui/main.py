# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(763, 714)
        Window.setStyleSheet("color: rgb(0,0 , 255);")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Window)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Window)
        self.groupBox.setStyleSheet("*{\n"
"    font-size:20px\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 21))
        self.label.setStyleSheet("color:rgb(0, 125, 255)")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_url = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_url.setMinimumSize(QtCore.QSize(0, 21))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("color:rgb(0, 125, 255)")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_dir = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.horizontalLayout_2.addWidget(self.lineEdit_dir)
        self.button_select_dir = QtWidgets.QPushButton(self.groupBox)
        self.button_select_dir.setObjectName("button_select_dir")
        self.horizontalLayout_2.addWidget(self.button_select_dir)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("color:rgb(0, 125, 255)")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_start = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy)
        self.button_start.setMinimumSize(QtCore.QSize(200, 70))
        self.button_start.setStyleSheet("")
        self.button_start.setObjectName("button_start")
        self.horizontalLayout_6.addWidget(self.button_start)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.progressBar = QtWidgets.QProgressBar(Window)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.groupBox_2 = QtWidgets.QGroupBox(Window)
        self.groupBox_2.setStyleSheet("font-size:20px")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setContentsMargins(-1, 11, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.plainTextEdit_result = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_result.setStyleSheet("font-size:16px")
        self.plainTextEdit_result.setReadOnly(True)
        self.plainTextEdit_result.setPlainText("")
        self.plainTextEdit_result.setObjectName("plainTextEdit_result")
        self.horizontalLayout_4.addWidget(self.plainTextEdit_result)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "高速下载器"))
        self.groupBox.setTitle(_translate("Window", "下载参数"))
        self.label.setText(_translate("Window", "下载地址链接"))
        self.lineEdit_url.setPlaceholderText(_translate("Window", "请输入网址"))
        self.label_3.setText(_translate("Window", "保存位置"))
        self.lineEdit_dir.setPlaceholderText(_translate("Window", "请选择保存图片的目标文件夹"))
        self.button_select_dir.setText(_translate("Window", "浏览"))
        self.label_4.setText(_translate("Window", "下载时所用的线程数"))
        self.comboBox.setItemText(0, _translate("Window", "2"))
        self.comboBox.setItemText(1, _translate("Window", "4"))
        self.comboBox.setItemText(2, _translate("Window", "6"))
        self.comboBox.setItemText(3, _translate("Window", "8"))
        self.comboBox.setItemText(4, _translate("Window", "10"))
        self.comboBox.setItemText(5, _translate("Window", "12"))
        self.comboBox.setItemText(6, _translate("Window", "14"))
        self.comboBox.setItemText(7, _translate("Window", "16"))
        self.label_5.setText(_translate("Window", "推荐使用8--12线程"))
        self.button_start.setText(_translate("Window", "开始下载"))
        self.groupBox_2.setTitle(_translate("Window", "下载过程"))
        self.plainTextEdit_result.setPlaceholderText(_translate("Window", "你好，MrSupW"))
