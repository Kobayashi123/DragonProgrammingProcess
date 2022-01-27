#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.5.1'
__date__ = '2019/07/01 (Created: 2016/11/11)'

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import QGridLayout

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.MVC.OpenGLView import OpenGLView
from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLWindow(QWidget):
	"""
	PyQt5のQOpenGLWidgetを利用した三次元グラフィックス（OpenGL）のモデル・ビュー・コントローラ（MVC：Model-View-Controller）のウィンドウです。
	"""

	def __init__(self, model, application, window_position=None, window_size=(400, 400)):
		"""
		OpenGLのMVC（OpenGL{Model,View,Controller}）を内包するウィンドウを生成します。
		"""
		trace(self)

		super().__init__(parent=None)

		format = QSurfaceFormat()
		format.setDepthBufferSize(24)
		format.setStencilBufferSize(8)
		format.setSamples(4)
		QSurfaceFormat.setDefaultFormat(format)

		self._model = model
		self._view = OpenGLView(self._model, width=window_size[0], height=window_size[1], parent=self)
		self._controller = self._view._controller

		main_layout = QGridLayout()
		main_layout.setContentsMargins(0, 0, 0, 0)
		main_layout.addWidget(self._view)

		self.setLayout(main_layout)
		self.setMinimumSize(200, 200)
		self.setMaximumSize(800, 800)
		self.resize(*window_size)

		window_label = 'OpenGL Window'
		if self._model._body_name:
			window_label = window_label + '[' + self._model._body_name + ']'
		self.setWindowTitle(window_label)

		if window_position:
			self.move(*window_position)
		else:
			screen_center = application.primaryScreen().availableGeometry().center()
			window_center = self.window_center()
			self.move(screen_center - window_center)

	def keyPressEvent(self, event):
		"""
		キーが押された際にコントローラに通知します。
		"""
		trace(self)

		self._controller.keyboard(event)

	def window_center(self):
		"""
		ウィンドウの中心を応答します。つまり、ウィンドウの半分の大きさをQPointにして応答します。
		"""
		trace(self)

		x = self.window_width() / 2
		y = self.window_height() / 2
		return QPoint(x, y)

	def window_height(self):
		"""
		ウィンドウの高さを応答します。
		"""
		trace(self)

		return self.height()

	def window_width(self):
		"""
		ウィンドウの幅を応答します。
		"""
		trace(self)

		return self.width()
