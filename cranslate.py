#Have you ever wanted to speak in Croc code? 
#The advent of the 21st century has now made this possible. 
#Use ~cranslation~ to crocify your text.

import re
#Define a function cranslate which will take standard English text and return Croc text.
def cranslate(string):
    if(" " in string):
        string = string.split(" ")
    consonants = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','v','c','b','n','m']
    numbers = ['1','2','3','4','5','6','7','8','9','0','11','12','13','14','15','16','17','18','19','20']
    length = len(string)
    cranslation = ""
    for item in range(length):
        for i in range(21):
            if(string[item][0].isupper()):
                testCapitalization = True
            else:
                testCapitalization = False
            testconsonant = re.search("^"+consonants[i],string[item].lower())
            for n in range(10):
                testnumber = re.search(numbers[n],string[item].lower())
            #Address the case where a word starts with a consonant which is not part of a 
            #"th" digraph and which is not followed by the letter "r":
            if(testconsonant) and not testnumber and not re.search("^"+'th',string[item].lower())and not string[item][1]=="r":
                string[item] = string[item].replace(string[item][0],"cr",1)
                if(testCapitalization):
                    string[item] = string[item].replace(string[item][0],string[item][0].upper())
                break
            i=i+1
            #Address the case where a word starts with a consonant which is not part of a "th" digraph and which is followed by the letter "r": 
            if(testconsonant) and not testnumber and not re.search("^"+'th',string[item].lower()) and string[item][1]=="r":
                string[item] = string[item].replace(string[item][0],"c",1)
                if(testCapitalization):
                    string[item] = string[item].replace(string[item][0],string[item][0].upper())
                break
            else:
                #Address the case where a word starts with a "th" digraph:
                if(testconsonant) and not testnumber and re.search("^"+'th',string[item].lower()):
                    string[item] = string[item]
                    break
            i=i+1
            #Address the case where a word starts with a vowel:
        if(not testconsonant) and not testnumber: 
            string[item] = "cr"+string[item].lower()
            if(testCapitalization):
                    string[item] = string[item].replace(string[item][0],string[item][0].upper())
        i=i+1
        #Address the case of numbers in the text:
        if(testnumber):
            string[item] = string[item]
        cranslation+=string[item] + " "
    print(cranslation)
#Input the text you would like to cranslate (you need the quotation marks for the code to run):
cranslate("Hello world")