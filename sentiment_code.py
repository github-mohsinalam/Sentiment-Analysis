def strip_punctuation(word):
    """removes characters considered punctuation from everywhere in the word"""
    for char in punctuation_chars:
        if char in word:
            word = word.replace(char,'')
    return word



def get_pos(sentence):
    '''Returns the count of positive words in a sentence''' 
    words = sentence.split()
    count = 0
    for word in words :
        word = strip_punctuation(word)
        word = word.lower()
        if word in positive_words:
            count = count+1
    return count



def get_neg(sentence):
    '''Returns the count of negative words in a sentence''' 
    words = sentence.split()
    count = 0
    for word in words:
        word = strip_punctuation(word)
        word = word.lower()
        if word in negative_words:
            count = count+1
    return count




punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

            
resulting_data = open('resulting_data.csv', 'w')
resulting_data.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
resulting_data.write('\n')
            
            
            
with open('project_twitter_data.csv') as project_twitter_data:
    header = project_twitter_data.readline()
    line = 0
    for row in project_twitter_data:
        row = row.strip()
        item = row.split(',')
        NumberOfRetweets = item[1]
        NumberOfReplies = item[2]
        PositiveScore = get_pos(item[0])
        NegativeScore = get_neg(item[0])
        NetScore = PositiveScore - NegativeScore
        row_string = '{}, {}, {}, {}, {}'.format(NumberOfRetweets, NumberOfReplies, PositiveScore, NegativeScore, NetScore)    
        resulting_data.write(row_string)
        resulting_data.write('\n')
        
        
resulting_data.close()
   
