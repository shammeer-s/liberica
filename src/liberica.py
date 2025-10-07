import torch.nn as nn
from torchtext.data.metrics import bleu_score

def evaluate_bleu_simple(Model):
    """
    Demonstrates a simple BLEU score evaluation for a mock PyTorch model.
    """
    vocab_size = 10
    mock_model = Model(vocab_size)

    # Example candidate and reference sentences (as integer sequences)
    # In a real scenario, you'd get these from a tokenizer.
    candidate_sentence = [[6, 2, 7, 4, 9]]
    reference_corpus = [[[6, 2, 7, 4, 5]], [[6, 2, 8, 4, 9]]]

    # Convert to string tokens for bleu_score function
    candidate_tokens = [str(token) for token in candidate_sentence[0]]
    reference_tokens_1 = [[str(token) for token in reference_corpus[0][0]]]
    reference_tokens_2 = [[str(token) for token in reference_corpus[1][0]]]

    # In a real evaluation, you would loop through your entire test dataset
    # and accumulate the scores.
    score = bleu_score([candidate_tokens], reference_tokens_1 + reference_tokens_2)

    print(f"Candidate Sentence: {candidate_sentence[0]}")
    print(f"Reference Corpus 1: {reference_corpus[0][0]}")
    print(f"Reference Corpus 2: {reference_corpus[1][0]}")
    print(f"BLEU score: {score}")

class MockSeq2Seq(nn.Module):
    def __init__(self, vocab_size):
        super(MockSeq2Seq, self).__init__()
        self.linear = nn.Linear(vocab_size, vocab_size)

    def forward(self, x):
        return self.linear(x)

if __name__ == '__main__':
    evaluate_bleu_simple(MockSeq2Seq)
