# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import os

import GlobalDefine

class Avatar(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		DEBUG_MSG("Avatar(id=%i dbid=%i)::__init__" % (self.id, self.databaseID))
		
	def onDestroy(self):
		"""
		"""
		DEBUG_MSG("Avatar(id=%i dbid=%i)::onDestroy" % (self.id, self.databaseID))
		
	def onTimer(self, id, userdata):
		"""
		KBEngine method.
		"""
		pass
		
	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		"""
		INFO_MSG("Avatar(id=%i dbid=%i)::onEntitiesEnabled" % (self.id, self.databaseID))
		
	def onClientDeath(self):
		"""
		KBEngine method.
		"""
		INFO_MSG("Avatar(id=%i dbid=%i)::onClientDeath" % (self.id, self.databaseID))
		self.destroy()
		
		
		
		
		