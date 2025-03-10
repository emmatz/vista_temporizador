# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mensajeEmeriYLpMI.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 550)
        Form.setMinimumSize(QSize(700, 550))
        icon = QIcon()
        icon.addFile(u":/iconos/ojo2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 500, 201, 31))
        font = QFont()
        font.setFamilies([u"Segoe MDL2 Assets"])
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.imagenLabel = QLabel(Form)
        self.imagenLabel.setObjectName(u"imagenLabel")
        self.imagenLabel.setGeometry(QRect(20, 20, 661, 461))
        self.imagenLabel.setPixmap(QPixmap(u":/iconos/ojo2.png"))
        self.imagenLabel.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Tiempo de descansar la vista", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Salir", None))
        self.imagenLabel.setText("")
    # retranslateUi

