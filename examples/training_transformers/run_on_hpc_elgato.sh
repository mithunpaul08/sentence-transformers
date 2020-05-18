#!/bin/bash
#PBS -q standard
#PBS -l select=1:ncpus=1:mem=16gb:pcmem=16gb:ngpus=1
#PBS -W group_list=msurdeanu
#PBS -l walltime=00:10:00
#PBS -j oe


cd /home/u11/mithunpaul/
module load cuda10/10.1
module load python/3.8
mkdir my_virtual_env
python3 -m venv my_virtual_env
source my_virtual_env/bin/activate


#####my code part
export PYTHONPATH="/home/u11/mithunpaul/sentence-transformers/"
cd /home/u11/mithunpaul/sentence-transformers
pip install -r requirements.txt
#pip install torch==1.5.0+cu101 torchvision==0.6.0+cu101 -f https://download.pytorch.org/whl/torch_stable.htm
pip install torch torchvision
cd /home/u11/mithunpaul/sentence-transformers/examples
bash get_fact_verification_files.sh
bash reduce_size_fact_verification_files.sh
bash get_convert_zip_fact_verification_files.sh
cd /home/u11/mithunpaul/sentence-transformers/examples/training_transformers
python3 training_nli.py

