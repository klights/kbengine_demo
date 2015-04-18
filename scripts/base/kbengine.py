# -*- coding: utf-8 -*-
import os
import KBEngine
from KBEDebug import *

def onBaseAppReady(isBootstrap):
	"""
	KBEngine method.
	baseapp已经准备好了
	@param isBootstrap: 是否为第一个启动的baseapp
	@type isBootstrap: BOOL
	"""
	bootIdxGroup = int(os.getenv("KBE_BOOTIDX_GROUP"))
	bootIdxGlobal = int(os.getenv("KBE_BOOTIDX_GLOBAL"))
	INFO_MSG('onBaseAppReady: isBootstrap=%s, bootstrapGroupIndex=%s, bootstrapGlobalIndex=%s' % (isBootstrap, bootIdxGroup, bootIdxGlobal))
	
	table_vex = "map_%s_vex" % (bootIdxGroup)
	table_arc = "map_%s_arc" % (bootIdxGroup)
	table_triangle = "map_%s_triangle" % (bootIdxGroup)
	
	cmd = "CREATE TABLE IF NOT EXISTS `%s`(`id` BIGINT UNSIGNED NOT NULL, `campId` TINYINT NOT NULL, `position_x` INT NOT NULL, `position_y` INT NOT NULL, PRIMARY KEY(`id`)) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;" % (table_vex)
	KBEngine.executeRawDatabaseCommand(cmd, None, bootIdxGlobal)
	cmd = "CREATE TABLE IF NOT EXISTS `%s`(`id1` BIGINT UNSIGNED NOT NULL, `id2` BIGINT UNSIGNED NOT NULL) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;" % (table_arc)
	KBEngine.executeRawDatabaseCommand(cmd, None, bootIdxGlobal)
	cmd = "CREATE TABLE IF NOT EXISTS `%s`(`id1` BIGINT UNSIGNED NOT NULL, `id2` BIGINT UNSIGNED NOT NULL, `id3` BIGINT UNSIGNED NOT NULL) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;" % (table_triangle)
	KBEngine.executeRawDatabaseCommand(cmd, None, bootIdxGlobal)
	
	cmd = "SELECT `id`, `campId`, `position_x`, `position_y` FROM `%s`;" % (table_vex)
	KBEngine.executeRawDatabaseCommand(cmd, dbGetVexs, bootIdxGlobal)
	
	cmd = "SELECT `id1`, `id2` FROM `%s`;" % (table_arc)
	KBEngine.executeRawDatabaseCommand(cmd, dbGetArcs, bootIdxGlobal)
	
	cmd = "SELECT `id1`, `id2`, `id3` FROM `%s`;" % (table_triangle)
	KBEngine.executeRawDatabaseCommand(cmd, dbGetTriangles, bootIdxGlobal)

def dbGetVexs(result, num, error):
	"""
	"""
	if(error is None):
		if(result is not None):
			for item in result:
				KBEngine.mapGame.insertVexGreen(int(item[1]), int(item[2]), int(item[3]), int(item[0]))
		else:
			ERROR_MSG("kbengine(bootIdxGroup=%s, bootIdxGlobal=%s)::dbGetVexs result is None. result=%s num=%s error=%s" % (os.getenv("KBE_BOOTIDX_GROUP"), os.getenv("KBE_BOOTIDX_GLOBAL"), result, num, error))
	else:
		ERROR_MSG("kbengine(bootIdxGroup=%s, bootIdxGlobal=%s)::dbGetVexs error=%s" % (os.getenv("KBE_BOOTIDX_GROUP"), os.getenv("KBE_BOOTIDX_GLOBAL"), error))

def dbGetArcs(result, num, error):
	"""
	"""
	if(error is None):
		if(result is not None):
			for item in result:
				KBEngine.mapGame.insertArcGreen(int(item[0]), int(item[1]))
		else:
			ERROR_MSG("kbengine(bootIdxGroup=%s, bootIdxGlobal=%s)::dbGetArcs result is None. result=%s num=%s error=%s" % (os.getenv("KBE_BOOTIDX_GROUP"), os.getenv("KBE_BOOTIDX_GLOBAL"), result, num, error))
	else:
		ERROR_MSG("kbengine(bootIdxGroup=%s, bootIdxGlobal=%s)::dbGetArcs error=%s" % (os.getenv("KBE_BOOTIDX_GROUP"), os.getenv("KBE_BOOTIDX_GLOBAL"), error))

def dbGetTriangles(result, num, error):
	"""
	"""
	if(error is None):
		if(result is not None):
			for item in result:
				KBEngine.mapGame.insertTriangleGreen(int(item[0]), int(item[1]), int(item[2]))
		else:
			ERROR_MSG("kbengine(bootIdxGroup=%s, bootIdxGlobal=%s)::dbGetTriangles result is None. result=%s num=%s error=%s" % (os.getenv("KBE_BOOTIDX_GROUP"), os.getenv("KBE_BOOTIDX_GLOBAL"), result, num, error))
	else:
		ERROR_MSG("kbengine(bootIdxGroup=%s, bootIdxGlobal=%s)::dbGetTriangles error=%s" % (os.getenv("KBE_BOOTIDX_GROUP"), os.getenv("KBE_BOOTIDX_GLOBAL"), error))

def onReadyForLogin(isBootstrap):
	"""
	KBEngine method.
	如果返回值大于等于1.0则初始化全部完成, 否则返回准备的进度值0.0~1.0。
	在此可以确保脚本层全部初始化完成之后才开放登录。
	@param isBootstrap: 是否为第一个启动的baseapp
	@type isBootstrap: BOOL
	"""
	return 1.0

def onBaseAppShutDown(state):
	"""
	KBEngine method.
	这个baseapp被关闭前的回调函数
	@param state: 0 : 在断开所有客户端之前
				  1 : 在将所有entity写入数据库之前
				  2 : 所有entity被写入数据库之后
	@type state: int
	"""
	INFO_MSG('onBaseAppShutDown: state=%i' % state)
		
def onInit(isReload):
	"""
	KBEngine method.
	当引擎启动后初始化完所有的脚本后这个接口被调用
	@param isReload: 是否是被重写加载脚本后触发的
	@type isReload: bool
	"""
	INFO_MSG('onInit::isReload:%s' % isReload)

def onFini():
	"""
	KBEngine method.
	引擎正式关闭
	"""
	INFO_MSG('onFini()')
	
def onCellAppDeath(addr):
	"""
	KBEngine method.
	某个cellapp死亡
	"""
	WARNING_MSG('onCellAppDeath: %s' % (str(addr)))
	
def onGlobalData(key, value):
	"""
	KBEngine method.
	globalData有改变
	"""
	DEBUG_MSG('onGlobalData: %s' % key)
	
def onGlobalDataDel(key):
	"""
	KBEngine method.
	globalData有删除
	"""
	DEBUG_MSG('onDelGlobalData: %s' % key)
	
def onGlobalBases(key, value):
	"""
	KBEngine method.
	globalBases有改变
	"""
	DEBUG_MSG('onGlobalBases: %s' % key)
	
def onGlobalBasesDel(key):
	"""
	KBEngine method.
	globalBases有删除
	"""
	DEBUG_MSG('onGlobalBasesDel: %s' % key)

def onLoseChargeCB(ordersID, dbid, success, datas):
	"""
	KBEngine method.
	有一个不明订单被处理， 可能是超时导致记录被billing
	清除， 而又收到第三方充值的处理回调
	"""
	DEBUG_MSG('onLoseChargeCB: ordersID=%s, dbid=%i, success=%i, datas=%s' % \
							(ordersID, dbid, success, datas))


