#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.9.0'
__date__ = '2019/07/05 (Created: 2016/11/11)'

# from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLObject:
	"""
	OpenGLオブジェクトです。
	"""

	def __init__(self):
		"""
		OpenGLオブジェクトのインスタンスを生成します。
		"""
		# trace(self)

		self._rgba = [1.0,] * 4    # デフォルトの色は白(red=1.0, green=1.0, blue=1.0, alpha=1.0)

	def rendering(self, gl):
		"""
		OpenGLオブジェクトをレンダリングします。
		"""
		# trace(self)

		gl.glColor4f(self._rgba[0], self._rgba[1], self._rgba[2], self._rgba[3])

	def rgb(self, red, green, blue):
		"""
		OpenGLオブジェクトの色(RGB)を設定します。
		"""
		# trace(self)

		self.rgba(red, green, blue, 1.0)

	def rgba(self, red, green, blue, alpha):
		"""
		OpenGLオブジェクトの色(RGBA)を設定します。
		"""
		# trace(self)

		self._rgba = [red, green, blue, alpha]
