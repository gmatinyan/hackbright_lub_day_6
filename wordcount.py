def count_words(file):

    open_file = open('./twain.txt')

    words_count = {}

    for line in open_file:
        line = line.rstrip()
        words = line.split()
        
        for word in words:
            word = word.lower()
            word = word.strip("':(,;.\")?!_-")
            words_count[word] = words_count.get(word, 0) + 1

    for word, count in words_count.iteritems():
        print word, count
    

    open_file.close()

#count_words('./test.txt')
count_words('./twain.txt')
