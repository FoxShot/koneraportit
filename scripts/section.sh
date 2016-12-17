#!/bin/bash

for fl in *.tex.old; do
	mv $fl $fl.tex
	sed "s/scshape\\\Large/section/g" $fl > $fl.tex
#	sed 's/}}/}/g' $fl
done
