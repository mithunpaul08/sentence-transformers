import pandas as pd
import os



def read_fever_format_write_to_allnli_format(train_lex_file,run_name):
    """Load dataset

    Args:
        args (str): all arguments which were create initially.
    Returns:
        an instance of ReviewDataset
    """

    claim_ev_lex= pd.read_json(train_lex_file, lines=True)

    s1_filename = os.path.join("../../datasets/rte/fever/", "s1." + run_name)
    with open(s1_filename, 'w') as outfile:
        for claim in (claim_ev_lex.claim):
            outfile.write(claim + "\n")


    s2_filename = os.path.join("../../datasets/rte/fever/", "s2." + run_name)
    with open(s2_filename, 'w') as outfile:
        for ev in (claim_ev_lex.evidence):
            outfile.write(ev+"\n")

    labels_filename = os.path.join("../../datasets/rte/fever/", "labels." + run_name)
    with open(labels_filename, 'w') as outfile:
        for label in (claim_ev_lex.label):
            outfile.write(label.lower()+"\n")

#convert from fever format. this should be run only once
read_fever_format_write_to_allnli_format("../../datasets/rte/fever/train/fever_train_lex.jsonl","train")
read_fever_format_write_to_allnli_format("../../datasets/rte/fever/dev/fever_dev_lex.jsonl","dev")
