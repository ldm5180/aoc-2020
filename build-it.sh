#!/bin/bash

files=${1:-"*.cpp"}

for f in $files; do
    ccache clang++-12 -std=c++20 -O3 \
	   -Werror -Wall -Wextra -pedantic \
	   -fconstexpr-steps=1000000000 \
	   $f \
	   -o bin/${f%.*} \
	&& \
	bin/${f%.*}
done
