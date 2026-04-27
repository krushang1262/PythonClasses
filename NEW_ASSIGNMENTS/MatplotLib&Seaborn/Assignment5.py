import pandas as pd 
import matplotlib.pyplot as plt

from wordcloud import WordCloud

# 5) A word cloud of the different causes of death (remove the string "Cause
# of Death:" for best results) 

df = pd.read_csv('~/Desktop/AssignmentData/U.S.Death.csv')

word = df['cause'].str.replace('Cause of Death:','', regex=False)
text = " ".join(word.dropna().astype(str))
print(word)

plt.figure(figsize=(10,6))
wc = WordCloud(width=800, height=800, background_color='white').generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Causes of Death")
          
plt.show()