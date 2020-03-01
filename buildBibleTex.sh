#!/bin/sh
cd bible_out
xelatex -syntax=1 bible.tex # will generate bible.toc , bible.aux
xelatex -syntax=1 bible.tex #second build, with success in toc
mv bible.pdf ../
cd ..
