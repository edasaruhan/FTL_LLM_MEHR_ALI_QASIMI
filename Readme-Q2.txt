# Text Embedding Classification Project

## Overview
This project demonstrates the use of various text embedding techniques, including Word2Vec, GloVe, and BERT, applied to a text classification task. The goal is to compare the performance of these embeddings in a logistic regression model for classifying text data.

## Steps in the Project
1. **Data Loading and Exploration**: The dataset is loaded, visualized, and explored to understand the distribution of text samples across different categories.

2. **Text Preprocessing**: The text is cleaned by removing special characters, URLs, and stop words, and then prepared for embedding.

3. **Embedding Techniques**:
    - **Word2Vec**: A Word2Vec model is trained on the dataset and used to convert text into embeddings.
    - **GloVe**: Pre-trained GloVe embeddings are used to represent the text.
    - **BERT**: A pre-trained BERT model is applied to generate contextualized embeddings.

4. **Model Training and Evaluation**: Logistic regression is used to classify the text based on the embeddings, and the models are evaluated using accuracy, precision, recall, and F1-score.

5. **Results Visualization**: A comparison of the results is visualized through bar charts showing the performance of each model.

## Prerequisites
Before running the project, ensure you have the following libraries installed:
- pandas
- matplotlib
- seaborn
- gensim
- transformers
- torch
- sklearn

To install the required dependencies, you can run:
pip install pandas matplotlib seaborn gensim transformers torch scikit-learn
Dataset
The dataset used in this project is a collection of text samples with corresponding labels. The text data is categorized into different classes, such as politics, business, sports, etc. You can replace the dataset file ('data.csv') with any text classification dataset of your choice.

Files Included
Text_Embedding_Classification_Project.ipynb: Jupyter notebook with the complete code for the project.

README.md: Documentation about the project.

Instructions for Running

Data Preparation: Ensure your dataset is named data.csv and located in the same directory as the notebook.

Running the Notebook: Open the Jupyter notebook and run each cell step by step.

Results: At the end of the notebook, you will find visualizations comparing the performance of Word2Vec, GloVe, and BERT embeddings.

Results Summary
Word2Vec: Fast and efficient, but limited in its ability to capture context and word polysemy.
GloVe: Strong semantic relationships but requires global context, making it slower in some applications.
BERT: Provides the best performance but is computationally expensive and slow to train.

Conclusion
This project highlights the strengths and weaknesses of different embedding techniques for text classification tasks. BERT performs best in terms of accuracy and contextual understanding, while Word2Vec and GloVe offer faster but less context-aware alternatives.