import re
def remove_noise(text):
    text=re.sub(r'http\S+','',text)
    text=re.sub(r'@\S+','',text)
    text=re.sub(r'#\S+','',text)
    text=re.sub(r'[^\w\S]','',text)
    text=re.sub(r'\S+','',text).strip()
    return text
text="just had the best coffee from @starbucks! #coffee #yum? http://starbucks.com"
clean_text=remove_noise(text)
print(clean_text)
    
