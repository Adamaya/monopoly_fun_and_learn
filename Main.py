'''
Project Name:Fun Monopoly
Author: Adamaya Sharma
last Modified: 10/12/2019
Version: 1.4.0

Description; fun monopoly is a monopoly based game stimulation. there are total 27 blocks in this game 2 lottery,
2 penalty,1 payday,1 bonus and rest are sub games.

Game Sequence:

21 20 19 18 17 16 15 14
22                   13
23                   12
24                   11
25                   10
26                   9
27                   8
0  1  2  3  4  5  6  7

1=> "identify_the_artist"                               2=>  "guess_the_song"
3=> "duet"                                              4=>  "penalty"
5=> "music_quiz"                                        6=>  "golden_era"
7=> "lottery"                                           8=>  "guess_the_movie_with_the_help_of_dialogue"
9=> "theme_based_movies"                                10=> "bollywood_quiz"
11=> "bonus"                                            12=> "marvel_quiz""basic_gk"
13=> "guess_the_movie_with_the_help_of_music"           14=> "jail",
15=> "the_logo_quiz"                                    16=> "the_famous_personality"
17=> "logical_puzzle"                                   18=> "penalty"
19=> "basic gk"                                         20=> "slogans"
21=> "payday"                                           22=> "riddles_level_1"
23=> "read_out_the_color"                               24=> "riddles_level_2"
25=> "bonus"                                            26=> "riddles_level_3"
27=> "reverse"
'''
# TODO check the file names in the_logo_quiz
# TODO ADD DISCRIPTION OF GAMES
import random
import PIL.Image
from win32com.client import Dispatch
import time
from pygame import mixer  # Load the popular external library


# checking that answer is correct or wrong
def response_return(request):
    if request.lower() == 'y':
        return True
    elif request.lower() == 'n':
        return False
    else:
        print("\nWrong Input\n")
        return response_return(input('Y\t\tN\n'))


# game chooser function created


def game_chooser(game_number):
    # Music : Identify the Artist
    if game_number == 1:
        print("\nGame " + str(game_number) + ": Identify the Artist")
        speak.Speak("\nGame " + str(game_number) + ": Identify the Artist")
        questions = ['1.Baby Doll-(Mr-Jatt (mp3cut.net).mp3',
                     '2.Chammak Challo - International Version-(Mr-Jatt (mp3cut.net).mp3',
                     '3.Dheeme Dheeme-(Mr-Jatt (mp3cut.net).mp3', '4.Do Peg Maar-(Mr-Jatt (mp3cut.net).mp3',
                     '5.Get Up Jawani - Honey Singh (MzcPunjab (mp3cut.net).mp3',
                     '6.Hud Hud Dabangg-(Mr-Jatt (mp3cut.net).mp3',
                     '7.Humnava Mere-(Mr-Jatt (mp3cut.net).mp3', '8.Jai Jai Shivshankar Song (War) (mp3cut.net).mp3',
                     '9.Lake Peg 4 by Parmish Verma- (mixtau (mp3cut.net).mp3', '10.Lamberghini (mp3cut.net).mp3',
                     '11.Leja Re-(Mr-Jatt (mp3cut.net).mp3', '12.Luv Letter-(Mr-Jatt (mp3cut.net).mp3',
                     '13.Machayenge(MP3Tau (mp3cut.net).mp3', '14.Makhna (Drive) (mp3cut.net).mp3',
                     '15.Mann Bharrya-(Mr-Jatt (mp3cut.net).mp3', '16.Milegi Milegi-(Mr-Jatt (mp3cut.net).mp3',
                     '17.Morni Banke (Badhaai Ho)(Mr-Jattt (mp3cut.net).mp3',
                     '18.Naagin (Vayu Aastha Gill Akasa) (mp3cut.net).mp3',
                     '19.Naino Mein Sapna-(Mr-Jatt (mp3cut.net).mp3', '20.Nazar Lag Jayegi-(Mr-Jatt (mp3cut.net).mp3',
                     '21.Oh Ho Ho Ho  Remix -(Mr-Jatt (mp3cut.net).mp3', '22.Parda-(Mr-Jatt (mp3cut.net).mp3',
                     '23.Prem Ratan Dhan Payo-(Mr-Jatt (mp3cut.net).mp3', '24.Putt_Jatt_Da_1 (mp3cut.net).mp3',
                     '25.Radha-(Mr-Jatt (mp3cut.net).mp3', '26.Rukh-(Mr-Jatt (mp3cut.net).mp3',
                     '27.Socha Hai-(Mr-Jatt (mp3cut.net).mp3', '28.Subhanallah -(Mr-Jatt (mp3cut.net).mp3',
                     '29.Tum Se Hi-(Mr-Jatt (mp3cut.net).mp3', '30.Yaarr Ni Milyaa-(Mr-Jatt (mp3cut.net).mp3']
        random_number = random.randint(0, 29)
        mixer.init()
        mixer.music.load(
            "C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Monopoly Identify The Artist/" + questions[
                random_number])
        print("\nplaying song " + str(random_number + 1)+'\n')
        mixer.music.play()

        response = input("Answer is Correct or Wrong: \nY\t\tN")
        mixer.music.stop()
        return response_return(response)


    # Music : Guess the Song
    elif game_number == 2:
        print("\nGame " + str(game_number) + ": Guess the song")
        speak.Speak("\nGame " + str(game_number) + ": Guess the song")
        questions = ['1.Aakhn maare.mp3','2.Bekhayali.mp3','3.Channa mereya.mp3','4.Chogada.mp3','5.Coka coka.mp3',
                     '6.Dekhte dekhte.mp3','7.Dil mein ho tm.mp3','8.duniya.mp3','9.Ek hazaron mein.mp3',
                     '10.Gali gali.mp3','11.Galiyaan.mp3','12.Gerua.mp3','13.Hawayein.mp3','14.Humko hami se chura lo.mp3',
                     '15.Jitni dafa.mp3','16.kal ho na ho.mp3','17.Kya baat hein.mp3','18.Leja re.mp3','19.Mahi ve.mp3',
                     '20.Mein agr kahoon.mp3','21.Mile ho tm hmko.mp3','22.Naino ki to baat.mp3','23.Nazar na lg jaye.mp3',
                     '24.Parada.mp3','25.Photo.mp3','26.Slowly slowly.mp3','27.Tera hua.mp3','28.Teri meri.mp3',
                     '29.Tujhe kitna chahne lage hm.mp3','30.Tujme rab dikhta h.mp3','30.Tujme rab dikhta h.mp3',
                     '31.Waada.mp3','32.Zaruri tha.mp3']
        random_number = random.randint(0, 31)
        mixer.init()
        mixer.music.load('C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Guess the Music/'+questions[random_number])
        print("\nplaying song " + str(random_number + 1)+'\n')
        mixer.music.play()

        response = input("Answer is Correct or Wrong: \nY\t\tN")
        mixer.music.stop()
        return response_return(response)

    # Music : Duet
    elif game_number == 3:
        print("\nGame " + str(game_number) + ": Duet")
        speak.Speak("\nGame " + str(game_number) + ": Duet")
        questions = ['Sharukh khan and Anushka sharma', 'Siddharth Malhotra and tara Sutaria',
                     'Arjun Kapoor and shraddha Kapoor', 'Ranbir Kapoor and Anushka sharma',
                     'Siddharth Malhotra and katrina kaif', 'Kartik aryan and Nusrat barucha',
                     'Kriti sanon and Sushant singh Rajput', 'Irfan khan, hritik roshan and Abhay deol',
                     'Ayushmaan Khurana and kriti sanon', 'Sushant singh Rajput and disha patani',
                     'Disha patani and tiger shroff', 'Rajkumar rao and shruti hasan',
                     'Akshay kumar and raveena tandon',
                     'Kartik aryan and kriti sanon', 'Aamir khan and kajol',
                     'Kartik aryan ,Ananya pandey and bhoomi padnekar', 'Salman khan and katrina kaif',
                     'Varun Dhawan and alia bhatt', 'Tiger shroff and Jacqueline Fernandez',
                     'Kareena Kapoor ,akshay kumar', 'Akshay kumar and john abrahm', 'Nora fatehi',
                     'Kareena Kapoor and shahrukh khan', 'Sharukh khan and Deepika Padukone',
                     'Hritik roshan and tiger shroff', 'Hritik roshan and vaani Kapoor',
                     'Varun Dhawan and kiara Advani', 'Shahid Kapoor ands kiara Advani',
                     'Akshay kumar and Iliana d’cruez', 'Shraddha Kapoor and Aditya roy kapoor'
                     ]
        random_number = random.randint(0, 29)
        print("\nQuestion Number :" + str(random_number + 1))
        print('\n'+questions[random_number])
        speak.Speak('\n' + questions[random_number])

        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Music : Music Quiz
    elif game_number == 5:
        print("\nGame " + str(game_number) + ": Music Quiz")

        speak.Speak("\nGame " + str(game_number) + ": Music Quiz")
        questions = ['Lead roles in the song ‘Mast Magan’', 'Lead roles in the song ‘ Raat Bhar’',
                     'Lead roles in the song ‘Ik Vaari aa’', 'Lead roles in the song ‘ Aaj  se teri’',
                     'Lead roles in the song ‘ Teri Ore’', 'Lead roles in the song ‘ Saans’',
                     'Lead roles in the song ‘Drama Queen’', 'Lead roles in the song ‘ Mujhe haq hein’',
                     'Lead roles in the song ‘ Dagabaaz Re’', 'Lead roles in the song ‘Shukran allah’',
                     'Lead roles in the song ‘Bol do na zara’',
                     'Lead roles in the song ‘ Sooraj dooba hai’', 'Lead roles in the song ‘Sau Asmaan’',
                     'Lead roles in the song ‘Mene tujko dekha’', 'Lead roles in the song ‘Dance k Legend’',
                     'Lead roles in the song ‘Saiyaan superstar’', 'Lead roles in the song ‘ Mein agar kahoon’',
                     'Lead roles in the song ‘Tareefan’', 'Lead roles in the song ‘ Ik Mulaqaat’',
                     'Lead roles in the song ‘ Saanu Ek pal chain’', 'Lead roles in the song ‘Aashiq Banaya aapne’',
                     'Lead roles in the song ‘Tera Yaar hoon mein’', 'Lead roles in the song ‘Tukur Tukur’',
                     'Lead roles in the song ‘ Enna Sona’', 'Lead roles in the song ‘ Beech Beech Mein’',
                     'Lead roles in the song ‘ Second Hand jawani’', 'Lead roles in the song ‘ Morni Banke’',
                     'GUESS THE SONG “SOMETIMES IN MY HEART, THERE COMES A THOUGHT , AS YOU WERE MADE ONLY FOR ME…”',
                     'GUESS THE SONG “ONE HOT TEACUP AND SOMEBODY TO SERVE IT..”',
                     'GUESS THE SONG “THIS FRIENDSHIP, WE SHALL NEVER BREAK, WE COULD GIVE UP OUR LIVES FOR THE COMPANIONSHIP’S SAKE..”'
                     ]
        random_number = random.randint(0, 29)
        print("\nQuestion Number :" + str(random_number + 1))
        print('\n'+questions[random_number])
        speak.Speak('\nYOUR QUESTION IS. '+questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Music : Golden Era
    elif game_number == 6:
        print("\nGame " + str(game_number) + ": Golden Era")
        speak.Speak("\nGame " + str(game_number) + ": Golden Era")
        questions = ['1.Aanewala Pal-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '2.Aaye Ho Meri-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '3.Ajeeb Dastan Hai Ye-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '4.Babuji Dheere Chalna - Geeta Dutt (MzcPunjab.Com)-[AudioTrimmer.com].mp3',
                     '5.Chabi Kho Jaye-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '6.Chura Liya Hai Tumne Jo Dil Ko-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '7.Do Lafzon Ki Hai Dil Ki Kahani-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '8.Ek Ladki Bheegi Bhagi Si-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '9.Gulabi Aankhen Jo-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '10.Honthon Mein Aisi Baat-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '11.Hothon Se Choo Lo Tum-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '12.In Aankhon Ki Masti Mein  Umrao Jaan -(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '13.Mehbooba Mehbooba Sholay2-[AudioTrimmer.com].mp3',
                     '14.Mere Mehboob Qayamat Hogi-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '15.Mere Sapno Ki Rani Kab Aayegi Tu-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '16.Na Bole Tum-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '17.Neele Neele Ambar-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '18.O Mere Dil Ke Chain-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '19.Pal Pal Dil Ke Paas  Blackmail -(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '20.Pyar Kiya To Darna Kya-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '21.Tere Bina Zindagi Mein Aandhi-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '22.Uden Jab Jab Zulfen Teri (Naya Daur 1957) - Various (MzcPunjab.Com)-[AudioTrimmer.com].mp3',
                     '23.Yashomati Maiya Se Bole Nandlala-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '24.Yeh Chand Sa Roshan Chehra (Kashmir Ki Kali) - Akbar Sami (MzcPunjab.Com)-[AudioTrimmer.com].mp3',
                     '25.Yeh Kahan Aa Gaye Hum-(Mr-Jatt.com)-[AudioTrimmer.com].mp3',
                     '26.Yeh Sama Sama Hai Yeh Pyar Ka-(Mr-Jatt.com)-[AudioTrimmer.com].mp3']
        random_number = random.randint(0, 25)
        mixer.init()
        mixer.music.load(
            "C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Golden Era/" + questions[random_number])
        print("\nplaying song " + str(random_number + 1))
        mixer.music.play()

        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        mixer.music.stop()
        return response_return(response)

    # Entertainment: Guess the movie (with the help of dialogue)
    elif game_number == 8:
        print("\nGame " + str(game_number) + ": GUESS THE MOVIE (with the help of dialogue)")
        speak.Speak("\nGame " + str(game_number) + ": GUESS THE MOVIE (with the help of dialogue)")
        questions = ["TENSION LENE KA NHI SIRF DENE KA", "LIFE MAI SBSE BADA RISK HOTA H KBHI KOI RISK NHI LENA",
                     "MAI APNI FAVOUITE HOON", "TUMSE NA HO PAYEGA", "PALAT, PALAT, PALAT!!!",
                     "AAP CONVINCE HOGYE KI MAI AUR BOLU",
                     "USKA TO NA BAD LUCK HI KHRAAB HAI",
                     "AADMI TBHI BADA BNTA HAI JB BADE LOG USSE MILNE LA ITNEZAAR KARE",
                     "KAHI PR PAHUCHNE K LIYE KAHI SE NIKLNA ZARURI H", "INSAAN NAAM MAI MAZHAB DHUND LETA HAI",
                     "KHAAMOSH!!!!", "PREM NAAM HAI MERA , PREM CHOPRA", "PICTURE ABHI BAAKI HAI MERE DOST",
                     "PUSHPA I  HATE TEARS!!!", "BABUMUSHAI ZINDAGI BADI HONI CHAHIYE , LAMBI NHI..",
                     "AAJ MERE PASS GADI HAI, BAGLA HAI, PAISA HAI, TMAHRE PASS KYA HAI??", "MERE KARAN ARJUN AYENGE!!",
                     "RISHTE MEIN TO HUM TMHARE BAAP LAGTE HAI",
                     "I’M JUST A STUPID COMMON MAN WAITING TO CLEAN HIS HOUSE",
                     "MOGAMBO KHUSH HUA", "JO YE TERA TORTURE HAI WO MERA WARMUP HAI",
                     "WATAN K AAGE KUCH NHI, KHUD BHI NHI",
                     "APNA LIFE FULL SAAP SEEDI KA BOARD H, KBHI UP TO DOWN",
                     "DOSTI AUR LADKI MAI HAMESHA LADKI JEETTI HAI",
                     "DOSTI KA USUL HAI, MADAM – NO SORRY , NO THANK U",
                     "KABHI KABHI KUCH JEETNE K LIYE KUCH HARNA PADTA H",
                     "JA SIMARAN JA", "KOI DHANDA CHOTA NHI HOTA AUR DHNDE SE BADA KOI DHARM NHI HOTA",
                     "TUMHARA RESULT DECIDE NHI KRTA HAI KI TUM LOSER HO KI NHI, TMHARI KOSHISH KRTI H..",
                     "YE BABURAO KA STYLE HAI"
                     ]
        random_number = random.randint(0, 29)
        print("\nDialogue Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak('\nYOUR QUESTION IS. ' + questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Entertainment: THEME BASED MOVIES
    elif game_number == 9:
        print("\nGame " + str(game_number) + ": THEME BASED MOVIES")
        speak.Speak("\nGame " + str(game_number) + ": THEME BASED MOVIES")
        questions = ["5 MOVIES RELATED TO – SPORTS", "5 PATRIOTIC MOVIES", "5 WOMEN EMPOWERMENT MOVIES",
                     "5 HORROR MOVIES", "5 ROMANTIC MOVIES", "5 COMEDY MOVIES", "5 THRILLER MOVIES"]
        random_number = random.randint(0, 6)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak('\nYOUR QUESTION IS. ' + questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN\n")
        return response_return(response)

    # Entertainment: BOLLYWOOD QUIZ
    elif game_number == 10:
        print("\nGame " + str(game_number) + ": BOLLYWOOD QUIZ")
        speak.Speak("\nGame " + str(game_number) + ": BOLLYWOOD QUIZ")
        questions = ["FATHER OF SALMAAN KHAN", "HOW MANY BROTHERS DO SALMAAN KHAN HAVE?",
                     "FIRST FILM OF SHAHID KAPOOR",
                     "FIRST FILM OF AMITABH BACHAN", "FIRST FILM OF SALMAAN KHAN", "FIRST FILM OF RANVEER SINGH",
                     "FIRST FILM OF AYUSHMAAN KHURANAA", "FIRST FILM OF SHARUKH KHAN", "FIRST FILM OF AISHWARYA",
                     "FIRST FILM OF KAJOL", "FIRST FILM OF AMIR KHAN", "FIRST FILM OF KATRINA KAIF",
                     "NAME ONE MOVIE OF SAIF ALI KHAN AND RANI MUKHERJI",
                     "NAME ONE MOVIE OF SALMAAN KHAN AND PRIYANKA CHOPRA",
                     "NAME ONE MOVIE OF AKSHAY KUMAR AND KATRINA KAIF", "WHAT WAS THE THEME OF THE MOVIE “SHIVAAY”",
                     "WHAT WAS THE THEME OF THE MOVIE “DEDE PYAAR DE”", "WHICH WAS THE FIRST BOLLYWOOD MOVIE",
                     "MADHURI DIXIT NAME IN MOVIE “ TEZAAB”", "AISHWARYA RAI WAS CROWNED MISS WORLD IN?",
                     "NAME THE DIRECTOR OF FILM “SATYA”", "NAME A  MOVIE OF AMIR KHAN’S HOME PRODUCTION",
                     "NAME OF RITIESH DESHMUKH CHARACTER IN “DHAMAAL”",
                     "NAME  A MOVIE WHERE SHARUKH KHAN WAS A VILLAIN", "NAME OF THE LEAD BAD GUY IN DHOOM",
                     "LEAD MALE ROEL IN-“DELHI 6”",
                     "BOLLYWOOD STAR SELECTED AS JURY MEMBER IN “CANNES FILM FESTIVAL” IN 2003?",
                     "WHO PRODUCED “FIR BHI DIL H HINDUSTANI”", "FEMALE LEAD IN “CHANDNI CHOWK TO CHINA”",
                     "WHO PALYED THE ROLE OF GOD IN “GOD TUSSI GREAT HO”?"]
        random_number = random.randint(0, 29)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak('\nYOUR QUESTION IS. ' + questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Entertainment: QUIZ RELATED TO (DISNEY, MARVEL, CARTOONS)
    elif game_number == 12:
        print("\nGame " + str(game_number) + ": QUIZ RELATED TO (DISNEY, MARVEL, CARTOONS)")
        questions = ["IN WHICH TWO CHANNELS YOU CAN WATCH DORAEMON", "FROM WHICH CENTURY DORARMON CAME FROM?",
                     "NAME OF DOG WHICH TALKS TOO MUCH IN MOVIE NOBITA’S LITTLE SPACE WAR",
                     "WHAT’S HAWKEYE’S REAL NAME IN AVENGERS",
                     "IN “THE CLAWS OF THE CAT” WHO WAS BEHIND THE  MASK OF FELINEORIENTED SUPERHEROINE?",
                     "IN 1939, WHAT PULP MAGAZINE PUBLISHER DECIDED TO GET INTO THE COMIC BUSINESS WITH “MARVEL COMICS”",
                     "WHO IS THE VILLAIN WHO KILLED GWEN STACY, SPIDER-MAN’S FIRST LOVE?",
                     "WHAT IS THE NAME OF SHINCHAN’S DOG?",
                     "WHAT IS THE VEGETABLE WHICH SHINCHAN HATES TO EAT",
                     "WHAT IS THE COLOUR OF DRESS SHINCHAN’S SISTER",
                     "WHAT IS THE NAME OF LOKI’S FATHER", "THOR’S HAMMER NAME",
                     "HOW MANY TIMES DR STRANGE SAW THE FUTURE IN INFINTY WAR",
                     "WHICH STONE DOES DR STRANGE HAD WITH HIM", "WHAT WAS THE NAME OF THANOS DAUGHTERS",
                     "WORD USED TO ACTIVATE IRON MAN’S SPECS(IN SPIDERMAN FAR FROM HOME )",
                     "WHEN DID STANLEE DIED?",
                     "T’CHALLA IS THE BLACK PANTHER SO WHAT IS HIS FATHER’S NAME ?",
                     "REAL VOICE BEHIND DOREAMON", "NAME ANY 5 CHARACTER OF MICKEY MOUSE",
                     "NAME THE THREE POWERPUFF GIRLS",
                     "BROTHER’S NAME OF PRETTI IN HADI MERA BUDDY",
                     "WHAT WAS THE NAME OF DORA’S MONKEY?", "WHO DIES IN GUARDIAN OF GALAXY VOL-1",
                     "IN WHICH KINGDOM CHOTA BHEEM LIVES?", "NAME 5 DISNEY MOVIES"]
        random_number = random.randint(0, 20)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak('\nYOUR QUESTION IS. ' + questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Entertainment: Guess the Movie with the help of Music
    elif game_number == 13:
        print("\nGame " + str(game_number) + ": Guess the Movie with the help of Music\n")
        speak.Speak("\nGame " + str(game_number) + ": Guess the Movie with the help of Music\n")
        print("Description: Identify the movie with the help of music\nNote: - Music will be played once")
        speak.Speak("Description: Identify the movie with the help of music\nNote: - Music will be played once")
        questions = ['1._Hawa Hawa_ (Full Video Song) _ Mubarakan _ Anil K(MP3_160K)-[AudioTrimmer.com].mp3',
                     '2._Main Aai Hoon U.P. Bihar Lootne_ Lyrical Video __(MP3_160K)-[AudioTrimmer.com].mp3',
                     '3.A.R. Rahman - Tere Bina Best Video_ Guru_Aishwarya(MP3_160K)-[AudioTrimmer.com].mp3',
                     '4.Aaj dil Shaayraana - Arijit Singh _ Holiday _ Aksh(MP3_160K)-[AudioTrimmer.com].mp3',
                     '5.Abhi Abhi Toh Mile Ho Full Video Song Jism 2 _ Sun(MP3_160K)-[AudioTrimmer.com].mp3',
                     '6.Afghan Jalebi (Ya Baba) FULL VIDEO Song _ Phantom(MP3_160K)-[AudioTrimmer.com].mp3',
                     '7.Agent Vinod _Dil Mera Muft Ka_ Video Song Feat. Ka(MP3_160K)-[AudioTrimmer.com].mp3',
                     '8.ALCOHOLIC - LYRICAL VIDEO _ The Shaukeens _ Yo Yo(MP3_160K)-[AudioTrimmer.com].mp3',
                     '9.Baby besharam Lyrics video _ full video _ Naam Sha(MP3_160K)-[AudioTrimmer.com].mp3',
                     '10.Fugly_ Dhup Chik Video Song _ Raftaar(MP3_160K)-[AudioTrimmer.com].mp3',
                     '11.Gazab Ka Hai Din With Lyrics _ DIL JUUNGLEE _ Tani(MP3_160K)-[AudioTrimmer.com].mp3',
                     '12.Hip hop pammy(MP3_160K)-[AudioTrimmer.com].mp3',
                     '13.Iss Qadar Pyar Hai VIDEO Song - Ankit Tiwari _ Bha(MP3_160K)-[AudioTrimmer.com].mp3',
                     '14.Jaanu _ Behen Hogi Teri _ Rajkummar Rao _ Shruti H(MP3_160K)-[AudioTrimmer.com].mp3',
                     '15.Jazba - Full Song _ Ladies vs Ricky Bahl _ Anushka(MP3_160K)-[AudioTrimmer.com].mp3',
                     '16.Kuch is tarah _ atif aslam_s kuch is tarah _ kuch(MP3_160K)-[AudioTrimmer.com].mp3',
                     '17.Kuch Iss Tarah _ 1921 _ Zareen Khan _ Karan Kundrr(MP3_160K)-[AudioTrimmer.com].mp3',
                     '18.Ladki Kyon - Full Song _ Hum Tum _ Saif Ali Khan _(MP3_160K)-[AudioTrimmer.com].mp3',
                     '19.Lae Dooba - Full Video _ Aiyaary _ Sidharth Malhot(MP3_160K)-[AudioTrimmer.com].mp3',
                     '20.Laung Da Lashkara (Patiala House) Full Song _ Feat(MP3_160K)-[AudioTrimmer.com].mp3',
                     '21.Lut Gaye Besharam Full HD Video Song _ Ranbir Kapo(MP3_160K)-[AudioTrimmer.com].mp3',
                     '22.Lyrical_ Apna Har Din Aise Jiyo _  Golmaal 3 _ Aja(MP3_160K)-[AudioTrimmer.com].mp3',
                     '23.Muskaanein Jhooti Hai (Lyrics HD) - Talaash ft. Su(MP3_160K)-[AudioTrimmer.com].mp3',
                     '24.Namak Halaal - Jawani Janeman Haseen Dilruba - Ash(MP3_160K)-[AudioTrimmer.com].mp3',
                     '25.Piya Ke Bazaar Mein _ Humshakals HD Video Song _ S(MP3_160K) (mp3cut.net).mp3',
                     '26.Sharara - Full Song _ Mere Yaar Ki Shaadi Hai _ Sh(MP3_160K) (mp3cut.net).mp3',
                     '27.Shootout At Wadala - Laila Uncensored HD Full Vide(MP3_160K) (mp3cut.net).mp3',
                     '28.Tera Fitoor Full Video - Genius _ Utkarsh Sharma_(MP3_160K) (mp3cut.net).mp3',
                     '29.Tere Naina Jai Ho Full Video Song _ Salman Khan_ D(MP3_160K) (mp3cut.net).mp3',
                     '30.Tose Naina- Mickey Virus _ HD _ Feat Elli Avram an(MP3_160K) (mp3cut.net).mp3',
                     '31.Tu Hi Hai Aashiqui (DISHKIYAOON) Arijit Singh(MP3_160K) (mp3cut.net).mp3',
                     '32.You are My Love Full Video Song _ Partner _ Salman(MP3_160K) (mp3cut.net).mp3']
        random_number = random.randint(0, 31)
        mixer.init()
        mixer.music.load(
            "C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Guess the Movie/" + questions[random_number])
        print("\nplaying song " + str(random_number + 1))
        mixer.music.play()
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        mixer.music.stop()
        return response_return(response)

    # Technology and Famous Personality: The LOGO Quiz
    elif game_number == 15:
        print("\nGame " + str(game_number) + ": The LOGO Quiz")
        speak.Speak("\nGame " + str(game_number) + ": The LOGO Quiz")
        questions = ['adobe.png', 'Airtel.jpg', 'alienware.jpg', 'apple.jpg', 'bentley.jpg', 'blackberry.png',
                     'Boeing.png',
                     'Cisco.png', 'cn_logo.jpg', 'DHL.png', 'dodge.png', 'dove.png', 'dreamworks.jpg', 'EA Sports.png',
                     'Github.png', 'gulf.jpg', 'intelliJ.png', 'jetix.jpg', 'johney walker.jpg', 'Kwality walls.png',
                     'mcdonald.png', 'microsoft.png', 'mini.jpg', 'NBC.jpg', 'nvidia.png', 'pringles.jpg', 'rolex.jpg',
                     'Rolls_royce.png', 'shell.png', 'tesla.jpg', 'unity.png', 'Visual Studio.png', 'wolks_wagan.jpg']
        random_number = random.randint(0, 32)
        image = PIL.Image.open(
            "C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Logo/" + questions[random_number])
        image.show()
        print("\nAnswer: Image number " + str(random_number + 1))
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Technology and Famous Personality: THE FAMOUS PERSONALITY
    elif game_number == 16:
        print("\nGame " + str(game_number) + ": THE FAMOUS PERSONALITY")
        speak.Speak("\nGame " + str(game_number) + ": THE FAMOUS PERSONALITY")
        questions = ['Albert Einstein.jpg', 'denial redcliff.jpg', 'dr APJ Abdul Kalam.jpg', 'Elon Musk.jpg',
                     'Jack ma.jpg','jenifer lawrence.jpg', 'jk rowling.jpg', 'leonardo dicaprio.jpg',
                     'martin luthor king junior.jpg','messi.jpg','muhammad ali.jpg','Nicola Tesla.png','pele.png',
                     'robert downy jr.png']
        random_number = random.randint(0, 13)
        image = PIL.Image.open(
            "C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Famous Personality/" + questions[
                random_number])
        image.show()
        print("\nAnswer: Image number " + str(random_number + 1))
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Technology and Famous Personality: Logical puzzle
    elif game_number == 17:
        print("\nGame " + str(game_number) + ": Logical Puzzle")
        speak.Speak("\nGame " + str(game_number) + ": Logical Puzzle")
        questions = [
            'THERE ARE TWO GIRLS ONE IS FACING THE SOUTH THE OTHER FACES THE NORTH YET THEY CAN SEE EACH OTHER WITHOUT A MIRROR, HOW CAN IT BE?',
            'WHAT CAN YOU SEE ONCE IN A MIN, TWICE IN A MOMENT, AND NEVER IN A THOUSAND YEAR?',
            'WHAT NO IS MISSING?\n234\n23?\nTIP: IT’S NOT 4',
            'THERE IS A BATH TUB FILLED WITH WATER IN FRONT OF YOU, YOU’VE A SPOON, A CUP AND A BUCKET, WHAT IS THE FASTEST WAY TO EMPTY A TUB?',
            'ADD ONE LINE TO MAKE THE EQUATION TRUE\n5+5+5+5=555\nYOU CANNOT CROSS THE EQUAL SIGN',
            'THERE ARE 3 DOORS, IN FIRST DOOR A FIRE IS RAGGING AND SECOND DOOR THERE A GUN MAN, IN THIRD THERE IS A LION THAT HASN’T EATEN IN THREE YEARS. WHICH DOOR YOU WILL CHOOSE?',
            'PLACE THREE LETTER IN (---) SO THAT YOU CAN COMPLETE THE WORD ON THE LEFT AND BEGIN THE WORD ON RIGHT\nUNF(---)EST',
            'PLACE THREE LETTER IN (---) SO THAT YOU CAN COMPLETE THE WORD ON THE LEFT AND BEGIN THE WORD ON RIGHT\nTO(---)TURES',
            'PLACE THREE LETTER IN (---) SO THAT YOU CAN COMPLETE THE WORD ON THE LEFT AND BEGIN THE WORD ON RIGHT\nHIC(---)FUL',
            'PLACE THREE LETTER IN (---) SO THAT YOU CAN COMPLETE THE WORD ON THE LEFT AND BEGIN THE WORD ON RIGHT\nEIT(---)ETIC',
            'PLACE THREE LETTER IN (---) SO THAT YOU CAN COMPLETE THE WORD ON THE LEFT AND BEGIN THE WORD ON RIGHT\nFEE(---)EDER',
            'PLACE THREE LETTER IN (---) SO THAT YOU CAN COMPLETE THE WORD ON THE LEFT AND BEGIN THE WORD ON RIGHT\nHE(---)FUL',
            'WHAT DOES IT SIGNIFIES?\n1,2,3---------,38,39,40LIFE',
            'WHAT DOES IT SIGNIFIES?\nA,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,V,W,X,Y,Z',
            'WHAT DOES IT SIGNIFIES?\n\tGIVE GET\n\tGIVE GET\n\tGIVE GET\n\tGIVE GET',
            'WHAT DOES IT SIGNIFIES?\n\tLE\n\tVEL',
            'WHAT DOES IT SIGNIFIES?\nL\n O\n  V\n   \nE', 'WHAT DOES IT SIGNIFIES?\n\tTRY STAND\t\t2',
            'WHAT DOES IT SIGNIFIES?\n\tJOBINJOB', 'WHAT DOES IT SIGNIFIES?\n\tNEAFRIENDED',
            'WHAT DOES IT SIGNIFIES?\n\tTRAVEL\n\tCCCCC', 'WHAT DOES IT SIGNIFIES?\n\tMEN\nBOARD',
            'WHAT DOES IT SIGNIFIES?\n\t1.\n\t2.BLAME\n\t3.BLAME', 'HOW MANY MONTHS HAVE 28 DAYS?',
            'A FARMER HEAD 17 GOTS.ALL BUT 6 DIED.HOW MANY SURVIVED?',
            'WHAT OCCURS ONCE IN A YEAR, TWICE IN A WEEK BUT NEVER IN A DAY?',
            'JACK’S MOTHER HAS THREE SONS – SNAP, JOHN, GUESS THE LAST ONE?',
            'BEFORE MT EVEREST WAS DISCOVERED WHAT WAS HIGHEST MT.ON THE EARTH?',
            'NAME ONE MEAL YOU CAN NEVER EAT FOR BREAKFAST?',
            'WHAT WORD BECOMES SHORTER WHEN YOU ADD TWO LETTERS TO IT.'
        ]
        random_number = random.randint(0, 29)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak("your question is. "+questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Technology and Famous Personality: Basic GK
    elif game_number == 19:
        print("\nGame " + str(game_number) + ": Basic GK")
        speak.Speak("\nGame " + str(game_number) + ": Basic GK")
        questions = ['LANGUAGE SPOKEN BY PEOPLE IN PAKISTAN', 'WORLD’S LARGEST DESERT',
                     'METAL WHOSE SALTS ARE SESITIVE TO LIGHT IS', 'MOUNT EVEREST IS LOACTED IN',
                     'DEVICE USED FOR MEASURING ALTITUDE IS', 'WHICH IS CONSIDERED AS BIGGEST PORT IN INDIA',
                     'THE GAS USED FOR MAKING VEGETABLE', 'PINK CITY IN INDIA IS',
                     'HEADQUARTER OF COFFEE BOARD OF INDIA IS', 'LARGEST FRESHWATER LAKE IN INDIA',
                     'NAME THE GOVERNOR GENERAL WHO ABOLISHED SATI SYSTEM IN 1829.',
                     'LARGEST RIVER IN INDIA', 'PUNJAB IS FAMOUS FOR', 'FIRST UNIVERSITY IN INDIA WAS FOUNDED AT ',
                     'THE STATE WHICH HAS LARGEST NO OF SUGAR MILLS', 'MOST POPULAR SPORT THROUGHOUT THE WORLD',
                     'HOTEST CONTINENT ON EARTH', 'WORLD SMALLEST COUNTRY IS', 'SECOND LARGEST COUNTRY IN THE WORLD',
                     'LANGUAGE SPOKEN IN KARNATAKA', 'CURRENCY NOTES ARE PRINTED IN', 'WORLD MOST COMMON RELIGION',
                     'WHICH CITY HOSTED THE FIRST EVER ASAIN GAMES', 'IN WHICH YEAR WAS RASHPATI BHAVAN BUILT',
                     'INDIA’S FIRST FEMALE PLAYBACK SINGER', 'WHICH COUNTRY HAS THE WORLD’S LARGEST RAILWAY NETWORK',
                     'NATIONAL VEGETABLE OF INDIA', 'LARGEST SEA PORT IN INDIA',
                     'IN 2G, 3G AND 4G WHAT DOES G STANDS FOR?',
                     'WHEN IS THE INTERNATIONAL DAY OF YOGA?']
        random_number = random.randint(0, 29)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak("your question is. "+questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # Technology and Famous Personality: Slogans
    elif game_number == 20:
        print("\nGame " + str(game_number) + ": Slogans")
        speak.Speak("\nGame " + str(game_number) + ": Slogans")
        questions = ['TANN KI SHAKTI , MANN KI SHAKTI', 'FRESH AND JUICY', 'TASTE THE THUNDER', 'THE COMPLETE MEN',
                     'TASTE BHI , HEALTH BHI', 'BORN TOUGH', 'BEAUTY BAR OF FILM STARS', 'DESH KA NAMAK',
                     'DIMAG KI BATTI JALA DE', 'BAJATE RAHO', 'ZINDAGI K SATH BHI, ZINDAGI K BAAD BHI',
                     'SWAAD ZINDAGI KA',
                     'HAR GHAR KUCH KEHTE HAI', 'DAAG TO ACHE HAI', 'ISSE SASTA AUR KAHI NHI',
                     'BHUJAYE PYAAS BAAKI ALL BAKWASS!!', 'JII LALCHAYE RAHA NA JAYE', 'NO ONE CAN EAT JUST ONCE',
                     'JIYO SIR UTHA K', 'KAISI JEEP LAPLAPAYI', 'KHAAO AUR KHUD JAAN JAAO', 'DIL KI DEAL',
                     'AB HAR WISH HOGI PURI', 'CHALO NIKLO', 'DIL TO ROAMING HAI',
                     'DISCOVER GREAT PLACES TO EAT AROUND YOU',
                     'GALE KI KHARACH KA FIRST AID', 'THANDA THANDA COOL COOL', 'THE KING OF GOOD TIMES', 'TAKE CARE'
                     ]
        random_number = random.randint(0, 31)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak("your question is. "+questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)


    # IQ: Riddles (Level 1)
    elif game_number == 22:
        print("\nGame " + str(game_number) + ": Riddles (Level 1)")
        speak.Speak("\nGame " + str(game_number) + ": Riddles (Level 1)")
        questions = [
            'You begin reading a book 240 pages long. If you read half of the remaining book each day how long would it take you to finish the book?',
            'Add a single line to the equation in order to make it true.\n105 + 2 + 5 = 350',
            'Find the product of the following series:\n(x-a) (x-b) (x-c) ..... (x-z)',
            'What number when multiplied against itself will result in a number which includes the numbers (1 - 9) in forward order, and then descending in order from the 9? (i.e., to get the number: 12,345,678,987,654,321)',
            'An old man said to a young man, "I have a daughter. She has as many brothers as she has sisters. Each one of her brothers has twice as many sisters as he has brothers. How many sons and daughters do I have?',
            'A kite and surfboard cost $1500 in total. The kite costs $1,000 more than the surfboard. How much does the surfboard cost?',
            'Try to find a common connecting word.\n\tPiano : Lock',
            'Try to find a common connecting word.\n\tTree : Car',
            'Try to find a common connecting word.\n\tTennis : Noise',
            'Try to find a common connecting word.\n\tShip : Cards',
            'Try to find a common connecting word.\n\tBed : Paper',
            'Try to find a common connecting word.\n\tPillow : Court',
            'Try to find a common connecting word.\n\tSilver : Table',
            'Try to find a common connecting word.\n\tType : Lift',
            'Add a single line to the equation in order to make it true.\n\t5+5+5+5=555',
            'I AM A FRUIT . I AM TASTY AND PROVIDE LOTS OF ENERGY . YOU CAN ALSO FIND ME IN A CALENDAR. WHO AM I?',
            'I COME FROM NORTH, EAST,WEST AND SOUTH. I GIVE YOY LOTS OF INFORMATION EITHER VERBALLY OR TEXTUALLY. WHO AM I?',
            'I AM DRINK. I AM ALSO AN ALPHABET. WHO AM I?', 'THE MORE I AM PRESENT , THE LESS YOU CAN SEE . WHO AM I?',
            'I START WITH T AND END WITH T AND HAVE T IN ME . WHO AM I?']
        random_number = random.randint(0, 19)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak("your question is. "+questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # IQ: Read Out The Color
    elif game_number == 23:
        print("\nGame " + str(game_number) + ": Read Out The Color")
        speak.Speak("\nGame " + str(game_number) + ": Read Out The Color")
        questions = [
            '1.png', '2.png', '3.png', '4.png', '5.png'
        ]
        random_number = random.randint(0, 4)
        image = PIL.Image.open(
            "C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Read out the color/" + questions[
                random_number])
        image.show()
        print("\nAnswer: Image number " + str(random_number + 1))
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # IQ: Riddles (Level 2)
    elif game_number == 24:
        print("\nGame " + str(game_number) + ": Riddles (Level 2)")
        speak.Speak("\nGame " + str(game_number) + ": Riddles (Level 2)")
        questions = ['What is full of holes but still holds water?', 'What has no content yet you can see it?',
                     'What falls but never breaks?',
                     'What is it that goes with an automobile and comes with it; is of no use to it, and yet the automobile cannot move without it?',
                     'You are in a race and you overtake the person who is in second place. What is your position now?',
                     'Six drinking glasses stand in a row, with the first three full of juice and the next three empty. By moving only one glass can you arrange them so empty and full glasses alternate?',
                     'A man is asked what his daughters look like. He answers, "They are all blondes, but two, all brunettes, but two, and all redheads, but two." How many daughters did he have?',
                     'Why is it better to have round manhole covers than square ones?',
                     'There is a waterlily in a pond, that doubles in size every day. If it takes the waterlily 180 days to cover the entire pond, how long does it take to cover half the pond?',
                     'Identify the missing words that will make each statement true.\n\t1001 = A. N.',
                     'Identify the missing words that will make each statement true.\n\t24 = H. in a D.',
                     'Identify the missing words that will make each statement true.\n\t90 D. in a R. A.',
                     'Identify the missing words that will make each statement true.\n\t	7 = W. of the A. W.',
                     'Identify the missing words that will make each statement true.\n\t26	 L. of the A.',
                     'Identify the missing words that will make each statement true.\n\t12 = I. in a F',
                     'Identify the missing words that will make each statement true.\n\t 4 = Q. in a G',
                     'WHAT LOOKS LIKE A HALF APPLE?',
                     'I AM A FOUR LETTER WORD. I AM AN ANIMAL. YOU USE ME TO CALL YOUR DEAR ONES. WHO AM I?',
                     'I HAVE ONE LETTER BUT MY NAME IS SPELLED WITH EIGHT. WHAT AM I?',
                     'I CAN FILL UP AN ENTIRE ROOM AND STILL NOT TAKE UP ANY SPACE. WHO AM I?'
                     ]
        random_number = random.randint(0, 18)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak("your question is. "+questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # IQ: Riddles (Level 3)
    elif game_number == 26:
        print("\nGame " + str(game_number) + ": Riddles (Level 3)")
        speak.Speak("\nGame " + str(game_number) + ": Riddles (Level 3)")
        questions = [
            'There are 5 apples in the basket. They need to be divided among 5 people. How can you divide them so that each person has an apple and one apple stays in the basket?',
            'Billie was born on December 26th yet her birthday always falls in the summer. How is this possible?',
            'Which is correct to say,” The yolk of egg is white” , “The yolk of the egg are white”?',
            'Imagine you’re driving a bus, at first stop two passengers step in and 9 passengers step down from the bus. On second stop 12 passengers step in and 1 passenger step down. Guess the colour of the dress of driver?'
        ]
        random_number = random.randint(0, 3)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])
        speak.Speak("your question is "+questions[random_number])
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)

    # IQ: Reverse it out
    elif game_number == 27:
        print("\nGame " + str(game_number) + ": Read it Reverse")
        speak.Speak("\nGame " + str(game_number) + ": Reverse it reverse")
        questions = ['number upto 15 to 47','number 87 to 103','number 77 to 113','number 91 to 127'
                     ]
        random_number = random.randint(0, 3)
        print("\nQuestion Number :" + str(random_number + 1)+'\n')
        print(questions[random_number])

        speak.Speak("your question is speak "+questions[random_number]+" in reverse order")
        response = input("\nAnswer is Correct or Wrong: \nY\t\tN")
        return response_return(response)


# adding game scores
def score_addition(player_number, game_name, game_owner, answer_status, lottery=0, bonus=0, penalty=0):
    games_points = {"guess_the_movie_with_the_help_of_dialogue": 100, "theme_based_movies": 100, "bollywood_quiz": 100,
                    "marvel_quiz": 100, "guess_the_movie_with_the_help_of_music": 100,

                    "the_logo_quiz": 100, "the_famous_personality": 100, "logical_puzzle": 150, "basic_gk": 150,
                    "slogans": 100,

                    "identify_the_artist": 50, "guess_the_song": 50, "duet": 50, "music_quiz": 50,
                    "golden_era": 50,

                    "riddles_level_1": 200, "read_out_the_color": 150, "riddles_level_2": 200, "riddles_level_3": 200,
                    "reverse": 150}

    if answer_status:
        players_scores[player_number] = players_scores[player_number] + games_points[game_name]
    elif game_name == "penalty":
        players_scores[player_number] = players_scores[player_number] - penalty
    elif game_name == "bonus":
        players_scores[player_number] = players_scores[player_number] + bonus
    elif game_name == "lottery":
        players_scores[player_number] = players_scores[player_number] + lottery
    elif game_name == "payday":
        players_scores[player_number] = players_scores[player_number] + 50

    # if player gives the right answers then player is game owner
    if game_owner == player_number and answer_status == True:
        game_owners[game_name] = player_number
    elif game_owner == "None":
        pass
    elif game_owner != player_number:
        players_scores[game_owner] = players_scores[game_owner] + (games_points[game_name] / 4)


# defining penalty rules
def penalty(player, game_number):
    penalty_points = [10, 20, 30, 40, 50, 60]
    penalty_points_number = penalty_points[random.randint(0, 5)]
    if game_number - last_game_by_player[player] == 1:
        score_addition(player, "penalty", "None", False, 0, 0, penalty_points_number)
        return penalty_points_number
    elif game_number - last_game_by_player[player] == 2:
        score_addition(player, "penalty", "None", False, 0, 0, 20)
        return 20
    elif game_number - last_game_by_player[player] == 3:
        score_addition(player, "penalty", "None", False, 0, 0, penalty_points_number)
        return penalty_points_number
    elif game_number - last_game_by_player[player] == 4:
        score_addition(player, "penalty", "None", False, 0, 0, 40)
        return 40
    elif game_number - last_game_by_player[player] == 5:
        score_addition(player, "penalty", "None", False, 0, 0, penalty_points_number)
        return penalty_points_number
    elif game_number - last_game_by_player[player] == 6:
        score_addition(player, "penalty", "None", False, 0, 0, 60)
        return 60


# defining bonus rules
def bonus(player, game_number):
    bonus_points = [10, 20, 30, 40, 50, 60]
    bonus_points_number = bonus_points[random.randint(0, 5)]
    if game_number - last_game_by_player[player] == 1:
        score_addition(player, "bonus", "None", False, 0, bonus_points_number, 0)
        return bonus_points_number
    elif game_number - last_game_by_player[player] == 2:
        score_addition(player, "bonus", "None", False, 0, 20, 0)
        return 20
    elif game_number - last_game_by_player[player] == 3:
        score_addition(player, "bonus", "None", False, 0, bonus_points_number, 0)
        return bonus_points_number
    elif game_number - last_game_by_player[player] == 4:
        score_addition(player, "bonus", "None", False, 0, 40, 0)
        return 40
    elif game_number - last_game_by_player[player] == 5:
        score_addition(player, "bonus", "None", False, 0, bonus_points_number, 0)
        return bonus_points_number
    elif game_number - last_game_by_player[player] == 6:
        score_addition(player, "bonus", "None", False, 0, 60, 0)
        return 60


# lottery
def lottery(player):
    lottery_number = random.randint(1, 10)
    print("\nLottery!!\n")
    speak.Speak("\nLottery!!\n")
    print("Description: enter the number between 1 and 10. If Your number is lottery number "
          "then you will get 300 points but if your number is not lottery number then 100 points will be deducted\n")
    speak.Speak("Description: enter the number between 1 and 10. If Your number is lottery number "
          "then you will get 300 points. But if your number is not lottery number then 100 points will be deducted. "
                "Want to play lottery?\n")

    wanna_play = response_return(input("Want to play Lottery"))
    if wanna_play == True:
        bidder_number = int(input("Enter the number between 1 and 10: "))
        if lottery_number == bidder_number:
            score_addition(player, "lottery", "None", False, 300)
            print("\n\tPlayer " + str(player) + " won the lottery!\n")
            speak.Speak("\n\tPlayer " + str(player) + " won the lottery! 300 points are added\n")
        else:
            score_addition(player, "lottery", "None", False, -100)
            print("\n\tlottery number:", lottery_number, "\n\tbetter luck next time.\n")
            speak.Speak("\n\tlottery number:"+ str(lottery_number)+ "\n\tbetter luck next time.\n")
    else:
        print("\nNot Interested\n")


# checks who is the owner of particular game
def who_is_game_owner(game_number, player):
    if game_owners[games_name_with_codes[game_number]] == None:
        return player
    else:
        return game_owners[games_name_with_codes[game_number]]


# check remaining turns
def update_remaining_chances(player, game_number, last_game):
    players_remaining_chances[player] = players_remaining_chances[player] - (game_number - last_game)
    return players_remaining_chances[player]


# main executing function
while True:
    number_of_players = int(input('Enter the number of players: '))  # number of players to be played
    players_details_name = {}  # names of the players
    players_details_email = {}  # email of the players
    players_scores = {}  # score of the players
    players_remaining_chances = {}  # number of steps remaining per player
    last_game_by_player = {}  # last played game(number) by player
    players_who_loose_chance = {}  # players which are in jail
    game_owners = {"guess_the_movie_with_the_help_of_dialogue": None, "theme_based_movies": None,
                   "bollywood_quiz": None,
                   "marvel_quiz": None, "guess_the_movie_with_the_help_of_music": None,

                   "the_logo_quiz": None, "the_famous_personality": None, "logical_puzzle": None, "bonus": None,
                   "basic_gk": None, "slogans": None,

                   "identify_the_artist": None, "guess_the_song": None, "duet": None, "music_quiz": None,
                   "golden_era": None,
                   "payday": None,
                   "riddles_level_1": None, "read_out_the_color": None, "riddles_level_2": None,
                   "riddles_level_3": None,
                   "reverse": None
                   }  # owner(player) of the game by default None

    games_name_with_codes = {1: "identify_the_artist", 2: "guess_the_song", 3: "duet",4: "penalty", 5: "music_quiz",
                             6: "golden_era",7: "lottery",
                             8: "guess_the_movie_with_the_help_of_dialogue", 9: "theme_based_movies",
                             10: "bollywood_quiz",11: "penalty",
                             12: "marvel_quiz", 13: "guess_the_movie_with_the_help_of_music",
                             14: "jail",
                             15: "the_logo_quiz", 16: "the_famous_personality", 17: "logical_puzzle", 18: "bonus",
                             19: "basic_gk", 20: "slogans",
                             21: "payday",
                             22: "riddles_level_1", 23: "read_out_the_color", 24: "riddles_level_2", 25: "bonus",
                             26: "riddles_level_3", 27: "reverse"}  # particular game code(number)

    # setting score equals to zero
    # setting player_in_jail value equals to zero
    # setting last game value of each player equal to zero
    for _ in range(1, number_of_players + 1):
        players_scores[_] = 0
        players_who_loose_chance[_] = 0
        last_game_by_player[_] = 0

    # remaining chances
    for _ in range(1, number_of_players + 1):
        players_remaining_chances[_] = 27

    # player details input
    for _ in range(1, number_of_players + 1):
        players_details_name[_] = input("Enter Player " + str(_) + " Name: ")
        # players_details_email[_] = input("Enter Player " + str(_) + " Email")

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak("Description and rules of the games:\n. Each player will play 1 round only. "
                "\n. According to their dice number game will be organised. \n. If a player wins any game and another"
                " player arrives at that game then 1 by fourth points will be added to 1st winner of that particular game.\n"
                " lets begin the game!")
    while True:
        for player in range(1, number_of_players + 1):
            if players_remaining_chances[player] >= 0:
                # checking that a player is in jail or not
                if last_game_by_player[player] == 14 and players_who_loose_chance[player] == 1:
                    print("\n\tPlayer "+str(player) + " Wait for next chance.\n")
                    speak.Speak("\n\tPlayer "+str(player) + " Wait for next chance.\n")
                    players_who_loose_chance[player] = 0
                    continue
                while True:
                    dice_number = input("Enter the Dice Number of player " + str(player) + " :")
                    if dice_number.isdigit()==True and 1 <= int(dice_number) <= 6:
                        break
                    else:
                        print("\nEnter the valid Dice Number\n")
                # converting dice to game board number
                game_number = int(dice_number) + last_game_by_player[player]
                if game_number > 27:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    print("\n\t\tPlayer " + str(player) + " has completed his round\n")
                    speak.Speak("\n\t\tPlayer " + str(player) + " has completed his round\n")
                    last_game_by_player[player] = game_number
                    continue
                elif game_number == 4 or game_number == 18:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    penalty_points= penalty(player, game_number)
                    print("\n\tPenalty! of ",penalty_points," points\n")
                    speak.Speak("\n\tPenalty! of "+ str(penalty_points)+" points\n")
                    last_game_by_player[player] = game_number
                    continue
                elif game_number == 11 or game_number == 25:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    bonus_points=bonus(player, game_number)
                    print("\n\tBonus! of ", bonus_points," points\n")
                    speak.Speak("\n\tBonus! of "+str(bonus_points)+" points\n")
                    last_game_by_player[player] = game_number
                    continue
                elif game_number == 7:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    lottery(player)
                    last_game_by_player[player] = game_number
                    continue
                # setting chance loosing concept
                elif game_number == 14:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    players_who_loose_chance[player] = 1
                    last_game_by_player[player] = game_number
                    print("Wait in jail for 1 chance")
                    speak.Speak("Wait in jail for 1 chance")
                    continue
                elif game_number == 21:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    print('\n\tPayday: add 50 points\n')
                    speak.Speak('\n\tPayday: add 50 points\n')
                    score_addition(player, "payday", "None", False)
                    last_game_by_player[player] = game_number
                    continue
                game_owner = who_is_game_owner(game_number, player)
                score_addition(player, games_name_with_codes[game_number], game_owner, game_chooser(game_number))
                update_remaining_chances(player, game_number, last_game_by_player[player])

                last_game_by_player[player] = game_number

            else:
                continue

        # printing the scores of each player after each round
        print()
        for _ in range(1, number_of_players + 1):
            print("Player " + str(_) + " score is " + str(players_scores[_]))
        print()

        # checking all the players have completed the 1 round completely
        counter1 = 0
        for values in last_game_by_player.values():
            if values > 27:
                counter1 = counter1 + 1
        if counter1 == number_of_players:
            print()
            speak.Speak("final scores of the players are:\n")
            result=[]
            for _ in range(1, number_of_players + 1):
                print("Player " + str(_) + " score is " + str(players_scores[_]))
                speak.Speak("Player " + str(_) + " score is " + str(players_scores[_]))
                result.append(players_scores[_])
                result.sort()
            print("\n\t\t\tGAME OVER\n\n")
            speak.Speak("GAME OVER\n"
                        "Hope you enjoyed the Game!")
            break
