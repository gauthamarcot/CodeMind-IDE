import logging
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize logging
logging.basicConfig(level=logging.INFO)

class GPTResponder:
    def __init__(self, model_name='gpt2'):
        self.model_name = model_name
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    def generate_response(self, query):
        try:
            inputs = self.tokenizer.encode(query, return_tensors='pt')
            outputs = self.model.generate(inputs, max_length=150, do_sample=True)
            text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return text
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "Error generating response"
