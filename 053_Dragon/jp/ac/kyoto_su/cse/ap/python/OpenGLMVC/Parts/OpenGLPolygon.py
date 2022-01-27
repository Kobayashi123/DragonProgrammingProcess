#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.5.3'
__date__ = '2019/07/01 (Created: 2016/11/11)'

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Parts.OpenGLObject import OpenGLObject
# from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLPolygon(OpenGLObject):
	"""
	OpenGL多角形（ポリゴン：Polygon）です。
	"""

	def __init__(self, vertexes, colors=None):
		"""
		OpenGL多角形のインスタンスを生成します。
		"""
		# trace(self)

		super().__init__()
		self._vertexes = vertexes
		self._colors = colors
		self._normal_unit_vector = None

		x = 0.0
		y = 0.0
		z = 0.0
		length = len(vertexes)
		for i in range(0, vertexes):
			j = (i + 1) % length
			k = (i + 2) % length
			map_function = (lambda each1, each2: each1 - each2)
			ux, uy, uz = map(map_function, vertexes[j], vertexes[i])
			vx, vy, vz = map(map_function, vertexes[k], vertexes[j])
			x = x + (uy * vz - uz * vy)
			y = y + (uz * vx - ux * vz)
			z = z + (ux * vy - uy * vx)
		normal_vector = [x, y, z]
		map_function = (lambda each: each * each)
		distance = sum(list(map(map_function, normal_vector))) ** 0.5
		map_function = (lambda vecter: vecter / distance)
		self._normal_unit_vector = list(map(map_function, normal_vector))

	def rendering(self, gl):
		"""
		OpenGL多角形をレンダリングします。
		"""
		# trace(self)

		super().rendering(gl)
		gl.glBegin(gl.GL_POLYGON)
		gl.glNormal3fv(self._normal_unit_vector)
		if self._colors:
			for index, vertex in enumerate(self._vertexes):
				color = self._colors[index]
				if len(color) > 3:
					gl.glColor4f(*color)
				else:
					gl.glColor3f(*color)
				gl.glVertex3fv(vertex)
		else:
			for vertex in self._vertexes:
				gl.glVertex3fv(vertex)
		gl.glEnd()
