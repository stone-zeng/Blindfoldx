# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin: BlindFold Neue
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

from GlyphsApp import *
from GlyphsApp.plugins import *
import objc
import math

class BlindFoldNeue(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Blindfold Neue',
			'zh': u'眼罩 Neue',
		})

	@objc.python_method
	def foreground(self, layer):
		self.drawRect(layer, self.getScale())

	@objc.python_method
	def inactiveLayerForeground(self, layer):
		self.drawRect(layer, self.getScale())

	@objc.python_method
	def drawRect(self, layer, scale):
		NSColor.blackColor().set()

		LEFT_VALUE   = 200
		RIGHT_VALUE  = 200
		TOP_VALUE 	 = 200
		BOTTOM_VALUE = 200

		master = layer.associatedFontMaster()

		descender = master.descender
		ascender  = master.ascender

		customAscender = master.customParameters['ascender']
		if customAscender is not None:
			ascender = int(customAscender.split(':')[-1])

		width  = layer.width
		height = ascender - descender

		# Left, right, top, bottom
		NSBezierPath.fillRect_(((0, descender), (LEFT_VALUE, height)))
		NSBezierPath.fillRect_(((width - RIGHT_VALUE, descender), (RIGHT_VALUE, height)))
		NSBezierPath.fillRect_(((0, ascender - TOP_VALUE), (width, TOP_VALUE)))
		NSBezierPath.fillRect_(((0, descender), (width, BOTTOM_VALUE)))

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
