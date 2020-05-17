#!/usr/bin/env bash
head -100 datasets/rte/fever/train/fever_train_delex.jsonl > temp
mv temp datasets/rte/fever/train/fever_train_delex.jsonl

head -100 datasets/rte/fever/train/fever_train_lex.jsonl > temp
mv temp datasets/rte/fever/train/fever_train_lex.jsonl


head -20 datasets/rte/fever/dev/fever_dev_delex.jsonl > temp
mv temp datasets/rte/fever/dev/fever_dev_delex.jsonl

head -20 datasets/rte/fever/dev/fever_dev_lex.jsonl > temp
mv temp datasets/rte/fever/dev/fever_dev_lex.jsonl

#all fnc related
head -20 datasets/rte/fnc/test/fnc_test_delex.jsonl > temp
mv temp datasets/rte/fnc/test/fnc_test_delex.jsonl

head -20 datasets/rte/fnc/test/fnc_test_lex.jsonl > temp
mv temp datasets/rte/fnc/test/fnc_test_lex.jsonl

head -20 datasets/rte/fnc/dev/fnc_dev_lex.jsonl > temp
mv temp datasets/rte/fnc/dev/fnc_dev_lex.jsonl


head -20 datasets/rte/fnc/dev/fnc_dev_delex.jsonl > temp
mv temp datasets/rte/fnc/dev/fnc_dev_delex.jsonl


