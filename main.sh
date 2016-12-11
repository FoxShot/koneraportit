#!/bin/bash
tiedostot=$(ls | grep "[0-9]\.tex")

#vanhaa bashia (<4.1) varten
#ulos=$(printf '\subfile{%s}\\\vfill\pagebreak' $tiedostot)

printf -v subfilet '\\\subfile{%s}\\\ill\\\pagebreak' $tiedostot

ulos=$(cat main.tex | sed -e "s/%subfilet/$subfilet/g")
#ulos=egrep "%subfilet" . main.tex | xargs -l sed -e 's/subfilet/$subfilet/g'
pdflatex -output-directory="./build" -jobname main $ulos
echo $ulos
