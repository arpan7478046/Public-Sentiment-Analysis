import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import os
import googleapiclient.discovery



def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "YOUR_API_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=376,         # No of comments need to extract
        videoId='e_UYhqrL8ic'   # Video Id of the Youtube Video
    )
    response = request.execute()

    i = 0
    data2 = []
    for i in range(len(response['items'])):
        data = response['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']
        data2 += [data]
        i +=1
    
    return(data2)


# reading text file
text = ""
text_comments = main()
length = len(text_comments)


for i in range(0, length):
    text = text_comments[i] + " " + text


# converting to lowercase
lower_case = text.lower()


# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


# Get emotions text
emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    
    print(neg)
    print(pos)

    if neg > pos:
        print('Negative')
    elif pos > neg:
        print('Positive')
    else:
        print('Neutral')

# Sentiment score of the cleaned text
sentiment_analyse(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()