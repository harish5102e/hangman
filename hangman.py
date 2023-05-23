# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:44:04 2023

@author: haris
"""
import string
#hangman game
import random
from words import words
#select any random word such that the selected word shouldn't have any other characters such as - or " "
def selectword(words):
    inp=random.choice(words)
    while('-'in inp or " "in inp):
        inp=random.choice(wor)
   # print(inp)
    return inp
#selected an input so that it doesn't contain any " " or "-"
#now the user need to guess the letters so that he can able to find the word
al=selectword(words) #makes occurances of multiple letters as one
def hangman():
    word=selectword(words).upper()
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase) #gives set ABCDEFGHIJKLMNOPQRSTUVWXYZ
    used_letters=set() #the letters that are guessed by the user
    
    while(len(word_letters)>0):
        #letters used
        print("YOU have used these letters   ","".join(used_letters))
        word_list=[letter if letter in used_letters else'__' for letter in word]
        print("current word is",''.join(word_list))
        user_letter=input("enter the letter                                ").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif(user_letter in used_letters):
            print("You have already used this letter")
        else:
            print("Exact values from A To Z")
    print("Yay u guessed the word",word)
hangman()
