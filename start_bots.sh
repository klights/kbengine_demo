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

$KBE_BIN_PATH/bots --cid=10001004 --gus=10001&

#$KBE_BIN_PATH/bots --cid=10002004 --gus=10002&

#$KBE_BIN_PATH/bots --cid=10003004 --gus=10003&

#$KBE_BIN_PATH/bots --cid=10004004 --gus=10004&

#$KBE_BIN_PATH/bots --cid=10005004 --gus=10005&

#$KBE_BIN_PATH/bots --cid=10006004 --gus=10006&

#$KBE_BIN_PATH/bots --cid=10007004 --gus=10007&

#$KBE_BIN_PATH/bots --cid=10008004 --gus=10008&

#$KBE_BIN_PATH/bots --cid=10009004 --gus=10009&

#$KBE_BIN_PATH/bots --cid=10010004 --gus=10010&

#$KBE_BIN_PATH/bots --cid=10011004 --gus=10011&

#$KBE_BIN_PATH/bots --cid=10012004 --gus=10012&

#$KBE_BIN_PATH/bots --cid=10013004 --gus=10013&
