#%%from bs4 import BeautifulSoup
import os

from bs4 import BeautifulSoup

# Load the HTML file
html_file_path = 'index.html'

with open(html_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Remove script and style elements
for script in soup(['script', 'style']):
    script.extract()

# Extract text
text = soup.get_text()

# Break into lines and remove leading/trailing space on each
lines = (line.strip() for line in text.splitlines())

# Drop blank lines
clean_text = '\n'.join(line for line in lines if line)

print(clean_text)

# %%
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords') 

# Tokenization
tokens = word_tokenize(clean_text)

# Remove punctuation and stopwords
stop_words = set(stopwords.words('english'))
words = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]

print(words)


# %%
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# %%
