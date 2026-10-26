import numpy as np
import matplotlib.pyplot as plt
from transformers import pipeline

np.random.seed(0)

X = np.random.rand(4, 4)
Q = X @ np.random.rand(4, 4)
K = X @ np.random.rand(4, 4)
V = X @ np.random.rand(4, 4)

def attention(q, k, v):
    scores = q @ k.T / np.sqrt(q.shape[1])
    scores = scores - scores.max(axis=1, keepdims=True)
    exp = np.exp(scores)
    weights = exp / exp.sum(axis=1, keepdims=True)
    return weights, weights @ v

weights, output = attention(Q, K, V)

print("Attention weights (4x4):")
print(np.round(weights, 3))
print("Row sums:", np.round(weights.sum(axis=1), 3))
print("Valid:", np.allclose(weights.sum(axis=1), 1))

heads = []

for i in range(2):
    start = i * 2
    end = start + 2
    w, result = attention(Q[:, start:end],
                          K[:, start:end],
                          V[:, start:end])
    heads.append(result)

combined = np.concatenate(heads, axis=1)
multi_output = combined @ np.random.rand(4, 4)

print("Multi-head output shape:", multi_output.shape)

pos = np.arange(10)[:, None]
dims = np.arange(8)[None, :]
angles = pos / (10000 ** (2 * (dims // 2) / 8))

encoding = np.zeros((10, 8))
encoding[:, 0::2] = np.sin(angles[:, 0::2])
encoding[:, 1::2] = np.cos(angles[:, 1::2])

plt.imshow(encoding, aspect="auto")
plt.colorbar()
plt.xlabel("Dimensions")
plt.ylabel("Positions")
plt.title("Positional Encoding")
plt.savefig("outputs/task_3_positional_encoding.png")
plt.show()

bert = pipeline("fill-mask", model="bert-base-uncased")
result = bert("Paris is the [MASK] of France.", top_k=1)
print("BERT:", result[0]["token_str"])

gpt = pipeline("text-generation", model="gpt2")
result = gpt("Artificial intelligence will",
             max_new_tokens=30, pad_token_id=50256)
print("GPT-2:", result[0]["generated_text"])