# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressbar.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        if not ProgressBar.objectName():
            ProgressBar.setObjectName(u"ProgressBar")
        ProgressBar.resize(400, 100)
        self.verticalLayout = QVBoxLayout(ProgressBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ProgressBar)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(ProgressBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setBaseSize(QSize(0, 0))
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(ProgressBar)

        QMetaObject.connectSlotsByName(ProgressBar)
    # setupUi

    def retranslateUi(self, ProgressBar):
        ProgressBar.setWindowTitle(QCoreApplication.translate("ProgressBar", u"Form", None))
        self.label.setText(QCoreApplication.translate("ProgressBar", u"Please wait...", None))
        self.progressBar.setFormat(QCoreApplication.translate("ProgressBar", u"%v/%m", None))
    # retranslateUi

