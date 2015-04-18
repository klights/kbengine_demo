@echo off
set KBE_ROOT=D:/kbengine/
set KBE_RES_PATH=%KBE_ROOT%kbe/res/;./;./scripts/;./res/
set KBE_BIN_PATH=%KBE_ROOT%kbe/bin/server/

if defined uid (echo has define uid) else set uid=%random%%%32760+1

echo KBE_ROOT=%KBE_ROOT%
echo KBE_RES_PATH=%KBE_RES_PATH%
echo KBE_BIN_PATH=%KBE_BIN_PATH%
echo uid=%uid%

start %KBE_BIN_PATH%bots.exe --cid=10001001 --gus=10001
rem start %KBE_BIN_PATH%bots.exe --cid=10002001 --gus=10002
rem start %KBE_BIN_PATH%bots.exe --cid=10003001 --gus=10003
rem start %KBE_BIN_PATH%bots.exe --cid=10004001 --gus=10004
rem start %KBE_BIN_PATH%bots.exe --cid=10005001 --gus=10005
rem start %KBE_BIN_PATH%bots.exe --cid=10006001 --gus=10006
rem start %KBE_BIN_PATH%bots.exe --cid=10007001 --gus=10007
rem start %KBE_BIN_PATH%bots.exe --cid=10008001 --gus=10008
rem start %KBE_BIN_PATH%bots.exe --cid=10009001 --gus=10009
rem start %KBE_BIN_PATH%bots.exe --cid=10010001 --gus=10010
rem start %KBE_BIN_PATH%bots.exe --cid=10011001 --gus=10011
rem start %KBE_BIN_PATH%bots.exe --cid=10012001 --gus=10012
rem start %KBE_BIN_PATH%bots.exe --cid=10013001 --gus=10013
