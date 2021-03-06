# Sentiment-Analysis
Final Project of the course Python Functions, Files, and Dictionaries. This course is part of the Python 3 Programming Specialization offer by University of Michigan on Coursera. You can find more information at https://www.coursera.org/learn/python-functions-files-dictionaries/
- This repo covers making of a sentiment classifier in PYTHON.
- A .csv file containing text of tweets,number of retweets,number of replies is provided.
- Words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt have been provided.
- Task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
- For detailed description of the mini prject read **problem_statement.txt**

## Functions
1. **strip_punctuation(word):**  
   which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word.   
 
2. **get_pos(sentence) :**   
    which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words.   
    Use the list, positive_words to determine what words will count as positive.
    The function should return a positive integer-  how many occurrences there are of positive words in the text.
3. **get_neg(sentence) :**  
     which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words.
     Use the list, negative_words to determine what words will count as negative.
     The function should return a positive integer - how many occurrences there are of negative words in the text

## Inspiraion 
- This mini project is inspired by : 
#### Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews."
       Proceedings of the ACM SIGKDD International Conference on Knowledge
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle,
       Washington, USA,
#### Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing and Comparing Opinions on the Web."
      Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14,
      2005, Chiba, Japan.


