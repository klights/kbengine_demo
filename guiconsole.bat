@echo off
set KBE_ROOT=D:/kbengine/
set KBE_RES_PATH=%KBE_ROOT%kbe/res/;./;./scripts/;./res/
set KBE_BIN_PATH=%KBE_ROOT%kbe/bin/server/

if defined uid (echo has define uid) else set uid=%random%%%32760+1

echo KBE_ROOT=%KBE_ROOT%
echo KBE_RES_PATH=%KBE_RES_PATH%
echo KBE_BIN_PATH=%KBE_BIN_PATH%
echo uid=%uid%

start %KBE_ROOT%/kbe/tools/server/guiconsole/guiconsole.exe
