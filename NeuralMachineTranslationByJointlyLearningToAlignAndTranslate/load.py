# Load Data
import torch 
from torchtext.datasets import Multi30k
from torchtext.data import BucketIterator
from tokenizer import SRC, TRG


train_data, valid_data, test_data = Multi30k.splits(exts = ('.de', '.en'), 
                                                    fields = (SRC, TRG))

# Build vocab
SRC.build_vocab(train_data, min_freq=2)
TRG.build_vocab(train_data, min_freq=2)

# Define Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Create the iterators.
BATCH_SIZE = 64

train_iterator, valid_iterator, test_iterator = BucketIterator.splits(
    (train_data, valid_data, test_data),
    batch_size = BATCH_SIZE,
    device=device)


if __name__ == "__main__":
    for i in train_iterator:
        print(i)
        break