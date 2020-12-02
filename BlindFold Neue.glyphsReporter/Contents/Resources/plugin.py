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

import objc

from Foundation import NSBezierPath, NSColor

from GlyphsApp import *
from GlyphsApp.plugins import *

class BlindFoldNeue(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Blindfold Neue',
			'zh': u'眼罩 Neue',
		})
		self.inverseBlindfold = False
		self.generalContextMenus = self.buildContextMenus()

	@objc.python_method
	def buildContextMenus(self, sender=None):
		return [
			{
				'name': Glyphs.localize({
					'en': 'Blindfold Neue Options:',
					'zh': u'眼罩 Neue 选项：',
					}), 
				'action': None,
			},
			{
				'name': Glyphs.localize({
					'en': 'Inverse blindfold',
					'zh': u'反转眼罩',
				}),
				'action': self.inverse,
				'state': self.inverseBlindfold,
			},
		]

	def inverse(self):
		self.inverseBlindfold = not self.inverseBlindfold
		self.generalContextMenus = self.buildContextMenus()

	@objc.python_method
	def foreground(self, layer):
		self.drawRect(layer)

	@objc.python_method
	def inactiveLayerForeground(self, layer):
		self.drawRect(layer)

	@objc.python_method
	def drawRect(self, layer):
		self.getWidth()
		self.getColor()

		master = layer.associatedFontMaster()

		descender = master.descender
		ascender  = master.ascender

		customAscender = master.customParameters['ascender']
		if customAscender is not None:
			ascender = int(customAscender.split(':')[-1])

		width  = layer.width
		height = ascender - descender

		(left_width, right_width, top_width, bottom_width) = self.blindfoldWidth

		if self.inverseBlindfold:
			rect = (
				(left_width, descender + bottom_width),
				(width - left_width - right_width, height - top_width - bottom_width)
			)
			NSBezierPath.fillRect_(rect)
		else:
			for rect in [
				# Left, right, top, bottom
				((0, descender), (left_width, height)),
				((width - right_width, descender), (right_width, height)),
				((left_width, ascender - top_width), (width - left_width - right_width, top_width)),
				((left_width, descender), (width - left_width - right_width, bottom_width)),
			]:
				NSBezierPath.fillRect_(rect)

	@objc.python_method
	def getWidth(self):
		self.blindfoldWidth = (100, 100, 100, 100)  # Initial value

		widthStr = Glyphs.font.customParameters['blindfoldWidth']
		if widthStr:
			width = eval(widthStr)
			if type(width) == tuple:
				if len(width) == 2:
					self.blindfoldWidth = (width[0], width[0], width[1], width[1])
				elif len(width) == 4:
					self.blindfoldWidth = width
			elif type(width) == int or type(width) == float:
				self.blindfoldWidth = (width, width, width, width)

	@objc.python_method
	def getColor(self):
		color = NSColor.colorWithRed_green_blue_alpha_(0, 0, 0, 0.9)  # Initial value

		colorStr = Glyphs.font.customParameters['blindfoldColor']
		if colorStr:
			colorTuple = eval(colorStr)
			if type(colorTuple) == tuple and len(colorTuple) == 4:
				color = NSColor.colorWithRed_green_blue_alpha_(*colorTuple)

		color.set()

	@objc.python_method
	def __file__(self):
		'''Please leave this method unchanged'''
		return __file__
