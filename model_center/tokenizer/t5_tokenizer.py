# coding=utf-8

# The current implementation is mainly to adapt the training framework of the Transformers toolkit, 
# and replace the original model implementation.
# TODO we will change to our SAM implementation in the future, which will be a more efficient tokenizer

from transformers import T5Tokenizer as transformers_T5Tokenizer

T5Tokenizer = transformers_T5Tokenizer
