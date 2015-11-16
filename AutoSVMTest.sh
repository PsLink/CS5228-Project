#!/bin/bash 

# automatically svm test

for i in `ls ./querys/`
do
  ./svm-train ./querys/$i ./models/$i.model
  ./svm-predict ./tests/$i ./models/$i.model out.$i

done

for i in `ls | grep out`
do
    cat $i >> Output
done

