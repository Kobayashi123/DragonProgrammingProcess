#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.8.5'
__date__ = '2019/07/04 (Created: 2016/11/11)'

import os
import urllib.request

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Parts.OpenGLTriangle import OpenGLTriangle
from jp.ac.kyoto_su.cse.ap.python.Trace import trace    # トレース情報出力のための関数です。

class BunnyBody:
	"""
	うさぎ立体です。
	"""

	def __init__(self, model):
		"""
		モデル（OpenGLModel）からうさぎ立体のインスタンスを生成します。
		"""
		trace(self)

		self._url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/VisualWorks/Bunny/bunny.ply'
		self._model = model

	def make_body(self):
		"""
		モデルに表示物を登録します。
		"""
		trace(self)

		self.read()

	def read(self):
		"""
		うさぎ立体ファイルのURLよりダウンロードしたファイルから立体を読み込みます。
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
				eye_point_xyz=None, \
				sight_point_xyz=None, \
				up_vector_xyz=None, \
				fovy=None, \
				axes_scale=0.1, \
				body_name='うさぎ', \
			)

	def read_all(self, a_file, **dictionary):
		"""
		うさぎ立体ファイルを読み込んで、モデルに表示物を登録し、プロジェクション情報も登録します。
		"""
		trace(self)

		def comment_processing(a_list):
			first_string = a_list[0]
			if first_string == "comment":
				second_string = a_list[1]
				if second_string == "eye_point_xyz":
					dictionary["eye_point_xyz"] = list(map(float, a_list[2:5]))
				if second_string == "sight_point_xyz":
					dictionary["sight_point_xyz"] = list(map(float, a_list[2:5]))
				if second_string == "up_vector_xyz":
					dictionary["up_vector_xyz"] = list(map(float, a_list[2:5]))
				if second_string == "zoom_height" and a_list[3] == "fovy":
					dictionary["fovy"] = float(a_list[4])

		while True:
			a_string = a_file.readline()
			if not a_string: break
			a_list = a_string.split()
			if not a_list: continue
			first_string = a_list[0]
			if first_string == "element":
				second_string = a_list[1]
				if second_string == "vertex":
					number_of_vertexes = int(a_list[2])
				if second_string == "face":
					number_of_faces = int(a_list[2])
			if first_string == "end_header":
				get_tokens = (lambda file: file.readline().split())
				collection_of_vertexes = []
				for _ in range(number_of_vertexes):
					a_list = get_tokens(a_file)
					a_vertex = list(map(float, a_list[0:3]))
					collection_of_vertexes.append(a_vertex)
				index_to_vertex = (lambda index: collection_of_vertexes[index])
				for _ in range(number_of_faces):
					a_list = get_tokens(a_file)
					indexes = list(map(int, a_list[1:4]))
					vertexes = list(map(index_to_vertex, indexes))
					a_tringle = OpenGLTriangle(*vertexes)
					a_tringle.rgb(1.0, 1.0, 1.0)
					self._model.add(a_tringle)
			comment_processing(a_list)
		self.set_projection(**dictionary)

	def set_projection(self, **dictionary):
		"""
		モデルにプロジェクション情報を設定します。
		"""
		trace(self)

		self._model.set_projection(**dictionary)
