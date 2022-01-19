#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.2.0'
__date__ = '2019/06/28 (Created: 2016/11/11)'

from PyQt5.QtWidgets import QWidget

from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLWindow(QWidget):
	"""
	PyQt5のQOpenGLWidgetを利用した三次元グラフィックス（OpenGL）のモデル・ビュー・コントローラ（MVC：Model-View-Controller）のウィンドウです。
	"""

	def __init__(self, application, window_position=None, window_size=(400, 400)):
		"""
		OpenGLのMVC（OpenGL{Model,View,Controller}）を内包するウィンドウを生成します。
		"""
		trace(self)

		super().__init__(parent=None)

		self.setMinimumSize(200, 200)
		self.setMaximumSize(800, 800)
		self.resize(*window_size)

		window_label = 'OpenGL Window'
		self.setWindowTitle(window_label)

		# ここでウィンドウの表示位置を決めます。
		(lambda x: x)(application)
		(lambda x: x)(window_position)
