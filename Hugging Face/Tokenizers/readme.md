
# Hugging Face Tokenizers Library

This repository provides an introduction to the **Hugging Face Tokenizers library**, a fast and flexible tool for tokenizing text data used in natural language processing (NLP) models.

---

## What is a Tokenizer?

A **tokenizer** converts raw text into tokens (smaller units) that models can understand. For example:

```
"I love NLP!"
```

might be tokenized into:

```
["I", "love", "NL", "##P", "!"]
```

and then converted to token IDs like `[101, 1045, 2293, 17953, 999, 102]` to feed into transformer models.

---

## Why Use the Tokenizers Library?

- **Blazing Fast:** Written in Rust for high speed.
- **Flexible:** Supports many tokenization algorithms like BPE, WordPiece, Unigram.
- **Customizable:** Build and train your own tokenizers.
- **Compatible:** Integrates smoothly with Hugging Face Transformers.
- **Low-level API:** Gives more control over tokenization process.

---

## Installation

```bash
pip install tokenizers
```

---

## Basic Usage Example

```python
from tokenizers import Tokenizer

# Load a pre-trained tokenizer JSON file (e.g. from Hugging Face)
tokenizer = Tokenizer.from_file("bert-base-uncased-tokenizer.json")

output = tokenizer.encode("Hello, world!")
print("Tokens:", output.tokens)
print("Token IDs:", output.ids)
```

---

## Building a Custom Tokenizer

```python
from tokenizers import Tokenizer, models, pre_tokenizers, trainers

# Initialize a BPE tokenizer
tokenizer = Tokenizer(models.BPE())

# Use whitespace pre-tokenizer
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

# Define trainer with special tokens
trainer = trainers.BpeTrainer(special_tokens=["[PAD]", "[CLS]", "[SEP]", "[UNK]", "[MASK]"])

# Train tokenizer on your text files
tokenizer.train(["data.txt"], trainer)

# Save tokenizer to disk
tokenizer.save("custom-tokenizer.json")
```

---

## Integration with Transformers

If you use Hugging Face Transformers, you usually use the high-level `AutoTokenizer` class:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer("Hello, world!", return_tensors="pt")
print(tokens)
```

---

## Learn More

- [Tokenizers Documentation](https://huggingface.co/docs/tokenizers/index)
- [Transformers Documentation](https://huggingface.co/docs/transformers/index)

---

## License

This project is licensed under the MIT License.
