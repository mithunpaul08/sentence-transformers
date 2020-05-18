#!/usr/bin/env bash

./get_fact_verification_files.sh
mkdir -p datasets/rte/fever/allnli/
mkdir -p datasets/rte/fnc/allnli/

python training_transformers/fact_verification/utils.py
rm -rf datasets/rte/fever/allnli/*.gz
rm -rf datasets/rte/fnc/allnli/*.gz
for each in datasets/rte/fever/allnli/*;
do
gzip  $each
done
for each in datasets/rte/fnc/allnli/*;
do
gzip  $each
done
