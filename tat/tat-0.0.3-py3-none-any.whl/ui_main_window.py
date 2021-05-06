# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(0, 554))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.buttonClearGenerated = QPushButton(self.centralwidget)
        self.buttonClearGenerated.setObjectName(u"buttonClearGenerated")
        self.buttonClearGenerated.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.buttonClearGenerated, 3, 6, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(6)
        self.labelClusterCount = QLabel(self.centralwidget)
        self.labelClusterCount.setObjectName(u"labelClusterCount")
        sizePolicy1.setHeightForWidth(self.labelClusterCount.sizePolicy().hasHeightForWidth())
        self.labelClusterCount.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelClusterCount)

        self.clusterCount = QSpinBox(self.centralwidget)
        self.clusterCount.setObjectName(u"clusterCount")
        sizePolicy1.setHeightForWidth(self.clusterCount.sizePolicy().hasHeightForWidth())
        self.clusterCount.setSizePolicy(sizePolicy1)
        self.clusterCount.setMaximum(1000)
        self.clusterCount.setValue(4)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.clusterCount)

        self.labelRunCount = QLabel(self.centralwidget)
        self.labelRunCount.setObjectName(u"labelRunCount")
        sizePolicy1.setHeightForWidth(self.labelRunCount.sizePolicy().hasHeightForWidth())
        self.labelRunCount.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelRunCount)

        self.runCount = QSpinBox(self.centralwidget)
        self.runCount.setObjectName(u"runCount")
        sizePolicy1.setHeightForWidth(self.runCount.sizePolicy().hasHeightForWidth())
        self.runCount.setSizePolicy(sizePolicy1)
        self.runCount.setMaximum(1000)
        self.runCount.setValue(5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.runCount)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.maxIterCount = QSpinBox(self.centralwidget)
        self.maxIterCount.setObjectName(u"maxIterCount")
        sizePolicy1.setHeightForWidth(self.maxIterCount.sizePolicy().hasHeightForWidth())
        self.maxIterCount.setSizePolicy(sizePolicy1)
        self.maxIterCount.setMaximum(1000)
        self.maxIterCount.setValue(100)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.maxIterCount)

        self.buttonGenerate = QPushButton(self.centralwidget)
        self.buttonGenerate.setObjectName(u"buttonGenerate")
        self.buttonGenerate.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.buttonGenerate.sizePolicy().hasHeightForWidth())
        self.buttonGenerate.setSizePolicy(sizePolicy1)
        self.buttonGenerate.setCheckable(False)
        self.buttonGenerate.setChecked(False)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.buttonGenerate)


        self.gridLayout.addLayout(self.formLayout, 12, 6, 1, 1)

        self.scrollAreaDst = QScrollArea(self.centralwidget)
        self.scrollAreaDst.setObjectName(u"scrollAreaDst")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaDst.sizePolicy().hasHeightForWidth())
        self.scrollAreaDst.setSizePolicy(sizePolicy2)
        self.scrollAreaDst.setMinimumSize(QSize(150, 0))
        self.scrollAreaDst.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaDst.setWidgetResizable(True)
        self.scrollAreaWidgetContentsDst = QWidget()
        self.scrollAreaWidgetContentsDst.setObjectName(u"scrollAreaWidgetContentsDst")
        self.scrollAreaWidgetContentsDst.setGeometry(QRect(0, 0, 180, 451))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContentsDst)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollAreaDst.setWidget(self.scrollAreaWidgetContentsDst)

        self.gridLayout.addWidget(self.scrollAreaDst, 2, 6, 1, 1)

        self.scrollAreaSrc = QScrollArea(self.centralwidget)
        self.scrollAreaSrc.setObjectName(u"scrollAreaSrc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollAreaSrc.sizePolicy().hasHeightForWidth())
        self.scrollAreaSrc.setSizePolicy(sizePolicy3)
        self.scrollAreaSrc.setMinimumSize(QSize(0, 0))
        self.scrollAreaSrc.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaSrc.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSrc = QWidget()
        self.scrollAreaWidgetContentsSrc.setObjectName(u"scrollAreaWidgetContentsSrc")
        self.scrollAreaWidgetContentsSrc.setGeometry(QRect(0, 0, 592, 125))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContentsSrc)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollAreaSrc.setWidget(self.scrollAreaWidgetContentsSrc)

        self.gridLayout.addWidget(self.scrollAreaSrc, 12, 0, 1, 1)

        self.imageFrame = QFrame(self.centralwidget)
        self.imageFrame.setObjectName(u"imageFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.imageFrame.sizePolicy().hasHeightForWidth())
        self.imageFrame.setSizePolicy(sizePolicy4)
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.imageFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imagePreview = QLabel(self.imageFrame)
        self.imagePreview.setObjectName(u"imagePreview")
        sizePolicy1.setHeightForWidth(self.imagePreview.sizePolicy().hasHeightForWidth())
        self.imagePreview.setSizePolicy(sizePolicy1)
        self.imagePreview.setMinimumSize(QSize(300, 300))
        font = QFont()
        font.setPointSize(22)
        self.imagePreview.setFont(font)
        self.imagePreview.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.imagePreview, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.imageFrame, 2, 0, 4, 1)

        self.buttonCheckUncheck = QPushButton(self.centralwidget)
        self.buttonCheckUncheck.setObjectName(u"buttonCheckUncheck")

        self.gridLayout.addWidget(self.buttonCheckUncheck, 6, 0, 1, 1)

        self.buttonOutputDir = QPushButton(self.centralwidget)
        self.buttonOutputDir.setObjectName(u"buttonOutputDir")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.buttonOutputDir.sizePolicy().hasHeightForWidth())
        self.buttonOutputDir.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.buttonOutputDir, 6, 6, 1, 1)

        self.buttonInputDir = QPushButton(self.centralwidget)
        self.buttonInputDir.setObjectName(u"buttonInputDir")
        sizePolicy5.setHeightForWidth(self.buttonInputDir.sizePolicy().hasHeightForWidth())
        self.buttonInputDir.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.buttonInputDir, 4, 6, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonClearGenerated.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.labelClusterCount.setText(QCoreApplication.translate("MainWindow", u"Cluster Count", None))
        self.clusterCount.setSuffix("")
        self.clusterCount.setPrefix("")
        self.labelRunCount.setText(QCoreApplication.translate("MainWindow", u"Run count", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Max iterations", None))
        self.buttonGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.imagePreview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.buttonCheckUncheck.setText(QCoreApplication.translate("MainWindow", u"Select/Deselect all", None))
        self.buttonOutputDir.setText(QCoreApplication.translate("MainWindow", u"Load output directory", None))
        self.buttonInputDir.setText(QCoreApplication.translate("MainWindow", u"Load input directory", None))
    # retranslateUi

