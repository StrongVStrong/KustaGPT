import random
import json

# Paths to your original JSONL files
input_jsonl_files = [
    'assets/kusta_gc_messages_with_prompts.jsonl',
    'assets/kusta_messages_for_training.jsonl',
    'assets/kusta_messages_with_prompts.jsonl'
]

# Paths to save the new JSONL files for training and validation data
train_jsonl_file = 'assets/train_data.jsonl'
validation_jsonl_file = 'assets/validation_data.jsonl'

# Read all lines from the input files
all_lines = []
for file_path in input_jsonl_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        all_lines.extend(f.readlines())

# Shuffle the data to ensure randomness
random.shuffle(all_lines)

# Split the data into 90% training and 10% validation
split_index = int(0.9 * len(all_lines))
train_lines = all_lines[:split_index]
validation_lines = all_lines[split_index:]

# Write the training data to the new JSONL file
with open(train_jsonl_file, 'w', encoding='utf-8') as f:
    for line in train_lines:
        f.write(line)

# Write the validation data to the new JSONL file
with open(validation_jsonl_file, 'w', encoding='utf-8') as f:
    for line in validation_lines:
        f.write(line)

print(f"Training data saved to {train_jsonl_file}")
print(f"Validation data saved to {validation_jsonl_file}")
