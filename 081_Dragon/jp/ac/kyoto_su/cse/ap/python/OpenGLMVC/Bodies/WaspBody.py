#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.8.1'
__date__ = '2019/07/04 (Created: 2016/11/11)'

import os
import urllib.request

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Parts.OpenGLPolygon import OpenGLPolygon
from jp.ac.kyoto_su.cse.ap.python.Trace import trace    # トレース情報出力のための関数です。

class WaspBody:
	"""
	スズメバチ立体です。
	"""

	def __init__(self, model):
		"""
		モデル（OpenGLModel）からスズメバチ立体のインスタンスを生成します。
		"""
		trace(self)

		self._url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/VisualWorks/Wasp/wasp.txt'
		self._model = model

	def make_body(self):
		"""
		モデルに表示物を登録します。
		"""
		trace(self)

		self.read()

	def read(self):
		"""
		スズメバチ立体ファイルのURLよりダウンロードしたファイルから立体を読み込みます。
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
				eye_point_xyz=[-5.5852450791872, 3.07847342734, 15.794105252496], \
				sight_point_xyz=[0.19825005531311, 1.8530999422073, -0.63795006275177], \
				up_vector_xyz=[0.070077999093727, 0.99630606032682, -0.049631725731267], \
				fovy=41.480099231656, \
				axes_scale=4.0, \
				body_name='スズメバチ', \
			)

	def read_all(self, a_file, **dictionary):
		"""
		スズメバチ立体ファイルを読み込んで、モデルに表示物を登録し、プロジェクション情報も登録します。
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
					rgb_color = list(map(float, a_list[index:index+3]))
					a_polygon = OpenGLPolygon(vertexes)
					a_polygon.rgb(*rgb_color)
					self._model.add(a_polygon)
		self.set_projection(**dictionary)

	def set_projection(self, **dictionary):
		"""
		モデルにプロジェクション情報を設定します。
		"""
		trace(self)

		self._model.set_projection(**dictionary)
