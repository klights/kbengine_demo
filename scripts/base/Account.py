# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

import Functor

CreateAvatarFailed = 1
AvatarWriteToDBFailed = 2

class Account(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		
	def onDestroy(self):
		"""
		"""
		DEBUG_MSG("Account(id=%i dbid=%i)::onDestroy" % (self.id, self.databaseID))
		
	def onTimer(self, id, userdata):
		"""
		KBEngine method.
		"""
		pass
		
	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		"""
		INFO_MSG("Account(id=%i dbid=%i)::onEntitiesEnabled" % (self.id, self.databaseID))
		
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		"""
		INFO_MSG("Account(id=%i dbid=%i)::onClientDeath ip=%s port=%s password=%s" % (self.id, self.databaseID, ip, port, password))
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		"""
		INFO_MSG("Account(id=%i dbid=%i)::onClientDeath" % (self.id, self.databaseID))
		self.destroy()
		
	def requestAvatarList(self):
		"""
		Define method.
		"""
		DEBUG_MSG("Account(id=%i dbid=%i)::requestAvatarList self.avatarInfos=%s" % (self.id, self.databaseID, self.avatarInfos.value))
		self.client.responseAvatarList(self.avatarInfos)
		
	def requestCreateAvatar(self, name):
		"""
		Define method.
		"""
		DEBUG_MSG("Account(id=%i dbid=%i)::requestCreateAvatar name=%s" % (self.id, self.databaseID, name))
		avatar = KBEngine.createBaseLocally("Avatar", {"name":name})
		if(avatar):
			avatar.writeToDB(self._onAvatarWriteToDB)
		else:
			ERROR_MSG("Account(id=%i dbid=%i)::requestCreateAvatar name=%s create avatar failed" % (self.id, self.databaseID, name))
			self.client.responseCreateAvatarFailed(CreateAvatarFailed)
		
	def selectAvatarEnterGame(self, avatarDBID):
		"""
		Define method.
		"""
		DEBUG_MSG("Account(id=%i dbid=%i)::selectAvatarEnterGame avatarDBID=%i" % (self.id, self.databaseID, avatarDBID))
		KBEngine.createBaseFromDBID("Avatar", avatarDBID, self._onCreateAvatarFromDBID)
		
	def _onAvatarWriteToDB(self, success, avatar):
		"""
		"""
		DEBUG_MSG("Account(id=%i dbid=%i)::_onAvatarWriteToDB success=%s avatar=%s" % (self.id, self.databaseID, success, avatar))
		if(success):
			avatarInfo = {"dbid":avatar.databaseID, "name":avatar.name}
			self.avatarInfos.value[avatar.databaseID] = avatarInfo
			avatar.destroy()
			self.writeToDB(Functor.Functor(self._onSelfWriteToDB_saveAvatarInfo, avatarInfo))
		else:
			ERROR_MSG("Account(id=%i dbid=%i)::_onAvatarWriteToDB success=%s avatar=%s" % (self.id, self.databaseID, success, avatar))
			avatar.destroy()
			self.client.responseCreateAvatarFailed(AvatarWriteToDBFailed)
		
	def _onSelfWriteToDB_saveAvatarInfo(self, avatarInfo, success, account):
		"""
		"""
		DEBUG_MSG("Account(id=%i dbid=%i)::_onSelfWriteToDB_saveAvatarInfo success=%s account=%s" % (self.id, self.databaseID, success, account))
		self.client.responseCreateAvatar(avatarInfo)
		
	def _onCreateAvatarFromDBID(self, baseRef, dbid, wasActive):
		"""
		"""
		DEBUG_MSG("Account(id=%i dbid=%i)::_onCreateAvatarFromDBID baseRef=%s dbid=%s wasActive=%s" % (self.id, self.databaseID, baseRef, dbid, wasActive))
		
		if(wasActive or baseRef is None):
			ERROR_MSG("Account(id=%i dbid=%i)::_onCreateAvatarFromDBID baseRef=%s dbid=%s wasActive=%s" % (self.id, self.databaseID, baseRef, dbid, wasActive))
			return
		
		avatar = KBEngine.entities.get(baseRef.id)
		if(avatar):
			self.giveClientTo(avatar)
		