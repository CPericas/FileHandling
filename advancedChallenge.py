#Task 1: Travel Blog Sentiment Analysis:
#Problem Statement: Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. Identify and count the
# occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").
#- Dataset Example:  
#Entries:
#"Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."
#"The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."
#"The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."
#"Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."
#"Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."
#"We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."
#"The food on our trip was excellent. We sampled delicious local cuisine at every stop."
#"The historical tour was enlightening. We learned so much about the culture and heritage of the region."
#"Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!" "> Travel Blog 
# Entries:
#"Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."
#"The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."
#"The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."
#"Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."
#"Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."
#"We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."
#"The food on our trip was excellent. We sampled delicious local cuisine at every stop."
#"The historical tour was enlightening. We learned so much about the culture and heritage of the region."
#"Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!" ```
#Expected Outcome: A summary report indicating the number of positive and negative words in the travel blogs, demonstrating the ability 
# to process text data and apply basic sentiment analysis.


import re
import string

# Define lists of positive and negative words
positive_words = ["amazing", "enjoy", "beautiful", "wonderful", "breathtaking", "relaxed", "soaked", "memorable", "excellent", "delicious", "fantastic", "unforgettable", "mesmerizing", "unique", "stunning", "enlightening"]
negative_words = ["bad", "disappointing", "poor", "lackluster", "scarce", "overcrowded", "rain"]

def count_sentiment_words(text, sentiment_words):
    # Normalize the text by converting to lowercase and removing punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Count occurrences of each word in the sentiment words list
    count = 0
    for word in sentiment_words:
        word = word.lower()  # Convert word to lowercase to ensure case insensitivity
        word_count = len(re.findall(r'\b' + re.escape(word) + r'\b', text))
        count += word_count
    return count

def analyze_sentiment(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        positive_count = count_sentiment_words(text, positive_words)
        negative_count = count_sentiment_words(text, negative_words)

        return positive_count, negative_count

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

# Example usage
if __name__ == "__main__":
    positive_count, negative_count = analyze_sentiment('travel_blogs.txt')
    print(f"Number of positive words: {positive_count}")
    print(f"Number of negative words: {negative_count}")







#Task 2: Historical Weather Data Compiler
#Problem Statement: Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). Each 
# file contains daily temperature data. Calculate the average temperature for each year and identify the year with the highest average.
#- Dataset Example:
#File: weather_2020.txt
#python def analyze_blog_sentiments(blog_file): # Implement sentiment analysis logic on the blog file
#Code Example:
#2020-01-01,5°C 2020-01-15,6°C 2020-02-05,4°C 2020-02-20,7°C 2020-03-10,8°C 2020-03-25,9°C 2020-04-05,12°C 2020-04-20,14°C 2020-05-05,
# 17°C 2020-05-20,19°C 2020-06-05,22°C 2020-06-20,25°C 2020-07-05,28°C 2020-07-20,30°C 2020-08-05,32°C 2020-08-20,31°C 2020-09-05,27°C 
# 2020-09-20,24°C 2020-10-05,19°C 2020-10-20,16°C 2020-11-05,11°C 2020-11-20,9°C 2020-12-05,6°C 2020-12-20,4°C



