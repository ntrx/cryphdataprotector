#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import sys
import uie

if __name__ == "__main__":
	app = uie.QtGui.QApplication(sys.argv)
	form = uie.Ui_MainWindow()
	form.show()
	sys.exit(app.exec_())
