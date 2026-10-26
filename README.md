# LLM Evaluation Toolkit

## Project overview
This project evaluates LLM capabilities, limitations, token costs, transformer and prompt engineering.

## Technologies
- Python
- Groq API
- Numpy
- Tiktoken
- Hugging face
- Matplotlib
- Pydantic

## Comparison table:
| Model | Owner | Weights | Context window | Stengths |
|---|---|---|---|---|
| GPT-4.1 | OpenAI | Closed | 1,047,576 | Coding, reasoning |
| Claude sonnet 4.5 | Anthropic | Closed | 200K | Writing, analysis |
| Llama 4 scout | Meta | Open-weight | 10M | Self-hosting, multimodel |
| Gemini 2.5 pro | Google | Closed | 1,048,576 | Long-context, multimodal |

## Five safeguards:
- Verify important information
- Validate model outputs
- Use human review for critical decisions
- Prevent unsupported or invented answers
- Apply security, logging and input limits

## Encoder vs Decoder:
- BERT is an encoder-only model
- It reads input bidirectionally
- It is useful for classification and extraction
- GPT is a decoder-only model
- It generates text one token at a time
- Transformers largely replaced RNNs because attention enables parallel processing and better long-range modeling