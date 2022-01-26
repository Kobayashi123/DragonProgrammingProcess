#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '1.0.2'
__date__ = '2019/06/26 (Created: 2016/11/11)'

import inspect
import os
import sys

class Trace:
	"""
	トレース情報出力のON/OFFを司ります。
	"""

	TRACE = False # クラス変数（クラス属性）：トレース情報出力のON/OFFに用います。

	@staticmethod
	def trace_on():
		"""
		トレース情報出力をONにします。
		"""

		Trace.TRACE = True

	@staticmethod
	def trace_off():
		"""
		トレース情報出力をOFFにします。
		"""

		Trace.TRACE = False

def trace(an_object):
	"""
	この関数を呼び出したフレームオブジェクトから、ファイル名と行番号、そして、クラス名とメソッド名または関数名を割り出して、ドキュメント文字列を獲得し、それらを一緒に出力します。
	"""

	if Trace.TRACE:
		current_frame = inspect.stack(1)[0][0]
		current_frame = inspect.currentframe()
		current_frame = sys._getframe()
		sender_code_object = current_frame.f_back.f_code
		current_code_object = current_frame.f_code

		file_name = sender_code_object.co_filename
		this_directory_name = os.path.dirname(current_code_object.co_filename)
		if file_name.find(this_directory_name) >= 0:
			file_name = file_name[len(this_directory_name)+1:]
		line_no = sender_code_object.co_firstlineno

		method_name = sender_code_object.co_name

		argument_count = sender_code_object.co_argcount
		argument_string = ', '.join(sender_code_object.co_varnames[:argument_count])

		class_name = an_object.__class__.__qualname__
		class_name = an_object.__class__.__name__

		try:
			document_string = getattr(an_object, method_name).__doc__
		except AttributeError:
			document_string = an_object.__doc__
		document_string = document_string.strip()

		print(f"{file_name}:{line_no} [{class_name}.{method_name}({argument_string})] {document_string}")
