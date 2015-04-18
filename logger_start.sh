#!/bin/sh

cd ~/map
cp -f ./kbengine_linux.xml ./res/server/kbengine.xml

sudo svn update

export KBE_ROOT="/home/dbg2/kbengine/"
export KBE_RES_PATH="$KBE_ROOT/kbe/res/:/home/dbg2/map/:/home/dbg2/map/res/:/home/dbg2/map/scripts/"
export KBE_BIN_PATH="$KBE_ROOT/kbe/bin/server/"

echo KBE_ROOT=\"$KBE_ROOT\"
echo KBE_RES_PATH=\"$KBE_RES_PATH\"
echo KBE_BIN_PATH=\"$KBE_BIN_PATH\"

rm ./logs/logger*

$KBE_BIN_PATH/logger --cid=2001004 --gus=2001&
