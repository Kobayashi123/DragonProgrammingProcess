#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.0.0'
__date__ = '2019/06/26 (Created: 2016/11/11)'

import sys

from jp.ac.kyoto_su.cse.ap.python.Trace import Trace    # トレース情報出力のON/OFFに用います。
from jp.ac.kyoto_su.cse.ap.python.Trace import trace    # トレース情報出力のための関数です。

def main():
	"""
	PyQt5のQOpenGLWidgetを利用した三次元グラフィックス（OpenGL）のモデル・ビュー・コントローラ（MVC：Model-View-Controller）の例題（メイン・プログラム）です。
	常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
	"""
	# Trace.trace_off()
	Trace.trace_on()
	trace(main)

	# 正常終了を意味する0を応答します。
	return 0

if __name__ == '__main__':
	# このモジュールのmain()を呼び出し、結果を得て、Pythonシステムに終わりを告げます。
	sys.exit(main())
