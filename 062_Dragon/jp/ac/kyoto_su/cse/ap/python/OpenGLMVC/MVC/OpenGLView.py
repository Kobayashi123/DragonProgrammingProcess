#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例題プログラム：この例題を改変して大きなプログラムを作る足がかりにしてください。
"""

__author__ = 'AOKI Atsushi'
__version__ = '0.6.1'
__date__ = '2019/07/02 (Created: 2016/11/11)'

import math

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QOpenGLVersionProfile
from PyQt5.QtWidgets import QOpenGLWidget

from jp.ac.kyoto_su.cse.ap.python.OpenGLMVC.MVC.OpenGLController import OpenGLController
from jp.ac.kyoto_su.cse.ap.python.Trace import trace

class OpenGLView(QOpenGLWidget):
	"""
	PyQt5のQOpenGLWidgetを利用した三次元グラフィックス（OpenGL）のビュー（View of MVC）です。
	"""

	def __init__(self, model, width=400, height=400, parent=None):
		"""
		OpenGLViewのインスタンスを生成します。
		"""
		trace(self)

		super().__init__(parent)
		self._model = model
		self._controller = OpenGLController(self)
		self._width = width
		self._height = height
		self._gl = None
		self._angle_x = 0.0
		self._angle_y = 0.0
		self._angle_z = 0.0

	def gluLookAt(self, eye, sight, up):
		"""
		視点（eye）、注視点（sight）、上方向（up）を設定します。
		"""
		# trace(self)

		forward = [sight[0] - eye[0], sight[1] - eye[1], sight[2] - eye[2]]

		self._normalize(forward)

		side = [0,] * 3
		self._cross(forward, up, side)
		self._normalize(side)

		self._cross(side, forward, up)

		transform_matrix = [ \
			side[0], up[0], -forward[0], 0, \
			side[1], up[1], -forward[1], 0, \
			side[2], up[2], -forward[2], 0, \
			0, 0, 0, 1, \
			]

		translation_matrix = [ \
			1, 0, 0, 0, \
			0, 1, 0, 0, \
			0, 0, 1, 0, \
			-eye[0], -eye[1], -eye[2], 1, \
			]

		matrix = [0,] * 16
		self._multiplication(transform_matrix, translation_matrix, matrix)
		self._multiplication(transform_matrix, translation_matrix, matrix)
		self._gl.glLoadMatrixf(matrix)

	def gluPerspective(self, fovy, aspect, near, far):
		"""
		縦の視野角（fovy）、縦に対する横方向の視野角の倍率（aspect）、近い位置（near）、遠い位置（far）を設定します。
		"""
		#trace(self)

		radian = 2.0 * math.pi * fovy / 360.0
		scale = 1.0 / math.tan(radian / 2)
		matrix = [ \
			scale / aspect, 0, 0, 0, \
			0, scale, 0, 0, \
			0, 0, (far + near) / (near - far), -1, \
			0, 0, (2 * far * near) / (near - far), 0, \
			]
		self._gl.glLoadMatrixf(matrix)

	def initializeGL(self):
		"""
		OpenGLの初期化を行います。
		"""
		trace(self)

		version = QOpenGLVersionProfile()
		version.setVersion(2, 1)

		self._gl = self.context().versionFunctions(version)
		self._gl.initializeOpenGLFunctions()

		gl = self._gl
		gl.glEnable(gl.GL_COLOR_MATERIAL)
		gl.glEnable(gl.GL_DEPTH_TEST)
		gl.glEnable(gl.GL_CULL_FACE)
		gl.glEnable(gl.GL_NORMALIZE)
		gl.glShadeModel(gl.GL_SMOOTH)

		gl.glClearColor(0.9, 0.9, 0.9, 1.0)    # Red, Green, Blue, Alpha

	def paintGL(self):
		"""
		OpenGLViewの中を描きます。
		"""
		trace(self)

		eye_point = self._model._eye_point
		sight_point = self._model._sight_point
		up_vector = self._model._up_vector
		fovy = self._model._fovy

		aspect = float(self._width) / float(self._height)
		near = 0.01
		far = 100.0

		gl = self._gl

		gl.glMatrixMode(gl.GL_PROJECTION)
		gl.glLoadIdentity()
		self.gluPerspective(fovy, aspect, near, far)

		gl.glMatrixMode(gl.GL_MODELVIEW)
		gl.glLoadIdentity()
		self.gluLookAt(eye_point, sight_point, up_vector)

		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

		# 照明を設定します
		gl.glEnable(gl.GL_LIGHTING)
		gl.glLightModelfv(gl.GL_LIGHT_MODEL_AMBIENT, [0.5, 0.5, 0.5, 1.0])
		gl.glLightModelf(gl.GL_LIGHT_MODEL_LOCAL_VIEWER, 0.0)
		gl.glLightModelf(gl.GL_LIGHT_MODEL_TWO_SIDE, 1.0)
		gl.glEnable(gl.GL_LIGHT0)
		gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, [0.0, 0.0, 1.0, 0.0])
		gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPOT_DIRECTION, [0.0, 0.0, -1.0])
		gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPOT_CUTOFF, [90.0])
		gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
		gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
		gl.glLightfv(gl.GL_LIGHT0, gl.GL_LINEAR_ATTENUATION, [0.0])
		gl.glLightfv(gl.GL_LIGHT0, gl.GL_QUADRATIC_ATTENUATION, [0.0])
		gl.glLightfv(gl.GL_LIGHT0, gl.GL_CONSTANT_ATTENUATION, [1.0])

		# 絶対座標系（X軸：赤、Y軸：緑、Z軸：青）を描きます。負方向を1とすると、正方向は黄金比(1.618)になります。
		self.rendering_axes(gl)

		# モデル座標系を回転させます。
		gl.glRotated(self._angle_x, 1.0, 0.0, 0.0)
		gl.glRotated(self._angle_y, 0.0, 1.0, 0.0)
		gl.glRotated(self._angle_z, 0.0, 0.0, 1.0)
		# モデルを描き出します。
		self._model.rendering(gl)

	def rendering_axes(self, gl):
		"""
		世界座標系（絶対座標系）を描画（レンダリング）します。
		"""
		trace(self)

		axes_scale = self._model._axes_scale
		map_function = (lambda value: value * axes_scale)
		scaled_by_n = (lambda vertex: list(map(map_function, vertex)))
		gl.glBegin(gl.GL_LINES)
		gl.glColor4f(1.0, 0.0, 0.0, 1.0)
		gl.glVertex3fv(scaled_by_n([-1.000, 0.0, 0.0]))
		gl.glVertex3fv(scaled_by_n([+1.618, 0.0, 0.0]))
		gl.glColor4f(0.0, 1.0, 0.0, 1.0)
		gl.glVertex3fv(scaled_by_n([0.0, -1.000, 0.0]))
		gl.glVertex3fv(scaled_by_n([0.0, +1.618, 0.0]))
		gl.glColor4f(0.0, 0.0, 1.0, 1.0)
		gl.glVertex3fv(scaled_by_n([0.0, 0.0, -1.000]))
		gl.glVertex3fv(scaled_by_n([0.0, 0.0, +1.618]))
		gl.glEnd()

	def resizeGL(self, width, height):
		"""
		OpenGLViewの大きさが変更された際に、OpenGLのビューポートを再形成します。
		"""
		trace(self)

		self._width = width
		self._height = height
		extent = min(width, height)
		x = (width - extent) // 2
		y = (height - extent) // 2
		w = extent
		h = extent
		self._gl.glViewport(x, y, w, h)

	def sizeHint(self):
		"""
		OpenGLViewの大きさを応答します。
		"""
		trace(self)

		return QSize(self._width, self._height)

	@staticmethod
	def _cross(src1, src2, dst):
		"""
		二つのベクトル（二つの座標：src1=(x1,y1,z1), src2=(x2,y2,z2)）の外積を求めます。
		"""

		dst[0] = src1[1] * src2[2] - src1[2] * src2[1]
		dst[1] = src1[2] * src2[0] - src1[0] * src2[2]
		dst[2] = src1[0] * src2[1] - src1[1] * src2[0]

	@staticmethod
	def _normalize(v):
		"""
		ベクトル（座標：v=(x,y,z)）を正規化します。
		"""

		m = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
		if m > 0.0:
			m = 1.0 / m
		else:
			m = 0.0
		v[0] = v[0] * m
		v[1] = v[1] * m
		v[2] = v[2] * m

	@staticmethod
	def _multiplication(src1, src2, dst):
		"""
		二つの同次座標変換行列を合成します。
		"""

		for y in range(4):
			for x in range(4):
				dst[y*4+x] = src2[y*4] * src1[x] + src2[y*4+1] * src1[x+4] + src2[y*4+2] * src1[x+8] + src2[y*4+3] * src1[x+12]

	def mouseMoveEvent(self, event):
		"""
		マウスが移動した際にコントローラに通知します。
		"""
		self._controller.motion(event)

	def mousePressEvent(self, event):
		"""
		マウスボタンが押された際にコントローラに通知します。
		"""
		self._controller.mouse(event)
