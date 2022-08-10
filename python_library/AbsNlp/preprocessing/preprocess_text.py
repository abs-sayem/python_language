def help():
    print("preprocess_text contains following modules:--")
    print(" textOnly(): it returns only text excluding everything without alpha characters, useful for keyword based search, user input/query processing")
    print(" preprocessForEmail(): it is a special type module only for email extraction.")
    print(" preprocessForDate(): it is a special type module only for date extraction.")
    print(" cleanText(): it returns full text excluding tabs, newline and links")

def textOnly(text):     # It will return the corpus containing only text(alpha) except everything else.
    import nltk
    import re
    import string
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    stemmer = nltk.SnowballStemmer('english')

    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\t', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stop_words]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return(text)

def preprocessForEmail(text):
    # Removing spaces
    import re
    #non_spaced_text = text.replace('\t','\n').split('\n')
    non_spaced_text = re.sub('\s+', ' ', text)
    
    # Remove Stopwords
    import nltk
    from nltk.corpus import stopwords
    stop_set = set(stopwords.words('english'))
    stopped_text = [word.lower() for word in non_spaced_text.split() if word.lower() not in stop_set]

    # Convert to string
    final_string_text = " ".join(stopped_text)
    
    return(final_string_text)

def preprocessForDate(text):
    import nltk
    import re
    import string
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    stemmer = nltk.SnowballStemmer('english')

    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\t', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stop_words]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return(text)

def cleanText(text):    # It return a plain corpus excluding punctuation, whiteshapes, tabs, links
    #import nltk
    import re
    #import string

    #text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    #text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\t', '', text)
    text = re.sub('\n', '', text)
    #text = re.sub('\w*\d\w*', '', text)

    return(text)