while True:
    import random
    print(" This is dice rolling game ")
    print("press enter to roll dice")
    input()
    number = random.randint(1,6)
    if number == 1:
        print("[-------------------------------]")
        print("[                               ]")
        print("[              0                ]")
        print("[                               ]")
        print("[-------------------------------]")
    if number ==2 :
        print("[-------------------------------]")
        print("[                               ]")
        print("[           0     0             ]")
        print("[                               ]")
        print("[-------------------------------]")
    if number ==3 :
        print("[-------------------------------]")
        print("[                               ]")
        print("[          0   0   0            ]")
        print("[                               ]")
        print("[-------------------------------]")
    if number == 4:
        print("[-------------------------------]")
        print("[                               ]")
        print("[           0    0              ]")
        print("[           0    0              ]")
        print("[                               ]")
        print("[-------------------------------]")
    if number == 5:
        print("[-------------------------------]")
        print("[                               ]")
        print("[           0     0             ]")
        print("[              0                ]")
        print("[           0     0             ]")
        print("[                               ]")
        print("[-------------------------------]")
    if number == 6:
        print("[-------------------------------]")
        print("[                               ]")
        print("[           0    0              ]")
        print("[           0    0              ]")
        print("[           0    0              ]")
        print("[                               ]")
        print("[-------------------------------]")
        
