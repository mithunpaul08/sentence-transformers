#!/bin/bash
#PBS -q standard
#PBS -l select=1:ncpus=28:mem=168gb:pcmem=6gb:ngpus=1:os7=True
#PBS -W group_list=msurdeanu
#PBS -l walltime=10:00:00
#PBS -j oe


cd /home/u11/mithunpaul/
module load cuda90/neuralnet/7/7.3.1.20
module load python/3.6/3.6.5
#rm -rf my_virtual_env
#mkdir my_virtual_env
#python3 -m venv my_virtual_env
source my_virtual_env/bin/activate
#pip install torch==1.5.0+cu92 torchvision==0.6.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html


#####my code part
export PYTHONPATH="/home/u11/mithunpaul/sentence-transformers/"
cd /home/u11/mithunpaul/sentence-transformers
#pip install -r requirements.txt
cd /home/u11/mithunpaul/sentence-transformers/examples

#remove these two lines if you want to run on full data
bash get_fact_verification_files.sh
bash reduce_size_fact_verification_files.sh

bash get_convert_zip_fact_verification_files.sh
cd /home/u11/mithunpaul/sentence-transformers/examples/training_transformers
python3 training_nli.py

