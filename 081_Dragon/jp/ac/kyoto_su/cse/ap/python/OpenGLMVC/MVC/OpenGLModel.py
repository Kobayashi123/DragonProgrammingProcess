#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.8.0'
__date__ = '2019/07/04 (Created: 2016/11/11)'

from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLModel:
	"""
	PyQt5のQOpenGLWidgetを利用した三次元グラフィックス（OpenGL）のモデル（Model of MVC）です。
	"""

	def __init__(self):
		"""
		OpenGLModelのインスタンスを生成します。
		"""
		trace(self)

		self._objects = []
		self._eye_point = [-5.58, 3.07, 15.79]
		self._sight_point = [0.0, 0.0, 0.0]
		self._up_vector = [0.10, 0.98, -0.14]
		self._fovy = self._default_fovy = 12.64
		self._axes_scale = 1.0
		self._body_name = None
		self._display_list = -1

	def add(self, object):
		"""
		OpenGLModelの表示物にレンダリングできる物を入れます。
		"""
		# trace(self)

		self._objects.append(object)

	def add_all(self, objects):
		"""
		OpenGLModelの表示物に複数のレンダリングできる物たちを入れます。
		"""
		# trace(self)

		for object in objects:
			self.add(object)

	def rendering(self, gl):
		"""
		OpenGLModelをレンダリングします。
		"""
		trace(self)

		if self._display_list == -1:
			self._display_list = gl.glGenLists(1)
			gl.glNewList(self._display_list, gl.GL_COMPILE)
			for object in self._objects:
				object.rendering(gl)
			gl.glEndList()
		gl.glCallList(self._display_list)

	def set_projection(self, **dictionary):
		"""
		プロジェクション情報を設定します。
		"""
		trace(self)

		key = 'eye_point_xyz'
		if key in dictionary: self._eye_point = dictionary[key]
		key = 'sight_point_xyz'
		if key in dictionary: self._sight_point = dictionary[key]
		key = 'up_vector_xyz'
		if key in dictionary: self._up_vector = dictionary[key]
		key = 'fovy'
		if key in dictionary: self._fovy = self._default_fovy = dictionary[key]
		key = 'axes_scale'
		if key in dictionary: self._axes_scale = dictionary[key]
		key = 'body_name'
		if key in dictionary: self._body_name = dictionary[key]
