import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def generate_tags(title, description, num_tags =10):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(title + " " + description)
    words = [word.lower() for word in words if word.isalpha() and word not in stop_words]

    fdist = FreqDist(words)
    return [word for word, frequency in fdist.most_common(num_tags)]

if __name__ == "__main__":
    title = "YouTube Keyword Extractor in Python by @misterlooser"
    description = """
    In this video, we will learn how to use the power of Python to extract keywords from YouTube videos. Keyword extraction is a crucial part of optimizing your videos for search engines, and with the help of Python, it has never been easier.

We will start by understanding the basics of YouTube video optimization, including what keywords are and why they are important. Then, we will dive into the Python code and show you how to extract keywords from video titles, descriptions, and tags. We will also demonstrate how to use the extracted keywords to optimize your video and increase its visibility on YouTube.

By the end of this video, you will have a solid understanding of how to use Python to extract keywords from YouTube videos and use them to boost your video's ranking in search results. Whether you are a beginner or an experienced Python programmer, this video is perfect for anyone looking to improve their video optimization skills.

So, don't wait! Watch now and unlock the power of video optimization with the help of Python and the YouTube Keyword Extractor.
    """

    tags = generate_tags(title, description)
    print(tags)