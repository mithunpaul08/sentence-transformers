from . import InputExample
import csv
import gzip
import os
import logging

class NLIDataReader(object):
    """
    Reads in the Stanford NLI dataset and the MultiGenre NLI dataset
    """
    def __init__(self, dataset_folder):
        self.dataset_folder = dataset_folder

    def get_examples(self, filename, max_examples=0):
        logging.info("inside get_examples")
        """
        data_splits specified which data split to use (train, dev, test).
        Expects that self.dataset_folder contains the files s1.$data_split.gz,  s2.$data_split.gz,
        labels.$data_split.gz, e.g., for the train split, s1.train.gz, s2.train.gz, labels.train.gz
        """
        s1 = gzip.open(os.path.join(self.dataset_folder, 's1.' + filename),
                       mode="rt", encoding="utf-8").readlines()
        s2 = gzip.open(os.path.join(self.dataset_folder, 's2.' + filename),
                       mode="rt", encoding="utf-8").readlines()
        labels = gzip.open(os.path.join(self.dataset_folder, 'labels.' + filename),
                           mode="rt", encoding="utf-8").readlines()

        examples = []
        id = 0
        for sentence_a, sentence_b, label in zip(s1, s2, labels):
            label=label.rstrip("\n")
            #logging.info(f"label:{label}")
            guid = "%s-%d" % (filename, id)
            id += 1
            examples.append(InputExample(guid=guid, texts=[sentence_a, sentence_b], label=self.map_label(label.rstrip("\n"))))

            if 0 < max_examples <= len(examples):
                break

        return examples

    @staticmethod
    def get_labels():
        return {"agree": 0, "disagree": 1, "discuss": 2, "unrelated": 3}

    def get_num_labels(self):
        return len(self.get_labels())

    def map_label(self, label):
        #print(f"printin{label}g ")
        #print(label)
        #logging.info(f"value of this label is {label}")
        after_strip=label.strip().lower()
        #logging.info(f"value of after strip label is {after_strip}" )
        return self.get_labels()[after_strip]