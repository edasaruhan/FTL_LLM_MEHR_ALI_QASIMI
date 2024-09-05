
# Step 1: Installing required libraries
# Run this cell to install necessary libraries
!pip install transformers 

!pip install torch 
!pip install streamlit

# Step 2: Importing necessary libraries
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

# Step 3: Loading the model and tokenizer
model_name = "bigscience/bloom-560m"  # You can change this to another model like GPT-2
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 4: Defining the text generation function
def generate_text(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Step 5: Setting up Streamlit for the user interface
def main():
    st.title("SDG Text Generation App")
    st.write("Generate text based on Sustainable Development Goals (SDG) prompts.")
    
    prompt = st.text_input("Enter your prompt related to SDGs")
    
    if prompt:
        generated_text = generate_text(prompt)
        st.write("Generated Text:", generated_text)

# Step 6: Running the application
if __name__ == '__main__':
    main()