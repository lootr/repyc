#!/bin/sh

mkdir -p $1
pushd $1
ln -sf ../template/Makefile
popd
make -C $1
