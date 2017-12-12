import json

def main() :

    print("Mau cari HP yang seperti apa?\n")
    query = str(input("=> "))
    print(query)

    data_query = query.split(" ")
    
    list_stopword = []
    stopword = open("stopword.txt","r") #open stopword file
    for word in stopword :
        list_stopword.append((word.split("\n")[0]))
    
    fixed_query = []

    for word in data_query :
        if(not word.lower() in list_stopword) :
            fixed_query.append(word)
    
    print(fixed_query)

if __name__ == "__main__" : 
    main()

