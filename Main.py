'''
Project Name:Fun Monopoly
Author: Adamaya Sharma
last Modified: 24/11/2019
Version: 1.3.2

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

1=> "guess_the_movie_with_the_help_of_dialogue"                 2=> "theme_based_movies"
3=> "bollywood_quiz"                                            4=> "penalty"
5=> "marvel_quiz"                                               6=> "guess_the_movie_with_the_help_of_music"
7=> "lottery"                                                   8=> "the_logo_quiz"
9=> "the_famous_personality"                                    10=> "logical_puzzle"
11=> "bonus"                                                    12=> "basic_gk"
13=> "slogans"                                                  14=> "jail",
15=> "identify_the_artist"                                      16=> "guess_the_song"
17=> "duet"                                                     18=> "penalty"
19=> "music_quiz"                                               20=> "slogans"
21=> "payday"                                                   22=> "riddles_level_1"
23=> "read_out_the_color"                                       24=> "riddles_level_2"
25=> "bonus"                                                    26=> "riddles_level_3"
27=> "reverse"
'''

import random
import PIL.Image
import time
from pygame import mixer  # Load the popular external library


# checking that answer is correct or wrong
def response_return(request):
    if request.lower()=='y':
        return True
    elif request.lower()=='n':
        return False
    else:
        print("\nWrong Input\n")
        response_return(input('Answer is Correct or Wrong: \nY\t\tN\n'))
# game chooser function created


def game_chooser(game_number):
    # Entertainment: Guess the movie (with the help of dialogue)
    if game_number == 1:
        print("\nGame " + str(game_number) + ": GUESS THE MOVIE (with the help of dialogue)")
        questions = ["TENSION LENE KA NHI SIRF DENE KA", "LIFE MAI SBSE BADA RISK HOTA H KBHI KOI RISK NHI LENA",
                     "MAI APNI FAVOUITE HOON", "TUMSE NA HO PAYEGA", "PALAT, PALAT, PALAT!!!",
                     "AAP CONVINCE HOGYE KI MAI AUR BOLU",
                     "USKA TO NA BAD LUCK HI KHRAAB HAI",
                     "AADMI TBHI BADA BNTA HAI JB BADE LOG USSE MILNE LA ITNEZAAR KARE",
                     "KAHI PR PAHUCHNE K LIYE KAHI SE NIKLNA ZARURI H", "INSAAN NAAM MAI MAZHAB DHUND LETA HAI",
                     "KHAAMOSH!!!!", "PREM NAAM HAI MERA , PREM CHOPRA", "PICHAR ABHI BAAKI HAI MERE DOST",
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
        print("\nDialogue Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Entertainment: THEME BASED MOVIES
    elif game_number == 2:
        print("\nGame " + str(game_number) + ": THEME BASED MOVIES")
        questions = ["5 MOVIES RELATED TO – SPORTS", "5 PATRIOTIC MOVIES", "5 WOMEN EMPOWERMENT MOVIES",
                     "5 HORROR MOVIES", "5 ROMANTIC MOVIES", "5 COMEDY MOVIES", "5 THRILLER MOVIES"]
        random_number = random.randint(0, 6)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN\n")
        response_return(response)

    # Entertainment: BOLLYWOOD QUIZ
    elif game_number == 3:
        print("\nGame " + str(game_number) + ": BOLLYWOOD QUIZ")
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
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Entertainment: QUIZ RELATED TO (DISNEY, MARVEL, CARTOONS)
    elif game_number == 5:
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
                     "T’CHALLA IS THE BLACK PANTHER SO WHAT IS HIS FATHER’S NAME ?"
                     "REAL VOICE BEHIND DOREAMON", "NAME ANY 5 CHARACTER OF MICKEY MOUSE",
                     "NAME THE THREE POWERPUFF GIRLS",
                     "BROTHER’S NAME OF PRETTI IN HADI MERA BUDDY",
                     "WHAT WAS THE NAME OF DORA’S MONKEY?", "WHO DIES IN GUARDIAN OF GALAXY VOL-1",
                     "IN WHICH KINGDOM CHOTA BHEEM LIVES?", "NAME 5 DISNEY MOVIES"]
        random_number = random.randint(0, 25)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # TODO Add the theme music of movies in game number 6
    # Entertainment: Guess the Movie with the help of Music
    elif game_number == 6:
        print("\nGame " + str(game_number) + ": Guess the Movie with the help of Music")
        questions = ['Cool and Inspiring Background Music.mp3', 'Cool and Inspiring Background Music.mp3']
        random_number = random.randint(0, 1)
        mixer.init()
        mixer.music.load(questions[random_number])
        print("playing song " + str(random_number + 1))
        mixer.music.play()
        time.sleep(30)
        mixer.music.stop()

        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Technology and Famous Personality: The LOGO Quiz
    elif game_number == 8:
        print("\nGame " + str(game_number) + ": The LOGO Quiz")
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
        print("Answer: Image number " + str(random_number + 1))
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Technology and Famous Personality: THE FAMOUS PERSONALITY
    elif game_number == 9:
        print("\nGame " + str(game_number) + ": THE FAMOUS PERSONALITY")
        questions = ['Albert Einstein.jpg', 'denial redcliff.jpg', 'dr APJ Abdul Kalam.jpg', 'Elon Musk.jpg',
                     'Jack ma.jpg',
                     'jenifer lawrence.jpg', 'jk rowling.jpg', 'leonardo dicaprio.jpg']
        random_number = random.randint(0, 1)
        image = PIL.Image.open(
            "C:/Users/ADAMAYA SHARMA/PycharmProjects/monoply_fun_and_learn/Famous Personality/" + questions[
                random_number])
        image.show()
        print("Answer: Image number " + str(random_number + 1))
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Technology and Famous Personality: Logical puzzle
    elif game_number == 10:
        print("\nGame " + str(game_number) + ": Logical Puzzle")
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
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Technology and Famous Personality: Basic GK
    elif game_number == 12:
        print("\nGame " + str(game_number) + ": Basic GK")
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
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Technology and Famous Personality: Slogans
    elif game_number == 13:
        print("\nGame " + str(game_number) + ": Slogans")
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
        random_number = random.randint(0, 29)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Music : Identify the Artist
    elif game_number == 15:
        print("\nGame " + str(game_number) + ": Identify the Artist")
        questions = ['Cool and Inspiring Background Music.mp3', 'Cool and Inspiring Background Music.mp3']
        random_number = random.randint(0, 1)
        mixer.init()
        mixer.music.load(questions[random_number])
        print("playing song " + str(random_number + 1))
        mixer.music.play()
        time.sleep(30)
        mixer.music.stop()

        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Music : Guess the Song
    elif game_number == 16:
        print("\nGame " + str(game_number) + ": Guess the song")
        questions = ['Cool and Inspiring Background Music.mp3', 'Cool and Inspiring Background Music.mp3']
        random_number = random.randint(0, 1)
        mixer.init()
        mixer.music.load(questions[random_number])
        print("playing song " + str(random_number + 1))
        mixer.music.play()
        time.sleep(30)
        mixer.music.stop()

        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Music : Duet
    elif game_number == 17:
        print("\nGame " + str(game_number) + ": Duet")
        questions = ['Cool and Inspiring Background Music.mp3', 'Cool and Inspiring Background Music.mp3']
        random_number = random.randint(0, 1)
        mixer.init()
        mixer.music.load(questions[random_number])
        print("playing song " + str(random_number + 1))
        mixer.music.play()
        time.sleep(30)
        mixer.music.stop()

        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Music : Music Quiz
    elif game_number == 19:
        print("\nGame " + str(game_number) + ": Music Quiz")
        questions = ['Cool and Inspiring Background Music.mp3', 'Cool and Inspiring Background Music.mp3']
        random_number = random.randint(0, 1)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # Music : Golden Era
    elif game_number == 20:
        print("\nGame " + str(game_number) + ": Golden Era")
        questions = ['Cool and Inspiring Background Music.mp3', 'Cool and Inspiring Background Music.mp3']
        random_number = random.randint(0, 1)
        mixer.init()
        mixer.music.load(questions[random_number])
        print("playing song " + str(random_number + 1))
        mixer.music.play()
        time.sleep(30)
        mixer.music.stop()

        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # IQ: Riddles (Level 1)
    elif game_number == 22:
        print("\nGame " + str(game_number) + ": Riddles (Level 1)")
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
        random_number = random.randint(0, 25)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # IQ: Read Out The Color
    elif game_number == 23:
        print("\nGame " + str(game_number) + ": Read Out The Color")
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
        random_number = random.randint(0, 25)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # IQ: Riddles (Level 2)
    elif game_number == 24:
        print("\nGame " + str(game_number) + ": Riddles (Level 2)")
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
        random_number = random.randint(0, 25)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # IQ: Riddles (Level 3)
    elif game_number == 26:
        print("\nGame " + str(game_number) + ": Riddles (Level 3)")
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
        random_number = random.randint(0, 25)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

    # IQ: Reverse it out
    elif game_number == 27:
        print("\nGame " + str(game_number) + ": Reverse it Out")
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
        random_number = random.randint(0, 25)
        print("\nQuestion Number :" + str(random_number + 1))
        print(questions[random_number])
        response = input("Answer is Correct or Wrong: \nY\t\tN")
        response_return(response)

# adding game scores
def score_addition(player_number, game_name, game_owner, answer_status, lottery=0, bonus=0, penalty=0):
    games_points = {"guess_the_movie_with_the_help_of_dialogue": 100, "theme_based_movies": 200, "bollywood_quiz": 300,
                    "marvel_quiz": 100, "guess_the_movie_with_the_help_of_music": 200,

                    "the_logo_quiz": 100, "the_famous_personality": 200, "logical_puzzle": 300, "basic_gk": 200,
                    "slogans": 100,

                    "identify_the_artist": 200, "guess_the_song": 100, "duet": 300, "music_quiz": 100,
                    "golden_era": 200,

                    "riddles_level_1": 100, "read_out_the_color": 150, "riddles_level_2": 200, "riddles_level_3": 300,
                    "reverse": 250}

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

    # if player gives the write answers then player is game owner
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
    bidder_number = int(input("Enter the number between 1 and 10: "))
    if lottery_number == bidder_number:
        score_addition(player, "lottery", "None", False, 500)
        print("Player " + str(player) + " won the lottery!")
    else:
        score_addition(player, "lottery", "None", False, -100)
        print("lottery number:", lottery_number, "\n better luck next time.")


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
    number_of_players = int(input('Enter the number of players'))  # number of players to be played
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

    games_name_with_codes = {1: "guess_the_movie_with_the_help_of_dialogue", 2: "theme_based_movies",
                             3: "bollywood_quiz",
                             4: "penalty", 5: "marvel_quiz", 6: "guess_the_movie_with_the_help_of_music",
                             7: "lottery",
                             8: "the_logo_quiz", 9: "the_famous_personality", 10: "logical_puzzle", 11: "bonus",
                             12: "basic_gk", 13: "slogans",
                             14: "jail",
                             15: "identify_the_artist", 16: "guess_the_song", 17: "duet", 18: "penalty",
                             19: "music_quiz",
                             20: "slogans",
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

    while True:
        for player in range(1, number_of_players + 1):
            if players_remaining_chances[player] >= 0:
                # checking that a player is in jail or not
                if last_game_by_player[player] == 14 and players_who_loose_chance[player] == 1:
                    print(str(player) + " wait for next chance.")
                    players_who_loose_chance[player] = 0
                    continue
                while True:
                    dice_number = int(input("Enter the Dice Number of player " + str(player) + " :"))
                    if 1 <= dice_number <= 6:
                        break
                    else:
                        print("Enter the valid Dice Number\n")
                # converting dice to game board number
                game_number = dice_number + last_game_by_player[player]
                if game_number > 27:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    print("Player " + str(player) + " has completed his round")
                    last_game_by_player[player] = game_number
                    continue
                elif game_number == 4 or game_number == 18:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    print("Penalty! of ", penalty(player, game_number))
                    last_game_by_player[player] = game_number
                    continue
                elif game_number == 11 or game_number == 25:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    print("Bonus! of ", bonus(player, game_number))
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
                    continue
                elif game_number == 21:
                    update_remaining_chances(player, game_number, last_game_by_player[player])
                    print('\n\tPayday: add 50 points\n')
                    score_addition(player, "payday", "None", False)
                    last_game_by_player[player] = game_number
                    continue
                game_owner = who_is_game_owner(game_number, player)
                score_addition(player, games_name_with_codes[game_number], game_owner, game_chooser(game_number))
                update_remaining_chances(player, game_number, last_game_by_player[player])

                last_game_by_player[player] = game_number

            else:
                continue

        # checking all the players have completed the 1 round completely
        counter = 0
        for values in last_game_by_player.values():
            if values > 27:
                counter = counter + 1
        if counter == number_of_players:
            for _ in range(1, number_of_players + 1):
                print("Player " + str(_) + " score is " + str(players_scores[_]))
            break
