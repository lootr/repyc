#!/bin/sh
BASE=`dirname $0`/$1
mkdir -p $BASE
pushd $BASE
touch __init__.py
ln -sf ../template/Makefile
popd
make -C $BASE
