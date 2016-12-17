#!/bin/bash

for fl in *.tex; do
	mv $fl $fl.old
	sed "s/scshape\\\Large/section/g" $fl.old > $fl
#	sed 's/}}/}/g' $fl
done
