"""
The system trains BERT (or any other transformer model like RoBERTa, DistilBERT etc.) on the SNLI + MultiNLI (AllNLI) dataset
with softmax loss function. At every 1000 training steps, the model is evaluated on the
STS benchmark dataset

Usage:
python training_nli.py

OR
python training_nli.py pretrained_transformer_model_name
"""
from comet_ml import Experiment,ExistingExperiment
from torch.utils.data import DataLoader
import math
from sentence_transformers import models, losses
from sentence_transformers import SentencesDataset, LoggingHandler, SentenceTransformer
from sentence_transformers.evaluation import LabelAccuracyEvaluator
from sentence_transformers.readers import *
import logging
from datetime import datetime
import sys
from sentence_transformers.readers import NLIDataReader


def initialize_comet():
    # for drawing graphs on comet:
    comet_Expt_object=None
    comet_Expt_object = Experiment(api_key="XUbi4cShweB6drrJ5eAKMT6FT", project_name="rte-decomp-attention")

    return comet_Expt_object

#### Just some code to print debug information to stdout
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[LoggingHandler()])
comet_value_updater=initialize_comet()
if (comet_value_updater) is not None:
    hyper_params = vars()
    comet_value_updater.log_parameters(hyper_params)




#You can specify any huggingface/transformers pre-trained model here, for example, bert-base-uncased, roberta-base, xlm-roberta-base
model_name = sys.argv[1] if len(sys.argv) > 1 else 'bert-base-uncased'


# Read the dataset
batch_size = 32
nli_reader_fever = NLIDataReader('../datasets/rte/fever/allnli')
nli_reader_fnc = NLIDataReader('../datasets/rte/fnc/allnli')
train_num_labels = nli_reader_fever.get_num_labels()
model_save_path = 'output/training_nli_'+model_name.replace("/", "-")+'-'+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# Use Huggingface/transformers model (like BERT, RoBERTa, XLNet, XLM-R) for mapping tokens to embeddings
word_embedding_model = models.Transformer(model_name)

# Apply mean pooling to get one fixed sized sentence vector
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                               pooling_mode_mean_tokens=True,
                               pooling_mode_cls_token=False,
                               pooling_mode_max_tokens=False)

model = SentenceTransformer(modules=[word_embedding_model, pooling_model])


# Convert the dataset to a DataLoader ready for training
logging.info("Read fever train dataset")

train_data = SentencesDataset(nli_reader_fever.get_examples('train.gz'), model=model)
train_dataloader = DataLoader(train_data, shuffle=True, batch_size=batch_size)
train_loss = losses.SoftmaxLoss(model=model, sentence_embedding_dimension=model.get_sentence_embedding_dimension(), num_labels=train_num_labels)



logging.info("Read fever dev dataset")
dev_data = SentencesDataset(nli_reader_fever.get_examples('dev.gz'), model=model)
dev_dataloader = DataLoader(dev_data, shuffle=False, batch_size=batch_size)
evaluator = LabelAccuracyEvaluator(dev_dataloader,softmax_model = train_loss,grapher=comet_value_updater)



# Configure the training
num_epochs = 1

warmup_steps = math.ceil(len(train_dataloader) * num_epochs / batch_size * 0.1) #10% of train data for warm-up
logging.info("Warmup-steps: {}".format(warmup_steps))



# Train the model
model.fit(train_objectives=[(train_dataloader, train_loss)],
          evaluator=evaluator,
          epochs=num_epochs,
          evaluation_steps=1000,
          warmup_steps=warmup_steps,
          output_path=model_save_path
          )



##############################################################################
#
# Load the stored model and evaluate its performance on fnc dataset
#
##############################################################################


logging.info("Read fnc dev dataset")

model = SentenceTransformer(model_save_path)
test_data = SentencesDataset(nli_reader_fnc.get_examples('dev.gz'), model=model)
test_dataloader = DataLoader(test_data, shuffle=False, batch_size=batch_size)
evaluator = LabelAccuracyEvaluator(test_dataloader,softmax_model = train_loss,grapher=comet_value_updater)
model.evaluate(evaluator)
