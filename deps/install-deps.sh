#!/bin/bash

SKIA_REV=`cat skia_version.txt`

svn checkout http://skia.googlecode.com/svn/trunk@${SKIA_REV} skia
