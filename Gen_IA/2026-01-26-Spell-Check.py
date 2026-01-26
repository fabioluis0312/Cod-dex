from textblob import TextBlob

text = 'Oi Tudo bem? boa tarde.'

blob = TextBlob(text)

corrected_text = blob.correct()

# Print the corrected text
print('Original Text:', text)
print('Corrected Text:', corrected_text)