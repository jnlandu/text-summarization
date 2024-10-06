import torch
from transformers import pipeline

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
summarizer = pipeline(task="summarization", model="Falconsai/text_summarization", device=device)
