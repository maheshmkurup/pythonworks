def longest_palindromic_substring(s):

    reversed_string=[]

    for ch in s:

        reversed_string.append(ch)

    reverred_string=reversed_string.reverse()

    if s==reverred_string:

        print(reversed_string)

longest_palindromic_substring("racecar")



