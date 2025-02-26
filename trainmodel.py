from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset
import torch

# Path to your GGUF model
model_path = 'assets/Meta-Llama-3.1-8B-Instruct-abliterated'  # Update to the path where your GGUF model is stored
gguf_file = f'{model_path}/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf'

# Load the tokenizer and model with GGUF support
tokenizer = AutoTokenizer.from_pretrained(model_path, gguf_file=gguf_file)
model = AutoModelForCausalLM.from_pretrained(model_path, gguf_file=gguf_file)

# Load the dataset from the JSONL file
dataset = load_dataset('json', data_files='assets/transformed_train_data_with_correct_output.json')  # Update with your JSONL file path

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples['instruction'], truncation=True, padding="max_length", max_length=512)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./results",          # Output directory for model checkpoints
    evaluation_strategy="epoch",     # Evaluate at the end of each epoch
    learning_rate=2e-5,              # Learning rate
    per_device_train_batch_size=2,   # Batch size for training
    per_device_eval_batch_size=2,    # Batch size for evaluation
    num_train_epochs=3,              # Number of epochs
    weight_decay=0.01,               # Weight decay for regularization
    save_strategy="epoch",           # Save model every epoch
    logging_dir="./logs",            # Directory for logs
)

# Initialize Trainer
trainer = Trainer(
    model=model,                     # The model to train
    args=training_args,              # Training arguments
    train_dataset=tokenized_datasets['train'],   # Training dataset
    eval_dataset=tokenized_datasets['test'],     # Validation dataset
)

# Start fine-tuning
trainer.train()
