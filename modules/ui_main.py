# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    font: 25pt \"Segoe UI\";\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"#stackedWidget QPushButton {\n"
"    border: 2px solid rgb(203, 204, 200);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(203, 204, 200);\n"
"}\n"
"#stackedWidget QPushButton:hover {\n"
"    background-color: rgb(203, 204, 200);\n"
"    border: 2px solid rgb(152, 153, 150);\n"
"}\n"
"#stackedWidget QPushButton:pressed {    \n"
"    background-color: rgb(152, 153, 150);\n"
"    border: 2px solid rgb(152, 153, 150);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("border-image: url(:/images/images/background.jpg) 0 0 0 0 stretch stretch;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setStyleSheet("")
        self.home_page.setObjectName("home_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_frame = QtWidgets.QFrame(self.home_page)
        self.title_frame.setStyleSheet("border-image: none;")
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.title_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_label = QtWidgets.QLabel(self.title_frame)
        self.title_label.setTextFormat(QtCore.Qt.RichText)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout_3.addWidget(self.title_label)
        self.verticalLayout_2.addWidget(self.title_frame)
        self.button_frame = QtWidgets.QFrame(self.home_page)
        self.button_frame.setStyleSheet("border-image: none;")
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.button_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_training = QtWidgets.QPushButton(self.button_frame)
        self.btn_training.setMinimumSize(QtCore.QSize(500, 60))
        self.btn_training.setMaximumSize(QtCore.QSize(500, 60))
        self.btn_training.setStyleSheet("")
        self.btn_training.setObjectName("btn_training")
        self.verticalLayout_4.addWidget(self.btn_training, 0, QtCore.Qt.AlignHCenter)
        self.btn_start_game = QtWidgets.QPushButton(self.button_frame)
        self.btn_start_game.setMinimumSize(QtCore.QSize(500, 60))
        self.btn_start_game.setMaximumSize(QtCore.QSize(500, 60))
        self.btn_start_game.setObjectName("btn_start_game")
        self.verticalLayout_4.addWidget(self.btn_start_game, 0, QtCore.Qt.AlignHCenter)
        self.btn_settings = QtWidgets.QPushButton(self.button_frame)
        self.btn_settings.setMinimumSize(QtCore.QSize(500, 60))
        self.btn_settings.setMaximumSize(QtCore.QSize(500, 60))
        self.btn_settings.setObjectName("btn_settings")
        self.verticalLayout_4.addWidget(self.btn_settings, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.button_frame)
        self.stackedWidget.addWidget(self.home_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.settings_title_frame = QtWidgets.QFrame(self.settings_page)
        self.settings_title_frame.setStyleSheet("border-image: none;")
        self.settings_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_title_frame.setObjectName("settings_title_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settings_title_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.settings_title_label = QtWidgets.QLabel(self.settings_title_frame)
        self.settings_title_label.setTextFormat(QtCore.Qt.RichText)
        self.settings_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_title_label.setObjectName("settings_title_label")
        self.verticalLayout_5.addWidget(self.settings_title_label)
        self.verticalLayout_6.addWidget(self.settings_title_frame)
        self.settings_body_frame = QtWidgets.QFrame(self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_body_frame.sizePolicy().hasHeightForWidth())
        self.settings_body_frame.setSizePolicy(sizePolicy)
        self.settings_body_frame.setStyleSheet("border-image: none;")
        self.settings_body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_body_frame.setObjectName("settings_body_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.settings_body_frame)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.task2_label = QtWidgets.QLabel(self.settings_body_frame)
        self.task2_label.setObjectName("task2_label")
        self.gridLayout.addWidget(self.task2_label, 1, 1, 1, 1)
        self.task3_lineEdit = QtWidgets.QLineEdit(self.settings_body_frame)
        self.task3_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.task3_lineEdit.setObjectName("task3_lineEdit")
        self.gridLayout.addWidget(self.task3_lineEdit, 2, 2, 1, 1)
        self.task1_label = QtWidgets.QLabel(self.settings_body_frame)
        self.task1_label.setObjectName("task1_label")
        self.gridLayout.addWidget(self.task1_label, 0, 1, 1, 1)
        self.task3_label = QtWidgets.QLabel(self.settings_body_frame)
        self.task3_label.setObjectName("task3_label")
        self.gridLayout.addWidget(self.task3_label, 2, 1, 1, 1)
        self.num_trials_label = QtWidgets.QLabel(self.settings_body_frame)
        self.num_trials_label.setObjectName("num_trials_label")
        self.gridLayout.addWidget(self.num_trials_label, 3, 1, 1, 1)
        self.lsl_marker_outlet_label = QtWidgets.QLabel(self.settings_body_frame)
        self.lsl_marker_outlet_label.setObjectName("lsl_marker_outlet_label")
        self.gridLayout.addWidget(self.lsl_marker_outlet_label, 4, 1, 1, 1)
        self.lsl_prediction_inlet_label = QtWidgets.QLabel(self.settings_body_frame)
        self.lsl_prediction_inlet_label.setObjectName("lsl_prediction_inlet_label")
        self.gridLayout.addWidget(self.lsl_prediction_inlet_label, 5, 1, 1, 1)
        self.num_trials_lineEdit = QtWidgets.QLineEdit(self.settings_body_frame)
        self.num_trials_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.num_trials_lineEdit.setObjectName("num_trials_lineEdit")
        self.gridLayout.addWidget(self.num_trials_lineEdit, 3, 2, 1, 1)
        self.task2_lineEdit = QtWidgets.QLineEdit(self.settings_body_frame)
        self.task2_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.task2_lineEdit.setObjectName("task2_lineEdit")
        self.gridLayout.addWidget(self.task2_lineEdit, 1, 2, 1, 2)
        self.task1_lineEdit = QtWidgets.QLineEdit(self.settings_body_frame)
        self.task1_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.task1_lineEdit.setObjectName("task1_lineEdit")
        self.gridLayout.addWidget(self.task1_lineEdit, 0, 2, 1, 2)
        self.lsl_marker_outlet_lineEdit = QtWidgets.QLineEdit(self.settings_body_frame)
        self.lsl_marker_outlet_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lsl_marker_outlet_lineEdit.setObjectName("lsl_marker_outlet_lineEdit")
        self.gridLayout.addWidget(self.lsl_marker_outlet_lineEdit, 4, 2, 1, 1)
        self.lsl_prediction_inlet_lineEdit = QtWidgets.QLineEdit(self.settings_body_frame)
        self.lsl_prediction_inlet_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lsl_prediction_inlet_lineEdit.setObjectName("lsl_prediction_inlet_lineEdit")
        self.gridLayout.addWidget(self.lsl_prediction_inlet_lineEdit, 5, 2, 1, 1)
        self.btn_save_settings = QtWidgets.QPushButton(self.settings_body_frame)
        self.btn_save_settings.setObjectName("btn_save_settings")
        self.gridLayout.addWidget(self.btn_save_settings, 6, 1, 1, 2)
        self.verticalLayout_6.addWidget(self.settings_body_frame)
        self.stackedWidget.addWidget(self.settings_page)
        self.game_page = QtWidgets.QWidget()
        self.game_page.setObjectName("game_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.game_page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.game_frame = QtWidgets.QFrame(self.game_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_frame.sizePolicy().hasHeightForWidth())
        self.game_frame.setSizePolicy(sizePolicy)
        self.game_frame.setStyleSheet("border-image: none;")
        self.game_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.game_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.game_frame.setObjectName("game_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.game_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_2.addWidget(self.game_frame, 1, 0, 1, 2)
        self.top_frame = QtWidgets.QFrame(self.game_page)
        self.top_frame.setStyleSheet("border-image: none;")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtWidgets.QPushButton(self.top_frame)
        self.btn_back.setMinimumSize(QtCore.QSize(60, 30))
        self.btn_back.setStyleSheet("font: 15pt \"Segoe UI\";\n"
"font-weight: 500;")
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back, 0, QtCore.Qt.AlignLeft)
        self.game_title_label = QtWidgets.QLabel(self.top_frame)
        self.game_title_label.setStyleSheet("")
        self.game_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.game_title_label.setObjectName("game_title_label")
        self.horizontalLayout.addWidget(self.game_title_label)
        self.score_label = QtWidgets.QLabel(self.top_frame)
        self.score_label.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"font-weight: 500;")
        self.score_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score_label.setObjectName("score_label")
        self.horizontalLayout.addWidget(self.score_label)
        self.gridLayout_2.addWidget(self.top_frame, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.game_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_training, self.btn_start_game)
        MainWindow.setTabOrder(self.btn_start_game, self.btn_settings)
        MainWindow.setTabOrder(self.btn_settings, self.task1_lineEdit)
        MainWindow.setTabOrder(self.task1_lineEdit, self.task2_lineEdit)
        MainWindow.setTabOrder(self.task2_lineEdit, self.task3_lineEdit)
        MainWindow.setTabOrder(self.task3_lineEdit, self.num_trials_lineEdit)
        MainWindow.setTabOrder(self.num_trials_lineEdit, self.lsl_marker_outlet_lineEdit)
        MainWindow.setTabOrder(self.lsl_marker_outlet_lineEdit, self.lsl_prediction_inlet_lineEdit)
        MainWindow.setTabOrder(self.lsl_prediction_inlet_lineEdit, self.btn_save_settings)
        MainWindow.setTabOrder(self.btn_save_settings, self.btn_back)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600;\">BCI Hoops</span></p></body></html>"))
        self.btn_training.setText(_translate("MainWindow", "Training"))
        self.btn_start_game.setText(_translate("MainWindow", "Start Game"))
        self.btn_settings.setText(_translate("MainWindow", "Settings"))
        self.settings_title_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:50pt; font-weight:600;\">Settings</span></p></body></html>"))
        self.task2_label.setText(_translate("MainWindow", "Task 2:"))
        self.task3_lineEdit.setText(_translate("MainWindow", "Task 3"))
        self.task1_label.setText(_translate("MainWindow", "Task 1:"))
        self.task3_label.setText(_translate("MainWindow", "Task 3:"))
        self.num_trials_label.setText(_translate("MainWindow", "Number of Trials:"))
        self.lsl_marker_outlet_label.setText(_translate("MainWindow", "LSL Marker Outlet:"))
        self.lsl_prediction_inlet_label.setText(_translate("MainWindow", "LSL Prediction Inlet:"))
        self.num_trials_lineEdit.setText(_translate("MainWindow", "15"))
        self.task2_lineEdit.setText(_translate("MainWindow", "Task 2"))
        self.task1_lineEdit.setText(_translate("MainWindow", "Task 1"))
        self.lsl_marker_outlet_lineEdit.setText(_translate("MainWindow", "bci_hoops_marker"))
        self.lsl_prediction_inlet_lineEdit.setText(_translate("MainWindow", "bcipy_prediction"))
        self.btn_save_settings.setText(_translate("MainWindow", "Save"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.game_title_label.setText(_translate("MainWindow", "BCI Hoops"))
        self.score_label.setText(_translate("MainWindow", "Score: 0"))
from . resources_rc import *
