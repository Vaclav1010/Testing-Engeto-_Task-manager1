seznam_ukolu = []


def hlavni_menu():
    

    while True:
        print("Spravce ukolu - Hlavni menu")
        print("1. Pridat novy ukol\n2. Zobrazit vsechny ukoly\n3. Odstranit ukol\n4. Konec programu")
        user_choice = input("Vyberte moznost (1-4):")
        
        if user_choice == "1":
            task_name = input("\nZadej nazev ukolu: ")
            task_description = input("Zadej popis ukolu: ")
            pridat_ukol(task_name,task_description)

        elif user_choice == "2":
            zobrazit_ukoly(seznam_ukolu)  

        elif user_choice == "3":
            zobrazit_ukoly(seznam_ukolu)
            odstranit_ukol()

        elif user_choice == "4":
            print("\nKonec programu.")
            exit()
        
        else:
            print("\nNeplatna volba!\n")
           
        
def pridat_ukol(task_name,task_description):

    for ukol in seznam_ukolu:
        if task_name in ukol and task_description in ukol:
            print(">> Duplicitni nazev a popis ukolu. Nelze provest.\n".upper())
            return

    while True:

        if task_name == "" or task_description == "":
            print("K přidání úkolu je potřeba vyplnit název a popis.")
            task_name = input("\nZadej název úkolu: ")
            task_description = input("Zadej popis úkolu: ")
        else:
            seznam_ukolu.append(f"{task_name} - {task_description}")
            print(f"Úkol '{task_name}' byl přidán do seznamu úkolů.\n")
            break


def zobrazit_ukoly(seznam_ukolu):
    print("\nSeznam ukolu:")
    if seznam_ukolu == []:
        print("Seznam ukolu neobsahuje zadna data.")

    for idx,each in enumerate(seznam_ukolu):
            print(f"{idx+1}. {each}")
    print()


def odstranit_ukol():
    while True:

        if seznam_ukolu == []:
            print(">> Odstraneni ukolu neni mozne provest. Seznam je prazdny!\n".upper())
            break

        try:
            delete_number = int(input("Zadej cislo úkolu k odstranění: "))

            if 1 <= delete_number <= len(seznam_ukolu):
                    removed_task = seznam_ukolu.pop(delete_number - 1)
                    print(f"Ukol '{removed_task}' byl odstranen.\n")
                    break
            else:
                print(f"Úkol s cislem '{delete_number}' není v seznamu úkolů!\n")               
        except ValueError:
            print("Neplatný vstup! Zadej prosím číslo.\n")

            
hlavni_menu()
