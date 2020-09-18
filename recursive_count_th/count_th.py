'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    try:
        th_index = word.index('th')
        return 1 + count_th(word[th_index+2:])
    except:
        return 0
    
print(count_th("")) #0
print(count_th("abcthxyz")) #1
print(count_th("abcthefthghith")) #3
print(count_th("thhtthht")) #2
print(count_th("THtHThth")) #1

#Here I am using the index method to find substring of "th" occurring in the word I pass into the function count_th.

#Recursively, I call the function itself each time, which will pass through the word and find how many times "th" occurs, and then will cut off the first 2 indexes and move through the word again, until it finds 0. 