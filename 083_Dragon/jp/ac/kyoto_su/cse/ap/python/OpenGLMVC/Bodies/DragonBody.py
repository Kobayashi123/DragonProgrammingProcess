#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.8.2'
__date__ = '2019/07/04 (Created: 2016/11/11)'

import os
import urllib.request

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Parts.OpenGLTriangle import OpenGLTriangle
from jp.ac.kyoto_su.cse.ap.python.Trace import trace    # トレース情報出力のための関数です。

class DragonBody:
	"""
	ドラゴン立体です。
	"""

	def __init__(self, model):
		"""
		モデル（OpenGLModel）からドラゴン立体のインスタンスを生成します。
		"""
		trace(self)

		self._url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/VisualWorks/Dragon/dragon.txt'
		self._model = model

	def make_body(self):
		"""
		モデルに表示物を登録します。
		"""
		trace(self)

		self.read()

	def read(self):
		"""
		ドラゴン立体ファイルのURLよりダウンロードしたファイルから立体を読み込みます。
		"""
		trace(self)

		a_list = self._url.split('/')
		a_directory = os.path.join(os.getcwd(), 'bodies')
		if not os.path.exists(a_directory): os.mkdir(a_directory)

		a_file = os.path.join(a_directory, a_list[-1])
		if not (os.path.exists(a_file) and os.path.isfile(a_file)):
			urllib.request.urlretrieve(self._url, a_file)

		with open(a_file, "r", encoding = 'utf-8') as a_file:
			self.read_all(a_file, \
				number_of_vertexes=None, \
				number_of_triangles=None, \
				eye_point_xyz=[-5.5852450791872, 3.07847342734, 15.794105252496], \
				sight_point_xyz=[0.27455347776413, 0.20096999406815, -0.11261999607086], \
				up_vector_xyz=[0.1018574904194, 0.98480906061847, -0.14062775604137], \
				fovy=12.642721790235, \
				axes_scale=1.0, \
				body_name='ドラゴン', \
			)

	def read_all(self, a_file, **dictionary):
		"""
		ドラゴン立体ファイルを読み込んで、モデルに表示物を登録し、プロジェクション情報も登録します。
		"""
		trace(self)

		while True:
			a_string = a_file.readline()
			if not a_string: break
			a_list = a_string.split()
			if not a_list: continue
			first_string = a_list[0]
			if first_string == "number_of_vertexes":
				number_of_vertexes = int(a_list[1])
			if first_string == "number_of_triangles":
				number_of_triangles = int(a_list[1])
			if first_string == "end_header":
				get_tokens = (lambda file: file.readline().split())
				collection_of_vertexes = []
				for _ in range(number_of_vertexes):
					a_list = get_tokens(a_file)
					a_vertex = list(map(float, a_list[0:3]))
					collection_of_vertexes.append(a_vertex)
				index_to_vertex = (lambda index: collection_of_vertexes[index-1])
				for _ in range(number_of_triangles):
					a_list = get_tokens(a_file)
					indexes = list(map(int, a_list[0:3]))
					vertexes = list(map(index_to_vertex, indexes))
					a_triangle = OpenGLTriangle(*vertexes)
					a_triangle.rgb(0.8, 0.1, 0.1)
					self._model.add(a_triangle)
		self.set_projection(**dictionary)

	def set_projection(self, **dictionary):
		"""
		モデルにプロジェクション情報を設定します。
		"""
		trace(self)

		self._model.set_projection(**dictionary)
