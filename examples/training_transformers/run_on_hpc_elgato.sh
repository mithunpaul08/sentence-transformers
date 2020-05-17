#!/bin/bash
#PBS -q standard
#PBS -l select=1:ncpus=16:mem=250gb:ngpus=1:pcmem=16gb
### Specify a name for the job
#PBS -N elgato_
### Specify the group name
#PBS -W group_list=msurdeanu
### Used if job requires partial node only
#PBS -l place=free:exclhost
### CPUtime required in hhh:mm:ss.
### Leading 0's can be omitted e.g 48:0:0 sets 48 hours
#PBS -l cput=672:00:00
### Walltime is how long your job will run
#PBS -l walltime=24:00:00


### Optional. Request email when job begins and ends
# PBS -m bea
### Optional. Specify email address to use for notification
# PBS -M mithunpaul@email.arizona.edu

### Joins standard error and standard out
#PBS -j oe


module load singularity/3.2.1
export PYTHONPATH="/home/u11/mithunpaul/sentence-transformers/"
cd /home/u11/mithunpaul/sentence-transformers
pip install -r requirements.txt
cd /home/u11/mithunpaul/sentence-transformers/examples
bash get_convert_zip_fact_verification_files.sh
cd /home/u11/mithunpaul/sentence-transformers/examples/training_transformers
python training_nli.py

