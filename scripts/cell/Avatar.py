# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Avatar(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		
	def onDestroy(self):
		"""
		"""
		DEBUG_MSG("Avatar(id=%i spaceID=%i)::onDestroy" % (self.id, self.spaceID))
		