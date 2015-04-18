@echo off
set KBE_ROOT=D:/kbengine/
set KBE_RES_PATH=%KBE_ROOT%kbe/res/;./;./scripts/;./res/
set KBE_BIN_PATH=%KBE_ROOT%kbe/bin/server/

if defined uid (echo has define uid) else set uid=%random%%%32760+1

echo KBE_ROOT=%KBE_ROOT%
echo KBE_RES_PATH=%KBE_RES_PATH%
echo KBE_BIN_PATH=%KBE_BIN_PATH%
echo uid=%uid%

start %KBE_BIN_PATH%machine.exe --cid=1001001 --gus=1001
rem start %KBE_BIN_PATH%logger.exe --cid=2001001 --gus=2001
start %KBE_BIN_PATH%interfaces.exe --cid=3001001 --gus=3001
start %KBE_BIN_PATH%dbmgr.exe --cid=4001001 --gus=4001
start %KBE_BIN_PATH%baseappmgr.exe --cid=5001001 --gus=5001
start %KBE_BIN_PATH%cellappmgr.exe --cid=6001001 --gus=6001
start %KBE_BIN_PATH%baseapp.exe --cid=7001001 --gus=7001
start %KBE_BIN_PATH%baseapp.exe --cid=7002001 --gus=7002
start %KBE_BIN_PATH%baseapp.exe --cid=7003001 --gus=7003
start %KBE_BIN_PATH%cellapp.exe --cid=8001001 --gus=8001
rem start %KBE_BIN_PATH%cellapp.exe --cid=8002001 --gus=8002
rem start %KBE_BIN_PATH%cellapp.exe --cid=8003001 --gus=8003
start %KBE_BIN_PATH%loginapp.exe --cid=9001001 --gus=9001
