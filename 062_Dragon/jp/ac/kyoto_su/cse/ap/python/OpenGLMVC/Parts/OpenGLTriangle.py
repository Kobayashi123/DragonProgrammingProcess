#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.6.1'
__date__ = '2019/07/02 (Created: 2016/11/11)'

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Parts.OpenGLObject import OpenGLObject
# from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLTriangle(OpenGLObject):
	"""
	OpenGL三角形（トライアングル：Triangle）です。
	"""

	def __init__(self, vertex1, vertex2, vertex3):
		"""
		OpenGL三角形のインスタンスを生成します。
		"""
		# trace(self)

		super().__init__()
		self._vertex1 = vertex1
		self._vertex2 = vertex2
		self._vertex3 = vertex3

		# 法線ベクトル（単位ベクトル）を計算（右手系で算出）
		map_function = (lambda value1, value0: value1 - value0)
		ux, uy, uz = list(map(map_function, vertex2, vertex1))
		vx, vy, vz = list(map(map_function, vertex3, vertex1))
		normal_vector = [(uy * vz - uz * vy), (uz * vx - ux * vz), (ux * vy - uy * vx)]
		map_function = (lambda value: value * value)
		distance = sum(list(map(map_function, normal_vector))) ** 0.5
		map_function = (lambda vector: vector / distance)
		self._normal_unit_vector = list(map(map_function, normal_vector))

	def rendering(self, gl):
		"""
		OpenGL三角形をレンダリングします。
		"""
		# trace(self)

		super().rendering(gl)
		gl.glBegin(gl.GL_TRIANGLES)
		gl.glNormal3fv(self._normal_unit_vector)
		gl.glVertex3fv(self._vertex1)
		gl.glVertex3fv(self._vertex2)
		gl.glVertex3fv(self._vertex3)
		gl.glEnd()
