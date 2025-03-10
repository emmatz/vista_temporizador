# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowffwlmS.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(335, 300)
        MainWindow.setMinimumSize(QSize(335, 300))
        MainWindow.setMaximumSize(QSize(335, 300))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/iconos/ojo2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Segoe MDL2 Assets"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout.addWidget(self.lineEdit)

        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout.addWidget(self.lcdNumber)

        self.pushButtonInicio = QPushButton(self.centralwidget)
        self.pushButtonInicio.setObjectName(u"pushButtonInicio")
        self.pushButtonInicio.setFont(font1)

        self.verticalLayout.addWidget(self.pushButtonInicio)

        self.pushButtonSalir = QPushButton(self.centralwidget)
        self.pushButtonSalir.setObjectName(u"pushButtonSalir")
        self.pushButtonSalir.setFont(font1)

        self.verticalLayout.addWidget(self.pushButtonSalir)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Temporizador", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingrese el tiempo en formato\n"
" (1h 20s), 30s, 1h, 00:01:15, etc.", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ejemplo: 1h 20s, 30s, 1h", None))
        self.pushButtonInicio.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.pushButtonSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

