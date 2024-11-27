print("*"*20,"Welcome to Fashion Sensei","*"*20)
print("\n","Choose from the below Options")
import pandas as pd
import cv2
import os
from pathlib import Path
df = pd.read_csv('labeled_data.csv')

# Resetting index if 'Color' is set as index
df.reset_index(inplace=True)
#df.info()

df['color'] = df['color'].str.lower()
df['Type'] = df['Type'].str.lower()
df['Pattern'] = df['Pattern'].str.lower()
df['Category'] = df['Category'].str.lower()
df['data'] = df['color'] + ' ' + df['Type'] + ' ' + df['Pattern'] + ' ' + df['Category']
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df['data'])

from sklearn.metrics.pairwise import cosine_similarity

similarities = cosine_similarity(vectorized)
#print(similarities)

print("-"*65)
print("color\t\t|Type\t\t|Pattern\t\t|Category")
print("-"*65)
print("red\t\t|ethnic\t\t|Plain\t\t\t|Top")
print("pink\t\t|Western\t|Printed\t\t|Jeans")
print("black\t\t|\t\t|Striped\t\t|Shorts")
print("blue\t\t|\t\t|Butterfly\t\t|Shirt")
print("white\t\t|\t\t|Check\t\t\t|T-shirt")
print("navy blue\t|\t\t|Floral\t\t\t|Plazo")
print("purple\t\t|\t\t|Flowers\t\t|Jumpsuit")
print("brown\t\t|\t\t|Plain\t\t\t|Saree")
print("mix\t\t|\t\t|Dotted\t\t\t|Kurti")
print("light blue\t|\t\t|embroidery\t\t|Suit")
print("lavendar\t|\t\t|Strips\t\t\t|Skirt")
print("cream\t\t|\t\t|\t\t\t|Dress")
print("grey\t\t|\t\t|\t\t\t|Pants")
print("green\t\t|\t\t|\t\t\t|Leggings")
print("beige\t\t|\t\t|\t\t\t|Jacket")
print("Magenta\t\t|\t\t|\t\t\t|Kurta")
print("Sky blue\t|\t\t|\t\t\t|")
print("Light pink\t|\t\t|\t\t\t|")
print("Sea Green\t|\t\t|\t\t\t|")
print("Yellow\t\t|\t\t|\t\t\t|")
print("Grey\t\t|\t\t|\t\t\t|")
print("-"*65,"\n")
# Take user input for preferences
user_color = input("Enter preferred color: ").lower()
user_type = input("Enter preferred type: ").lower()
user_pattern = input("Enter preferred pattern: ").lower()
user_category = input("Enter preferred category: ").lower()

# Combine user preferences into one string
user_data = user_color + ' ' + user_type + ' ' + user_pattern + ' ' + user_category

# Calculate cosine similarity between user preferences and dataset
user_vectorized = vectorizer.transform([user_data])
similarities = cosine_similarity(user_vectorized, vectorized)

# Get indices of top recommendations
top_indices = similarities.argsort(axis=1)[:, -5:].flatten()

# Print recommended items
print("Top recommendations:")

for idx in reversed(top_indices):
    print(df.iloc[idx]['S.NO.'])
    image=cv2.imread("C:/Users/anany/OneDrive/Documents/Project sem 4/final dataset/"+str(df.iloc[idx]['S.NO.'])+".png")
    cv2.imshow("recommendation",image)
    cv2.waitKey(0)

