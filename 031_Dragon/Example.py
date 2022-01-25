#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.3.0'
__date__ = '2019/06/29 (Created: 2016/11/11)'

import sys

from PyQt5.QtWidgets import QApplication

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.MVC.OpenGLModel import OpenGLModel
from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.OpenGLWindow import OpenGLWindow
from jp.ac.kyoto_su.cse.ap.python.Trace import Trace    # トレース情報出力のON/OFFに用います。
from jp.ac.kyoto_su.cse.ap.python.Trace import trace    # トレース情報出力のための関数です。

class DragonBody:
	"""
	ドラゴン立体です。
	"""

	def __init__(self, model):
		"""
		モデル(OpenGLModel)からドラゴン立体のインスタンスを生成します。
		"""
		trace(self)

		self._usr = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/VisualWorks/Dragon/dragon.txt'
		self._model = model

	def make_body(self):
		"""
		モデルに表示物を登録します。
		"""
		trace(self)

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

	# ドラゴン立体のインスタンスを生成し、モデルに表示物を登録します。
	dragon = DragonBody(model)
	dragon.make_body()

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
