# Read text from a file, and count the occurence of words in that text
# Example:
#count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    filename=open(filename,'r')
    print(filename.read())

read_file_content("story.txt")

def count_words():
    text = read_file_content("./story.txt")
    f = "story.txt"
    f = open(f,'r')
    # [assignment] Add your code here
    wli = []

    for l in f:
        l = l.split()

        for w in l:
            wli.append(w)
    wli.sort()

    wd = {}

    for w in wli:
        wd[w] = wli.count(w)

    print('\n{:^4}{:^4}'.format('Word',":"'Count')) # format columns with headers
    for w in wd:
        print('{:^4}{:^4d}'.format(w,wd[w]))
count_words()
