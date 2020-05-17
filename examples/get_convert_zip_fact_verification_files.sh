#!/usr/bin/env bash
./get_fact_verification_files.sh
mkdir -p datasets/rte/fever/allnli/

python training_transformers/fact_verification/utils.py
for each in datasets/rte/fever/allnli/*;
do
gzip $each
done