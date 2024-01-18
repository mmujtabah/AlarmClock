# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(600, 400)
        Widget.setStyleSheet(u"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #232430;\n"
"	color: #000000;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: #232430;\n"
"	color: #c1c1c1;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #ff9c2b;\n"
"	color: #000000;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-color: #000000;\n"
"	padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"	background-color: #ff9c2b;\n"
"	color: #000000;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-color: #000000;\n"
"	padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	backgroun"
                        "d-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #38394e;\n"
"	color: #c1c1c1;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #4a4c68;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView-----*/\n"
"QTableView, \n"
"QHeaderView, \n"
"QTableView::item \n"
"{\n"
"	background-color: #232430;\n"
"	color: #c1c1c1;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{ \n"
"    background-color: #41424e;\n"
"    color: #c1c1c1;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal \n"
"{\n"
"    background-color: #232430;\n"
"	border: 1px solid #37384d;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator{\n"
"	background-color: #1d1d28;\n"
"	border: 1px solid #37384d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator:checked{\n"
"	image:url(\"./ressources/check.png\"); /*To replace*/\n"
"	background-color: #1d1d28;\n"
"\n"
"}\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabWidget::pane \n"
"{ \n"
"    border: none;"
                        "\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar \n"
"{\n"
"    left: 5px; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab \n"
"{\n"
"    color: #c1c1c1;\n"
"    min-width: 1px;\n"
"	padding-left: 25px;\n"
"	margin-left:-22px;\n"
"    height: 28px;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected \n"
"{\n"
"    color: #c1c1c1;\n"
"	font-weight: bold;\n"
"    height: 28px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!first \n"
"{\n"
"    margin-left: -20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover \n"
"{\n"
"    color: #DDD;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"	min-width: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizo"
                        "ntal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"	min-height: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}")
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 160, 207, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hourcomboBox = QComboBox(self.horizontalLayoutWidget)
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.addItem("")
        self.hourcomboBox.setObjectName(u"hourcomboBox")
        self.hourcomboBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.hourcomboBox)

        self.mincomboBox = QComboBox(self.horizontalLayoutWidget)
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.addItem("")
        self.mincomboBox.setObjectName(u"mincomboBox")
        self.mincomboBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.mincomboBox)

        self.setButton = QPushButton(Widget)
        self.setButton.setObjectName(u"setButton")
        self.setButton.setGeometry(QRect(100, 260, 80, 24))
        self.setButton.setStyleSheet(u"QPushButton#setButton:hover {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
" }")
        self.labelTime = QLabel(Widget)
        self.labelTime.setObjectName(u"labelTime")
        self.labelTime.setGeometry(QRect(40, 80, 221, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.labelTime.setFont(font)
        self.listWidget = QListWidget(Widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(320, 110, 256, 192))
        self.listWidget.setStyleSheet(u"border: 2px solid;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 156, 43);")
        self.removeButton = QPushButton(Widget)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(400, 310, 80, 24))
        self.removeButton.setStyleSheet(u"QPushButton#removeButton:hover {\n"
"		\n"
"	background-color: rgb(255, 255, 255);\n"
" }")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.hourcomboBox.setItemText(0, QCoreApplication.translate("Widget", u"00", None))
        self.hourcomboBox.setItemText(1, QCoreApplication.translate("Widget", u"01", None))
        self.hourcomboBox.setItemText(2, QCoreApplication.translate("Widget", u"02", None))
        self.hourcomboBox.setItemText(3, QCoreApplication.translate("Widget", u"03", None))
        self.hourcomboBox.setItemText(4, QCoreApplication.translate("Widget", u"04", None))
        self.hourcomboBox.setItemText(5, QCoreApplication.translate("Widget", u"05", None))
        self.hourcomboBox.setItemText(6, QCoreApplication.translate("Widget", u"06", None))
        self.hourcomboBox.setItemText(7, QCoreApplication.translate("Widget", u"07", None))
        self.hourcomboBox.setItemText(8, QCoreApplication.translate("Widget", u"08", None))
        self.hourcomboBox.setItemText(9, QCoreApplication.translate("Widget", u"09", None))
        self.hourcomboBox.setItemText(10, QCoreApplication.translate("Widget", u"10", None))
        self.hourcomboBox.setItemText(11, QCoreApplication.translate("Widget", u"11", None))
        self.hourcomboBox.setItemText(12, QCoreApplication.translate("Widget", u"12", None))
        self.hourcomboBox.setItemText(13, QCoreApplication.translate("Widget", u"13", None))
        self.hourcomboBox.setItemText(14, QCoreApplication.translate("Widget", u"14", None))
        self.hourcomboBox.setItemText(15, QCoreApplication.translate("Widget", u"15", None))
        self.hourcomboBox.setItemText(16, QCoreApplication.translate("Widget", u"16", None))
        self.hourcomboBox.setItemText(17, QCoreApplication.translate("Widget", u"17", None))
        self.hourcomboBox.setItemText(18, QCoreApplication.translate("Widget", u"18", None))
        self.hourcomboBox.setItemText(19, QCoreApplication.translate("Widget", u"19", None))
        self.hourcomboBox.setItemText(20, QCoreApplication.translate("Widget", u"20", None))
        self.hourcomboBox.setItemText(21, QCoreApplication.translate("Widget", u"21", None))
        self.hourcomboBox.setItemText(22, QCoreApplication.translate("Widget", u"22", None))
        self.hourcomboBox.setItemText(23, QCoreApplication.translate("Widget", u"23", None))

        self.mincomboBox.setItemText(0, QCoreApplication.translate("Widget", u"00", None))
        self.mincomboBox.setItemText(1, QCoreApplication.translate("Widget", u"01", None))
        self.mincomboBox.setItemText(2, QCoreApplication.translate("Widget", u"02", None))
        self.mincomboBox.setItemText(3, QCoreApplication.translate("Widget", u"03", None))
        self.mincomboBox.setItemText(4, QCoreApplication.translate("Widget", u"04", None))
        self.mincomboBox.setItemText(5, QCoreApplication.translate("Widget", u"05", None))
        self.mincomboBox.setItemText(6, QCoreApplication.translate("Widget", u"06", None))
        self.mincomboBox.setItemText(7, QCoreApplication.translate("Widget", u"07", None))
        self.mincomboBox.setItemText(8, QCoreApplication.translate("Widget", u"09", None))
        self.mincomboBox.setItemText(9, QCoreApplication.translate("Widget", u"10", None))
        self.mincomboBox.setItemText(10, QCoreApplication.translate("Widget", u"11", None))
        self.mincomboBox.setItemText(11, QCoreApplication.translate("Widget", u"12", None))
        self.mincomboBox.setItemText(12, QCoreApplication.translate("Widget", u"13", None))
        self.mincomboBox.setItemText(13, QCoreApplication.translate("Widget", u"14", None))
        self.mincomboBox.setItemText(14, QCoreApplication.translate("Widget", u"15", None))
        self.mincomboBox.setItemText(15, QCoreApplication.translate("Widget", u"16", None))
        self.mincomboBox.setItemText(16, QCoreApplication.translate("Widget", u"17", None))
        self.mincomboBox.setItemText(17, QCoreApplication.translate("Widget", u"18", None))
        self.mincomboBox.setItemText(18, QCoreApplication.translate("Widget", u"19", None))
        self.mincomboBox.setItemText(19, QCoreApplication.translate("Widget", u"20", None))
        self.mincomboBox.setItemText(20, QCoreApplication.translate("Widget", u"21", None))
        self.mincomboBox.setItemText(21, QCoreApplication.translate("Widget", u"22", None))
        self.mincomboBox.setItemText(22, QCoreApplication.translate("Widget", u"23", None))
        self.mincomboBox.setItemText(23, QCoreApplication.translate("Widget", u"24", None))
        self.mincomboBox.setItemText(24, QCoreApplication.translate("Widget", u"25", None))
        self.mincomboBox.setItemText(25, QCoreApplication.translate("Widget", u"26", None))
        self.mincomboBox.setItemText(26, QCoreApplication.translate("Widget", u"27", None))
        self.mincomboBox.setItemText(27, QCoreApplication.translate("Widget", u"28", None))
        self.mincomboBox.setItemText(28, QCoreApplication.translate("Widget", u"29", None))
        self.mincomboBox.setItemText(29, QCoreApplication.translate("Widget", u"30", None))
        self.mincomboBox.setItemText(30, QCoreApplication.translate("Widget", u"31", None))
        self.mincomboBox.setItemText(31, QCoreApplication.translate("Widget", u"32", None))
        self.mincomboBox.setItemText(32, QCoreApplication.translate("Widget", u"33", None))
        self.mincomboBox.setItemText(33, QCoreApplication.translate("Widget", u"34", None))
        self.mincomboBox.setItemText(34, QCoreApplication.translate("Widget", u"35", None))
        self.mincomboBox.setItemText(35, QCoreApplication.translate("Widget", u"36", None))
        self.mincomboBox.setItemText(36, QCoreApplication.translate("Widget", u"37", None))
        self.mincomboBox.setItemText(37, QCoreApplication.translate("Widget", u"38", None))
        self.mincomboBox.setItemText(38, QCoreApplication.translate("Widget", u"39", None))
        self.mincomboBox.setItemText(39, QCoreApplication.translate("Widget", u"40", None))
        self.mincomboBox.setItemText(40, QCoreApplication.translate("Widget", u"41", None))
        self.mincomboBox.setItemText(41, QCoreApplication.translate("Widget", u"42", None))
        self.mincomboBox.setItemText(42, QCoreApplication.translate("Widget", u"43", None))
        self.mincomboBox.setItemText(43, QCoreApplication.translate("Widget", u"44", None))
        self.mincomboBox.setItemText(44, QCoreApplication.translate("Widget", u"45", None))
        self.mincomboBox.setItemText(45, QCoreApplication.translate("Widget", u"46", None))
        self.mincomboBox.setItemText(46, QCoreApplication.translate("Widget", u"47", None))
        self.mincomboBox.setItemText(47, QCoreApplication.translate("Widget", u"48", None))
        self.mincomboBox.setItemText(48, QCoreApplication.translate("Widget", u"49", None))
        self.mincomboBox.setItemText(49, QCoreApplication.translate("Widget", u"50", None))
        self.mincomboBox.setItemText(50, QCoreApplication.translate("Widget", u"51", None))
        self.mincomboBox.setItemText(51, QCoreApplication.translate("Widget", u"52", None))
        self.mincomboBox.setItemText(52, QCoreApplication.translate("Widget", u"53", None))
        self.mincomboBox.setItemText(53, QCoreApplication.translate("Widget", u"54", None))
        self.mincomboBox.setItemText(54, QCoreApplication.translate("Widget", u"55", None))
        self.mincomboBox.setItemText(55, QCoreApplication.translate("Widget", u"56", None))
        self.mincomboBox.setItemText(56, QCoreApplication.translate("Widget", u"57", None))
        self.mincomboBox.setItemText(57, QCoreApplication.translate("Widget", u"58", None))
        self.mincomboBox.setItemText(58, QCoreApplication.translate("Widget", u"59", None))

        self.setButton.setText(QCoreApplication.translate("Widget", u"SET", None))
        self.labelTime.setText(QCoreApplication.translate("Widget", u"Current Time", None))
        self.removeButton.setText(QCoreApplication.translate("Widget", u"Remove", None))
    # retranslateUi

