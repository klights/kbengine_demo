# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class AVATAR_INFOS:
	def __init__(self):
		self.value = {}
		
	def createFromDict(self, dct):
		for data in dct["values"]:
			self.value[data["dbid"]] = data
		return self
		
	def getDict(self):
		values = []
		dct = {"values" : values}
		for value in self.value.values():
			values.append(value)
		return dct

class AVATAR_INFOS_PICKLER:
	def __init__(self):
		pass
	
	def createObjFromDict(self, dct):
		return AVATAR_INFOS().createFromDict(dct)
	
	def getDictFromObj(self, obj):
		return obj.getDict()
		
	def isSameType(self, obj):
		return isinstance(obj, AVATAR_INFOS)

inst = AVATAR_INFOS_PICKLER()
