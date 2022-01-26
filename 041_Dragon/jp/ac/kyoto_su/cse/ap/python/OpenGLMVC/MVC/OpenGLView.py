#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.4.1'
__date__ = '2019/06/30 (Created: 2016/11/11)'

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QOpenGLVersionProfile
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
		self._gl = None

	def initializeGL(self):
		"""
		OpenGLの初期化を行います。
		"""
		trace(self)

		version = QOpenGLVersionProfile()
		version.setVersion(2, 1)

		self._gl = self.context().versionFunctions(version)
		self._gl.initializeGLFunctions()

		gl = self._gl
		gl.glEnable(gl.GL_COLOR_MATERIAL)
		gl.glEnable(gl.GL_DEPTH_TEST)
		gl.glEnable(gl.GL_CULL_FACE)
		gl.glEnable(gl.GL_NORMALIZE)
		gl.glShadeModel(gl.GL_SMOOTH)

		gl.glClearColor(0.9, 0.9, 0.9, 1.0)    # Red, Green, Blue, Alpha

	def paintGL(self):
		"""
		OpenGLViewの中を描きます。
		"""
		trace(self)

		gl = self._gl

		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

	def resizeGL(self, width, height):
		"""
		OpenGLViewの大きさが変更された際に、OpenGLのビューポートを再形成します。
		"""
		trace(self)

		self._width = width
		self._height = height
		extent = min(width, height)
		x = (width - extent) // 2
		y = (height - extent) // 2
		w = extent
		h = extent
		self._gl.glViewport(x, y, w, h)

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
