# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:06:45 2024

@author: asrajend

Letter Ref : https://ilearntamil.com/tamil-alphabets-chart/

"""


from pyuegc import EGC  # pip install pyuegc


index = "ஃஅக்ககாகிகீகுகூகெகேகைகொகோகௌ"
uyir = "அஆஇஈஉஊஎஏஐஒஓஔ"
mei = "க்ங்ச்ஞ்ட்ண்த்ந்ப்ம்ய்ர்ல்வ்ழ்ள்ற்ன்"
a = "கஙசஞடணதநபமயரலவழளறன"
aa = "காஙாசாஞாடாணாதாநாபாமாயாராலாவாழாளாறானா"
e = "கிஙிசிஞிடிணிதிநிபிமியி	ரிலிவிழிளிறினி"
ee = "கீஙீசீஞீடீணீதீநீபீமீயீரீலீவீழீளீறீனீ"
u = "குஙுசுஞுடுணுதுநுபுமுயுருலுவுழுளுறுனு"
uu ="கூஙூசூஞூடூணூதூநூபூமூயூரூலூவூழூளூறூனூ"
ya = "கெஙெசெஞெடெணெதெநெபெமெயெரெலெவெழெளெறெனெ"
yaa = "கேஙேசேஞேடேணேதேநேபேமேயேரேலேவேழேளேறேனே"
i = "கைஙைசைஞைடைணைதைநைபைமையைரைலைவைழைளைறைனை"
o ="கொஙொசொஞொடொணொதொநொபொமொயொரொலொவொழொளொறொனொ"
oo ="கோஙோசோஞோடோணோதோநோபோமோயோரோலோவோழோளோறோனோ"
au = "கௌஙௌசௌஞௌடௌணௌதௌநௌபௌமௌயௌரௌலௌவௌழௌளௌறௌனௌ"
#This needs fixing 
#sp = "ஶஜஷஸஹக்ஷஶாஜாஷாஸாஹாக்ஷாஶிஜிஷிஸிஹிக்ஷிஶீஜீஷீஸீஹீக்ஷீஶுஜுஷுஸுஹுக்ஷுஶூஜூஷூஸூஹூக்ஷூஶெஜெஷெஸெஹெக்ஷெஶேஜேஷேஸேஹேக்ஷேஶைஜைஷைஸைஹைக்ஷைஶொஜொஷொஸொஹொக்ஷொஶோஜோஷோஸோஹோக்ஷோஶௌஜௌஷௌஸௌஹௌக்ஷௌ"
sp = "ஜஷஸஹக்ஷஜாஷாஸாஹாக்ஷாஜிஷிஸிஹிக்ஷிஜீஷீஸீஹீக்ஷீஜுஷுஸுஹுக்ஷுஜூஷூஸூஹூக்ஷூஜெஷெஸெஹெக்ஷெஜேஷேஸேஹேக்ஷேஜைஷைஸைஹைக்ஷைஜொஷொஸொஹொக்ஷொஜோஷோஸோஹோக்ஷோஜௌஷௌஸௌஹௌக்ஷௌ"
sp = "ஜ"

egc_index = EGC(index)
egc_uyir = EGC(uyir)
egc_mei = EGC(mei)
egc_a = EGC(a)
egc_aa = EGC(aa)
egc_e = EGC(e)
egc_ee = EGC(ee)
egc_u = EGC(u)
egc_uu = EGC(uu)
egc_ya = EGC(ya)
egc_yaa = EGC(yaa)
egc_i = EGC(i)
egc_o = EGC(o)
egc_oo = EGC(oo)
egc_au = EGC(au) 
egc_sp = EGC(sp)



string = "தமிழுக்கும் அமுதென்றுபேர்! - அந்தத் \
தமிழ் இன்பத்தமிழ் எங்கள் உயிருக்கு நேர் \
தமிழுக்கு நிலவென்று பேர்! - இன்பத் \
தமிழ் எங்கள் சமூகத்தின் விளைவுக்கு நீர்! \
தமிழுக்கு மணமென்று பேர்! - இன்பத் \
தமிழ் எங்கள் வாழ்வுக்கு நிருமித்த ஊர்! \
தமிழுக்கு மதுவென்று பேர்! - இன்பத் \
தமிழ் எங்கள் உரிமைச் செம்பயிருக்கு வேர்! "

my_dict = {}

words = string.split()
#print(words)
for word in words:
    letter_set = 0
    egc_word = EGC(word)
    #print(egc_word)
    for letter in egc_word:

        if letter in egc_sp:
            if letter_set < 15:
                letter_set = 15
        
        if letter in egc_au:
            if letter_set < 14:
                letter_set = 14

        if letter in egc_oo:
            if letter_set < 13:
                letter_set = 13

        if letter in egc_o:
            if letter_set < 12:
                letter_set = 12

        if letter in egc_i:
            if letter_set < 11:
                letter_set = 11

        if letter in egc_yaa:
            if letter_set < 10:
                letter_set = 10

        if letter in egc_ya:
            if letter_set < 9:
                letter_set = 9

        if letter in egc_uu:
            if letter_set < 8:
                letter_set = 8

        if letter in egc_u:
            if letter_set < 7:
                letter_set = 7

        if letter in egc_ee:
            if letter_set < 6:
                letter_set = 6

        if letter in egc_e:
            if letter_set < 5:
                letter_set = 5

        if letter in egc_aa:
            if letter_set < 4:
                letter_set = 4

        if letter in egc_a:
            if letter_set < 3:
                letter_set = 3

        if letter in egc_mei:
            if letter_set < 2:
                letter_set = 2

        if letter in egc_uyir:
            if letter_set < 1:
                letter_set = 1

    #print(word, end=" ")
    #my_dict[letter_set].append(word)
    #my_dict[letter_set] = word
    if word not in my_dict.get(letter_set, []):
        my_dict.setdefault(letter_set, []).append(word)
    #print("belongs to letter_set "+str(letter_set)) 

for n in range(1,16):
    if n in my_dict:
        print("[",egc_index[n],"]  ", end="")
        word_list =my_dict.get(n)
        print(word_list)
    
