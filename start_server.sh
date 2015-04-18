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

rm core.*
rm ./logs/baseapp*
rm ./logs/cellapp*
rm ./logs/dbmgr*
rm ./logs/loginapp*

#$KBE_BIN_PATH/machine --cid=1001004 --gus=1001&
#sleep 1s
#$KBE_BIN_PATH/logger --cid=2001004 --gus=2001&
#sleep 1s
#$KBE_BIN_PATH/interfaces --cid=3001004 --gus=3001&
#sleep 1s
$KBE_BIN_PATH/dbmgr --cid=4001004 --gus=4001&
#sleep 1s
$KBE_BIN_PATH/baseappmgr --cid=5001004 --gus=5001&
#sleep 1s
$KBE_BIN_PATH/cellappmgr --cid=6001004 --gus=6001&
#sleep 1s
$KBE_BIN_PATH/baseapp --cid=7001004 --gus=7001&
#sleep 1s
$KBE_BIN_PATH/baseapp --cid=7002004 --gus=7002&
#sleep 1s
$KBE_BIN_PATH/baseapp --cid=7003004 --gus=7003&
#sleep 1s
$KBE_BIN_PATH/cellapp --cid=8001004 --gus=8001&
#sleep 1s
$KBE_BIN_PATH/cellapp --cid=8002004 --gus=8002&
#sleep 1s
$KBE_BIN_PATH/cellapp --cid=8003004 --gus=8003&
#sleep 1s
$KBE_BIN_PATH/loginapp --cid=9001004 --gus=9001&
