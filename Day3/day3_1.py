#task1
# def main():
#     f=open("input.txt", "r")
#     fl =f.readlines()
#     y = 0
#     for x in fl:
#         y = y + int(x)
#     print(y)

# if __name__== "__main__":
#   main()
#task2 
def main():
    f=open("input.txt", "r")
    fl =f.readlines()
    y = 0
    secik = set({})
    while True:
        for x in fl:
            y = y + int(x)
            if y in secik:
                print(y)
                return
            secik.add(y)

def calcMatriceSize():
                

if __name__== "__main__":
  main()
