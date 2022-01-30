#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.9.0'
__date__ = '2019/07/05 (Created: 2016/11/11)'

import sys

from PyQt5.QtWidgets import QApplication

# from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Bodies.DragonBody import DragonBody
# from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Bodies.WaspBody import WaspBody
# from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Bodies.BunnyBody import BunnyBody
# from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Bodies.PenguinBody import PenguinBody
# from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Bodies.OniBody import OniBody
# from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Bodies.BabyBody import BabyBody
from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.MVC.OpenGLModel import OpenGLModel
from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.OpenGLWindow import OpenGLWindow
from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Parts.OpenGLPolygon import OpenGLPolygon
from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.Parts.OpenGLTriangle import OpenGLTriangle
from jp.ac.kyoto_su.cse.ap.python.Trace import Trace    # トレース情報出力のON/OFFに用います。
from jp.ac.kyoto_su.cse.ap.python.Trace import trace    # トレース情報出力のための関数です。

class SampleBody:
	"""
	サンプル立体です。
	"""

	def __init__(self, model):
		"""
		モデル（OpenGLModel）からサンプル立体のインスタンスを生成します。
		"""
		trace(self)

		self._model = model

	def make_body(self):
		"""
		モデルに表示物を登録します。
		"""
		trace(self)

		self.make_gray_triangle()
		self.make_color_cube()
		self.set_projection( \
			eye_point_xyz=[-5.5852450791872, 3.07847342734, 15.794105252496], \
			sight_point_xyz=[0.0, 0.0, 0.0], \
			up_vector_xyz=[0.1018574904194, 0.98480906061847, -0.14062775604137], \
			fovy=12.642721790235, \
			axes_scale=1.0, \
			body_name='サンプル', \
		)

	def make_color_cube(self):
		"""
		モデルの表示物にカラーキューブ（色方体：六面体）を入れます。
		"""
		trace(self)

		surfaces = []
		# 第一番：Z=1の面（法線ベクトル+Zの四角形）：青〜マゼンタ〜白〜シアン
		surfaces.append([(0.0, 0.0, 1.0), (1.0, 0.0, 1.0), (1.0, 1.0, 1.0), (0.0, 1.0, 1.0)])
		# 第ニ番：Z=0の面（法線ベクトル-Zの四角形）：緑〜黄〜赤〜黒
		surfaces.append([(0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 0.0, 0.0)])
		# 第三番：X=1の面（法線ベクトル+Xの四角形）：赤〜黄〜白〜マゼンタ
		surfaces.append([(1.0, 0.0, 0.0), (1.0, 1.0, 0.0), (1.0, 1.0, 1.0), (1.0, 0.0, 1.0)])
		# 第四番：X=0の面（法線ベクトル-Xの四角形）：青〜シアン〜緑〜黒
		surfaces.append([(0.0, 0.0, 1.0), (0.0, 1.0, 1.0), (0.0, 1.0, 0.0), (0.0, 0.0, 0.0)])
		# 第五番：Y=1の面（法線ベクトル+Yの四角形）：シアン〜白〜黄〜緑
		surfaces.append([(0.0, 1.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 0.0), (0.0, 1.0, 0.0)])
		# 第六番：Y=0の面（法線ベクトル-Yの四角形）：黒〜赤〜マゼンタ〜青
		surfaces.append([(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (1.0, 0.0, 1.0), (0.0, 0.0, 1.0)])
		# ポリゴン六個でカラーキューブ（色方体：六面体）
		polygons = []
		for surface in surfaces:
			polygon = OpenGLPolygon(vertexes=surface, colors=surface)
			polygons.append(polygon)
			# 色方体の六面を追加
			self._model.add_all(polygons)

	def make_gray_triangle(self):
		"""
		モデルの表示物にグレーの三角形（明暗の表裏）を入れます。
		"""
		trace(self)

		surfaces = []
		# 三角形の表面（おもて：法線ベクトル+Z）：明るいグレー
		surfaces.append([(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (-1.0, 0.0, 0.0), (0.75, 0.75, 0.75)])
		# 三角形の裏面（うら：法線ベクトル-Z）：暗いグレー
		surfaces.append([(0.0, 0.0, 0.0), (-1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.25, 0.25, 0.25)])
		# 三角形二つで三角形の表裏
		triangles = []
		for surface in surfaces:
			triangle = OpenGLTriangle(*surface[:3])
			triangle.rgb(*surface[3])
			triangles.append(triangle)
		# 三角形の表裏の両方を追加
		self._model.add_all(triangles)

	def set_projection(self, **dictionary):
		"""
		モデルにプロジェクション情報を設定します。
		"""
		trace(self)

		self._model.set_projection(**dictionary)

def main():
	"""
	PyQt5のQOpenGLWidgetを利用した三次元グラフィックス（OpenGL）のモデル・ビュー・コントローラ（MVC：Model-View-Controller）の例題（メイン・プログラム）です。
	常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
	"""
	# Trace.trace_off()
	Trace.trace_on()
	trace(main)

	# OpenGLのモデルのインスタンスを生成します。
	model = OpenGLModel()
	sample = SampleBody(model)
	sample.make_body()
	# ドラゴン立体のインスタンスを生成し、モデルに表示物を登録します。
	# dragon = DragonBody(model)
	# dragon.make_body()

	# スズメバチ立体のインスタンスを生成し、モデルに表示物を登録します。
	# wasp = WaspBody(model)
	# wasp.make_body()

	# うさぎ立体のインスタンスを生成し、モデルに表示物を登録します。
	# bunny = BunnyBody(model)
	# bunny.make_body()

	# ペンギン立体のインスタンスを生成し、モデルに表示物を登録します。
	# penguin = PenguinBody(model)
	# penguin.make_body()

	# 鬼立体のインスタンスを生成し、モデルに表示物を登録します。
	# oni = OniBody(model)
	# oni.make_body()

	# 赤ちゃん立体のインスタンスを生成し、モデルに表示物を登録します。
	# baby = BabyBody(model)
	# baby.make_body()

	# アプリケーションのインスタンスを生成します。
	application = QApplication(sys.argv)

	# OpenGLウィンドウのインスタンスを生成し、ウィンドウを開きます。
	window = OpenGLWindow(model, application)
	window.show()

	# アプリケーションのイベントループに入ります。
	application.exec_()

	# イベントループを抜けて、正常終了を意味する0を応答します。
	return 0

if __name__ == '__main__':
	# このモジュールのmain()を呼び出し、結果を得て、Pythonシステムに終わりを告げます。
	sys.exit(main())
