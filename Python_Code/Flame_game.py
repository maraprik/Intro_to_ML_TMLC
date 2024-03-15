# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:22:01 2024

@author: Sarthak
"""





def flame_funtion(name1 , name2):
    
    flames="flames"
    
    for letter in name1:
        if letter in name2:
            name2=name2.replace(letter,"",1)
            name1=name1.replace(letter,"",1)
    
    flamed_name = name1 + name2
    letter_count=len(flamed_name)


    while len(flames) > 1:
        if len(flames) >= letter_count:
            target_letter = flames[letter_count - 1]
            flames = flames.replace(target_letter, "", 1)
        else:
            target_letter = flames[(letter_count % len(flames)) - 1]
            flames = flames.replace(target_letter, "", 1)
            
            
        print("Now in " + flames + ' target letter '+ target_letter )     
            

     
    return flames         

def relation_interpretation(result):

    out = {
        'f': 'Friendship',
        'l': 'Love',
        'a': 'Affection',
        'm': 'Marriage',
        'e': 'Enemy',
        's': 'Siblings'
    }
    return out[result]
    
def main():
    
    print("FLAME Game")
    print ("● Friends")
    print ("● Lovers")
    print ("● Affectionate")
    print ("● Marriage")
    print ("● Enemies")
    print ("● Siblings")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    name1 = name1.replace(" ","").lower()
    name2 = name2.replace(" ","").lower()
    

    
    print( name1 +" "+ name2)
    res = flame_funtion(name1,name2)
    relation = relation_interpretation(res)
    
    print( "Relationship between " +name1 +" & "+name2 +" "+ relation )
    
if __name__ == "__main__":
   main()     