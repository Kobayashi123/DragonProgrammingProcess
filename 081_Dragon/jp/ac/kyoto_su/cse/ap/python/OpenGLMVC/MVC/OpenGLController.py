#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.8.1'
__date__ = '2019/07/03 (Created: 2016/11/11)'

import sys

from PyQt5.QtCore import Qt
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

		def function_q():
			"""ウィンドウをクローズします。"""
			trace(function_q)
			self.close()
		def function_r():
			"""視界をリセットします。"""
			trace(function_r)
			self._view._angle_x = 0.0
			self._view._angle_y = 0.0
			self._view._angle_z = 0.0
			self._model._fovy = self._model._default_fovy
		def function_x():
			"""X軸のまわりに正方向に回転をします。"""
			trace(function_x)
			self._view._angle_x = (self._view._angle_x + 1.0) % 360.0
		def function_X():
			"""X軸のまわりに負方向に回転をします。"""
			trace(function_X)
			self._view._angle_x = (self._view._angle_x - 1.0) % 360.0
		def function_y():
			"""Y軸のまわりに正方向に回転をします。"""
			trace(function_y)
			self._view._angle_y = (self._view._angle_y + 1.0) % 360.0
		def function_Y():
			"""Y軸のまわりに負方向に回転をします。"""
			trace(function_Y)
			self._view._angle_y = (self._view._angle_y - 1.0) % 360.0
		def function_z():
			"""Z軸のまわりに正方向に回転をします。"""
			trace(function_z)
			self._view._angle_z = (self._view._angle_z + 1.0) % 360.0
		def function_Z():
			"""Z軸のまわりに正方向に回転をします。"""
			trace(function_Z)
			self._view._angle_z = (self._view._angle_z - 1.0) % 360.0
		def function_s():
			"""視野角を広げて視界を大きくすることでズームアウト（縮小）します。"""
			trace(function_s)
			self._model._fovy = min(max(self._model._fovy + 1.0, 1.0), 45.0)
		def function_S():
			"""視野角を広げて視界を小さくすることでズームイン（拡大）します。"""
			trace(function_S)
			self._model._fovy = min(max(self._model._fovy - 1.0, 1.0), 45.0)
		self._function_dictionary = { \
			'q': function_q, 'Q': function_q, \
			'r': function_r, 'R': function_r, \
			'x': function_x, 'X': function_X, \
			'y': function_y, 'Y': function_Y, \
			'z': function_z, 'Z': function_Z, \
			's': function_s, 'S': function_S, \
			}
		self._mouse_pressed_x = None
		self._mouse_pressed_y = None

	def close(self):
		"""
		ウィンドウを閉じて終了します。
		"""
		trace(self)

		sys.exit(0)

	def keyboard(self, event):
		"""
		キーボードが押されたときの処理をします。
		"""
		trace(self)

		key = event.key()
		if key == Qt.Key_Escape: self.close()
		text = event.text()
		if text == '' or text not in self._function_dictionary: return
		self._function_dictionary[text]()
		self._view.update()

	def motion(self, event):
		"""
		マウスの左ボタンを押しながらの移動を処理します。
		"""
		trace(self)

		button = event.button()
		if button in (Qt.LeftButton, Qt.NoButton):
			position = event.pos()
			position_x = position.x()
			position_y = position.y()
			amount_x = position_x - self._mouse_pressed_x
			amount_y = self._mouse_pressed_y - position_y
			self._view.rotate_xy(amount_x, amount_y)
			self._mouse_pressed_x = position_x
			self._mouse_pressed_y = position_y
			self._view.update()

	def mouse(self, event):
		"""
		マウスの左ボタンが押されたときの処理をします。
		"""
		trace(self)

		button = event.button()
		if button == Qt.LeftButton:
			position = event.pos()
			position_x = position.x()
			position_y = position.y()
			self._mouse_pressed_x = position_x
			self._mouse_pressed_y = position_y
