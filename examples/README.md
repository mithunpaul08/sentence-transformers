# to run training on fever files and test on fnc
- `pip install -r requirements.txt`

- add this to your ~/.bashrc preferably
`export PYTHONPATH="/Users/mordor/research/sentence-transformers/"`

- install right version of pytorch manually.
eg:`pip install torch==1.5.0+cu101 torchvision==0.6.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html`

- `./get_convert_zip_fact_verification_file.sh`

- `cd sentence-transformers/examples`
- `python trainining_transformers/training_nli.py`

or on hpc
cd examples/training_transformers
qsub <run_on_hpc_elgato.sh

# Examples
This folder contains various examples how to use SentenceTransformers.

##Datasets
The [datasets](datasets/) folder stores datasets that are used in these examples. To download these datasets, run in the dataset folder:
```
python get_data.py
```


##Applications
The [applications](applications/) folder contains examples how to use SentenceTransformers for tasks like clustering or semantic search.

##Training Transformers
The [training_transformers](training_transformers/) folder contains examples how to fine-tune transformer models like BERT, RoBERTa, or XLM-RoBERTa for generating sentence embedding.

Further, it contains examples for **multi-task-learning** and **multilingual-learning**.

##Training Basic Models
The [training_basic_models](training_basic_models/) show some examples how to train simple models like average word embeddings, Tf-Idf. Further, it has some more complex models based on Deep Averaging Networks (DAN), CNN, and LSTM.

These example are great if a high speed for sentence embedding generation is needed.

##Evaluation
The [evaluation](evaluation/) folder contains some examples how to evaluate SentenceTransformer models for common tasks.