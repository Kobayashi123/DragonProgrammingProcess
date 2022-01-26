#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.3.2'
__date__ = '2019/06/29 (Created: 2016/11/11)'

import sys

from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLController:
	"""
	PyQt5のQOpenGLWidgetを利用した三次元グラフィックス（OpenGL）のコントローラ（Controller of MVC）です。
	"""

	def __init__(self, view):
		"""
		OpenGLControllerのインスタンスを生成します。
		"""
		trace(self)

		self._model = view._model
		self._view = view

	def close(self):
		"""
		ウィンドウを閉じて終了します。
		"""
		trace(self)

		sys.exit(0)
