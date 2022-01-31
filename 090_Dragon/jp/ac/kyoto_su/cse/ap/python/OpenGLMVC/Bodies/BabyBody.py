#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.9.0'
__date__ = '2019/07/05 (Created: 2016/11/11)'

import os
import urllib.request

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Parts.OpenGLPolygon import OpenGLPolygon
from jp.ac.kyoto_su.cse.ap.python.Trace import trace    # トレース情報出力のための関数です。

class BabyBody:
	"""
	赤ちゃん立体です。
	"""

	def __init__(self, model):
		"""
		モデル（OpenGLModel）から赤ちゃん立体のインスタンスを生成します。
		"""
		trace(self)

		self._url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/VisualWorks/Baby/baby.txt'
		self._model = model

	def make_body(self):
		"""
		モデルに表示物を登録します。
		"""
		trace(self)

		self.read()

	def read(self):
		"""
		赤ちゃん立体ファイルのURLよりダウンロードしたファイルから立体を読み込みます。
		"""
		trace(self)

		a_list = self._url.split('/')
		a_directory = os.path.join(os.getcwd(), 'bodies')
		if not os.path.exists(a_directory): os.mkdir(a_directory)

		a_file = os.path.join(a_directory, a_list[-1])
		if not (os.path.exists(a_file) and os.path.isfile(a_file)):
			urllib.request.urlretrieve(self._url, a_file)

		with open(a_file, "r", encoding='utf-8') as a_file:
			self.read_all(a_file, \
				number_of_vertexes=None, \
				number_of_triangles=None, \
				eye_point_xyz=[-6.6153435525924, 3.5413918991617, 27.440373330962], \
				sight_point_xyz=[0.0, 0.14168989658356, 0.18842494487762], \
				up_vector_xyz=[0.03835909829153, 0.99323407243554, -0.10961139051838], \
				fovy=13.079457895221, \
				axes_scale=1.8, \
				body_name='赤ちゃん', \
			)

	def read_all(self, a_file, **dictionary):
		"""
		赤ちゃん立体ファイルを読み込んで、モデルに表示物を登録し、プロジェクション情報も登録します。
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
			if first_string == "number_of_polygons":
				number_of_polygons = int(a_list[1])
			if first_string == "number_of_colors":
				number_of_colors = int(a_list[1])
			if first_string == "end_header":
				get_tokens = (lambda file: file.readline().split())
				collection_of_vertexes = []
				for _ in range(number_of_vertexes):
					a_list = get_tokens(a_file)
					a_vertex = list(map(float, a_list[0:3]))
					collection_of_vertexes.append(a_vertex)
				index_to_vertex = (lambda index: collection_of_vertexes[index-1])
				for _ in range(number_of_polygons):
					a_list = get_tokens(a_file)
					number_of_indexes = int(a_list[0])
					index = number_of_indexes + 1
					indexes = list(map(int, a_list[1:index]))
					vertexes = list(map(index_to_vertex, indexes))
					a_polygon = OpenGLPolygon(vertexes)
					self._model.add(a_polygon)
				collection_of_colors = []
				for _ in range(number_of_colors):
					a_list = get_tokens(a_file)
					rgb_color = list(map(float, a_list[0:3]))
					collection_of_colors.append(rgb_color)
				for n_th in range(number_of_polygons):
					a_list = get_tokens(a_file)
					index = int(a_list[0])
					rgb_color = collection_of_colors[index - 1]
					a_polygon = self._model._objects[n_th]
					a_polygon.rgb(*rgb_color)
		self.set_projection(**dictionary)

	def set_projection(self, **dictionary):
		"""
		モデルにプロジェクション情報を設定します。
		"""
		trace(self)

		self._model.set_projection(**dictionary)
