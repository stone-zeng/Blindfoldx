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
from vanilla import *
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
	def getWidth(self):
		self.blindfoldWidth = (100, 100, 100, 100)  # Initial value

		font = Glyphs.font
		width = eval(font.customParameters['blindfoldWidth'])

		if type(width) == tuple:
			if len(width) == 2:
				self.blindfoldWidth = (width[0], width[0], width[1], width[1])
			elif len(width) == 4:
				self.blindfoldWidth = width
		elif type(width) == int or type(width) == float:
			self.blindfoldWidth = (width, width, width, width)

	@objc.python_method
	def foreground(self, layer):
		self.getWidth()
		self.drawRect(layer, self.getScale())

	@objc.python_method
	def inactiveLayerForeground(self, layer):
		self.getWidth()
		self.drawRect(layer, self.getScale())

	@objc.python_method
	def drawRect(self, layer, scale):
		NSColor.blackColor().set()

		master = layer.associatedFontMaster()

		descender = master.descender
		ascender  = master.ascender

		customAscender = master.customParameters['ascender']
		if customAscender is not None:
			ascender = int(customAscender.split(':')[-1])

		width  = layer.width
		height = ascender - descender

		(left_width, right_width, top_width, bottom_width) = self.blindfoldWidth

		# Left, right, top, bottom
		for rect in [
			((0, descender), (left_width, height)),
			((width - right_width, descender), (right_width, height)),
			((0, ascender - top_width), (width, top_width)),
			((0, descender), (width, bottom_width)),
		]:
			NSBezierPath.fillRect_(rect)

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
