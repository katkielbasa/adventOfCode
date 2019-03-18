def main():
    f=open("input.txt", "r")
    fl =f.readlines()
    listOfMaps=[]
    for x in fl:
        listOfMaps.append(getMapsOfLetterCounts(x))
    #     listOfCharac={}
    #     for s in x:
    #         if s in listOfCharac.keys():
    #             listOfCharac[s]+=1
    #         else:
    #             listOfCharac[s]=1
    #     print (listOfCharac)
    sum2=0
    sum3=0
    for elem in listOfMaps:
        counter2, counter3 = find2and3letters(elem)
        sum2 +=counter2
        sum3 +=counter3
    print(sum2*sum3)   


def getMapsOfLetterCounts(label):
    listOfCharac={}
    for s in label:
        if s in listOfCharac.keys():
            listOfCharac[s]+=1
        else:
            listOfCharac[s]=1
    return listOfCharac

def find2and3letters(map):
    counter2=0
    counter3=0
    for _, value in map.items():
        if value==3:
            counter3 = 1
        if value==2:
            counter2 =1
    return counter2, counter3   

if __name__== "__main__":
  main()


