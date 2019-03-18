list_of_words=[]
def main():
    f=open("input.txt", "r")
    fl =f.readlines()
    for x in fl:
        almost_equal(fl, x,list_of_words)
    print(list_of_words)
    print(remove_duplicated_letter(list_of_words))

def almost_equal(set_of_words,comparison_word,list_of_words):
    for word in set_of_words:
        amount = 0
        n_word = len(word)
        for i in range(n_word):
            if comparison_word[i] != word[i]:
                amount += 1
            if amount == 2:
                break
        if amount == 1:
            print(comparison_word)
            list_of_words.append(word)
            list_of_words.append(comparison_word)

def remove_duplicated_letter(list_of_words):
    a=list(list_of_words[0])
    print("a" , a)
    b=list(list_of_words[1])
    print("b" , b)
    return "".join([i for i, j in zip(a, b) if i == j])


if __name__== "__main__":
  main()
