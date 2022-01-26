#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.4.0'
__date__ = '2019/06/30 (Created: 2016/11/11)'

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QOpenGLWidget

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.MVC.OpenGLController import OpenGLController
from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLView(QOpenGLWidget):
	"""
	PyQt5のQOpenGLWidgetを利用した三次元グラフィックス（OpenGL）のビュー（View of MVC）です。
	"""

	def __init__(self, model, width=400, height=400, parent=None):
		"""
		OpenGLViewのインスタンスを生成します。
		"""
		trace(self)

		super().__init__(parent)
		self._model = model
		self._controller = OpenGLController(self)
		self._width = width
		self._height = height

	def sizeHint(self):
		"""
		OpenGLViewの大きさを応答します。
		"""
		trace(self)

		return QSize(self._width, self._height)

	def mouseMoveEvent(self, event):
		"""
		マウスが移動した際にコントローラに通知します。
		"""
		self._controller.motion(event)

	def mousePressEvent(self, event):
		"""
		マウスボタンが押された際にコントローラに通知します。
		"""
		self._controller.mouse(event)
