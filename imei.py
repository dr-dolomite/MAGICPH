"""
Generates random IMEI numbers.

The user specifies the 8-digit TAC and up to 4-digits of the serial number.
The user also specifies the number of random IMEIs to generate.
"""

import sys
import random
import os
import datetime


# Src: https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/luhn.py
def checksum(number, alphabet="0123456789"):
    """
    Calculate the Luhn checksum over the provided number.

    The checksum is returned as an int.
    Valid numbers should have a checksum of 0.
    """
    n = len(alphabet)
    number = tuple(alphabet.index(i) for i in reversed(str(number)))
    return (sum(number[::2]) + sum(sum(divmod(i * 2, n)) for i in number[1::2])) % n


def calc_check_digit(number, alphabet="0123456789"):
    """Calculate the extra digit."""
    check_digit = checksum(number + alphabet[0])
    return alphabet[-check_digit]


def save_to_file(imei_list, name):
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = "Generated IMEIs"
    filename = f"{name}_{current_datetime}.txt"
    file_path = os.path.join(folder_name, filename)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(file_path, "w") as file:
        for imei in imei_list:
            imei = imei.strip()  # Remove leading and trailing whitespace
            file.write(imei + "\n")


def clear_screen():
    """Clear the screen."""
    os.system("cls" if os.name == "nt" else "clear")


def generate_custom_imei():
    clear_screen()
    print(
        "\n Provide your own IMEI prefix here."
        "You can copy it from your own source and delete 3 digits or 5 digits of the IMEI.\n"
    )
    start = str(input(" Enter the first 8 - 12 digits: ")).strip()
    name = "Random IMEI"
    return start, name


def generate_smart_unlidata_imei(
    promaxA, promaxB, mq725, smarthome5G, smart5GRocket, R291, SamsungIMEI, GoogleIMEI
):
    clear_screen()
    print(" ======================================================================")
    print(
        "\n Choose your Smart Unlidata promo: \n"
        " 1. Smartbro Unlidata 999 \n"
        " 2. Smartbro / Famsim Unlidata 1299 \n"
        " 3. Unlidata 499 \n"
        " 4. Unli 5G promos \n"
        " 5. Go back \n"
    )
    print(" ======================================================================")
    option = int(input(" Enter your choice: "))

    if option == 1:
        clear_screen()
        print(" ======================================================================")
        print(
            "\n Choose your preferred IMEI: \n"
            "1. Iphone IMEI \n"
            "2. Smartbro Pocket Wifi IMEI \n"
            "3. Go back \n"
        )
        print(" ======================================================================")
        second_option = int(input("Enter your choice: "))

        if second_option == 1:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose your preferred IMEI: \n"
                " 1. Iphone 14 Pro Max \n"
                " 2. Iphone 15 Pro Max \n"
                " 3. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(promaxA).strip()
                name = "Iphone 14 Pro Max IMEI"

            elif third_option == 2:
                start = str(promaxB).strip()
                name = "Iphone 15 Pro Max IMEI"

            elif third_option == 3:
                clear_screen()
                main()

        elif second_option == 2:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose your preferred IMEI: \n"
                " 1. Smartbro MQ725 \n"
                " 2. Smartbro 5G Rocket Wifi \n"
                " 3. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(mq725).strip()
                name = "Smartbro MQ725 IMEI"

            elif third_option == 2:
                start = str(smart5GRocket).strip()
                name = "Smart Bro 5G Rocket WiFi IMEI"

            elif third_option == 3:
                clear_screen()
                main()

        elif second_option == 3:
            clear_screen()
            main()

    elif option == 2:
        clear_screen()
        print(" ======================================================================")
        print(
            "\n Choose your preferred IMEI: \n"
            " 1. Smartbro Home Wifi 5G \n"
            " 2. Smartbro Home Wifi R291 \n"
            " 3. Go back \n"
        )
        print(" ======================================================================")
        second_option = int(input(" Enter your choice: "))

        if second_option == 1:
            start = str(smarthome5G).strip()
            name = "Smartbro Home 5G IMEI"

        elif second_option == 2:
            start = str(R291).strip()
            name = "Smartbro Home Wifi R291 IMEI"

        elif second_option == 3:
            clear_screen()
            main()

        else:
            print(" Invalid input")
            main()

    elif option == 3:
        clear_screen()
        print(" ======================================================================")
        print(
            "\n Choose your preferred IMEI: \n"
            " 1. Iphone IMEI \n"
            " 2. Samsung IMEI \n"
            " 3. Google IMEI \n"
            " 4. Exit \n"
        )
        print(" ======================================================================")
        second_option = int(input(" Enter your choice: "))

        if second_option == 1:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose your preferred IMEI: \n"
                " 1. Iphone 14 Pro Max \n"
                " 2. Iphone 15 Pro Max \n"
                " 3. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(promaxA).strip()
                name = "Iphone 14 Pro Max IMEI"

            elif third_option == 2:
                start = str(promaxB).strip()
                name = "Iphone 15 Pro Max IMEI"

            elif third_option == 3:
                clear_screen()
                main()

        elif second_option == 2:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose your preferred IMEI: \n"
                " 1. Samsung Galaxy S23 Ultra \n"
                " 2. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(SamsungIMEI).strip()
                name = "Samsung Galaxy S23 Ultra IMEI"

            elif third_option == 2:
                clear_screen()
                main()

            else:
                print(" Invalid input")
                main()

        elif second_option == 3:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose your preferred IMEI: \n"
                " 1. Google Pixel 8 Pro \n"
                " 2. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(GoogleIMEI).strip()
                name = "Google Pixel 8 Pro IMEI"

            elif third_option == 2:
                clear_screen()
                main()

            else:
                print(" Invalid input")
                main()

    elif option == 4:
        clear_screen()
        print(" ======================================================================")
        print(
            "\n Choose your preferred IMEI: \n"
            " 1. Iphone IMEI \n"
            " 2. Samsung IMEI \n"
            " 3. Google IMEI \n"
            " 4. Exit \n"
        )
        print(" ======================================================================")
        second_option = int(input(" Enter your choice: "))

        if second_option == 1:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose your preferred IMEI: \n"
                " 1. Iphone 14 Pro Max \n"
                " 2. Iphone 15 Pro Max \n"
                " 3. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(promaxA).strip()
                name = "Iphone 14 Pro Max IMEI"

            elif third_option == 2:
                start = str(promaxB).strip()
                name = "Iphone 15 Pro Max IMEI"

            elif third_option == 3:
                clear_screen()
                main()

        elif second_option == 2:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose your preferred IMEI: \n"
                " 1. Samsung Galaxy S23 Ultra \n"
                " 2. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(SamsungIMEI).strip()
                name = "Samsung Galaxy S23 Ultra IMEI"

            elif third_option == 2:
                clear_screen()
                main()

            else:
                print(" Invalid input")
                main()

        elif second_option == 3:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose your preferred IMEI: \n"
                " 1. Google Pixel 8 Pro \n"
                " 2. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(GoogleIMEI).strip()
                name = "Google Pixel 8 Pro IMEI"

            elif third_option == 2:
                clear_screen()
                main()

            else:
                print(" Invalid input")
                main()

    elif option == 5:
        clear_screen()
        main()

    else:
        print(" Invalid input")
        main()

    return start, name


def generate_other_imei(
    sdx62,
    sdx55,
    sdx65,
    ZTECat12,
    huaCPEpro2,
    MC888s,
    Unilink200,
    ZLTX21,
    MC801A,
    WA2000,
    K10,
):
    clear_screen()
    print(" ======================================================================")
    print(
        "\n Choose your preferred IMEI: \n"
        " 1. Quectel IMEIs \n"
        " 2. ZTE IMEIs \n"
        " 3. Huawei IMEIs \n"
        " 4. DITO IMEIs \n"
        " 5. Go back \n"
    )
    print(" ======================================================================")
    option = int(input(" Enter your choice: "))

    if option == 1:
        clear_screen()
        print(" ======================================================================")
        print(
            "\n Choose your preferred IMEI: \n"
            " 1. RM520 (X62) IMEI \n"
            " 2. RM500 (X55) IMEI \n"
            " 3. RM521F (X65) IMEI \n"
            " 4. Go back \n"
        )
        print(" ======================================================================")
        second_option = int(input(" Enter your choice: "))

        if second_option == 1:
            start = str(sdx62).strip()
            name = "Quectel RM520 (X62) IMEI"

        elif second_option == 2:
            start = str(sdx55).strip()
            name = "Quectel RM500 (X55) IMEI"

        elif second_option == 3:
            start = str(sdx65).strip()
            name = "Quectel RM521F (X65) IMEI"

        elif second_option == 4:
            clear_screen()
            main()

        else:
            print(" Invalid input")
            main()

    elif option == 2:
        clear_screen()
        print(" ======================================================================")
        print(
            "\n Choose your preferred IMEI: \n" "1. ZTE MF289D IMEI \n" "2. Go back \n"
        )
        print(" ======================================================================")
        second_option = int(input(" Enter your choice: "))

        if second_option == 1:
            start = str(ZTECat12).strip()
            name = "ZTE MF289D IMEI"

        elif second_option == 2:
            clear_screen()
            main()

        else:
            print(" Invalid input")
            main()

    elif option == 3:
        clear_screen()
        print(" ======================================================================")
        print(
            "\n Choose your preferred IMEI: \n"
            " 1. Huawei 5G CPE PRO2 IMEI \n"
            " 2. Go back \n"
        )
        print(" ======================================================================")
        second_option = int(input(" Enter your choice: "))

        if second_option == 1:
            start = str(huaCPEpro2).strip()
            name = "Huawei 5G CPE PRO2 IMEI"

        elif second_option == 2:
            clear_screen()
            main()

        else:
            print(" Invalid input")
            main()

    elif option == 4:
        clear_screen()
        print(" ======================================================================")
        print(
            "\n Choose IMEI type: \n"
            " 1. Prepaid \n"
            " 2. Postpaid \n"
            " 3. Go back \n"
        )
        print(" ======================================================================")
        second_option = int(input(" Enter your choice: "))

        if second_option == 1:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose DITO PREPAID IMEI option: \n"
                " 1. ZTE MC888s IMEI \n"
                " 2. Unilink 200 IMEI \n"
                " 3. ZLT X21 IMEI \n"
                " 4. ZTE MC801A IMEI \n"
                " 5. ZTE K10 IMEI \n"
                " 0. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(MC888s).strip()
                name = "ZTE MC888s IMEI"

            elif third_option == 2:
                start = str(Unilink200).strip()
                name = "Unilink 200 IMEI"

            elif third_option == 3:
                start = str(ZLTX21).strip()
                name = "ZLT X21 IMEI"

            elif third_option == 4:
                start = str(MC801A).strip()
                name = "ZTE MC801A IMEI"
            
            elif third_option == 5:
                start = str(K10).strip()
                name = "ZTE K10 IMEI"

            elif third_option == 0:
                clear_screen()
                main()

            else:
                print(" Invalid input")
                main()

        elif second_option == 2:
            clear_screen()
            print(
                " ======================================================================"
            )
            print(
                "\n Choose DITO POSTPAID IMEI option: \n"
                " 1. Fiberhome WA2000 IMEI \n"
                " 2. Go back \n"
            )
            print(
                " ======================================================================"
            )
            third_option = int(input(" Enter your choice: "))

            if third_option == 1:
                start = str(WA2000).strip()
                name = "Fiberhome WA2000 IMEI"

            elif third_option == 2:
                clear_screen()
                main()

            else:
                print(" Invalid input")
                main()

        elif second_option == 3:
            clear_screen()
            main()

        else:
            print(" Invalid input")
            main()

    elif option == 5:
        clear_screen()
        main()

    else:
        print(" Invalid input")
        main()

    return start, name


def main():
    """Ask for the base IMEI, how many to generate, then generate them."""
    # Loop until the first 8-12 digits have been received & are valid
    start = ""
    sdx62 = 868371050431
    sdx55 = 864088060046
    sdx65 = 86178206000

    # Phone IMEIS
    promaxA = 357917871944
    promaxB = 356303480863
    SamsungIMEI = 354721880318
    GoogleIMEI = 358632951367

    huaCPEpro2 = 866887041463
    ZTECat12 = 867389050604

    # DITO IMEIs
    MC888s = 867336060091
    Unilink200 = 867629050213
    ZLTX21 = 864410040377
    MC801A = 863671043425
    WA2000 = 869955060170
    K10 = 861555061278

    # Smart IMEIs
    mq725 = 354386080883
    smarthome5G = 351624350028
    smart5GRocket = 359855100313
    R291 = 868579060149

    # fix menu

    while True:
        try:
            clear_screen()
            print(
                " ======================================================================\n"
            )
            print(
                "                     Welcome to IMEI Generator by RUS                    "
            )
            print(
                "               Type the number of your choice and press Enter.           "
            )
            print(
                "\n ======================================================================"
            )
            print(
                " Choose generator option: \n"
                " 1. Generate from your IMEI Prefix \n"
                " 2. For Smart Unlidata Promos \n"
                " 3. Other device IMEIs \n"
                " 4. Exit"
            )
            print(
                " ======================================================================"
            )
            choice = int(input(" Enter your choice: "))

            if choice == 1:
                start, name = generate_custom_imei()
                break

            elif choice == 2:
                start, name = generate_smart_unlidata_imei(
                    promaxA, promaxB, mq725, smarthome5G, smart5GRocket, R291, SamsungIMEI, GoogleIMEI
                )
                break

            elif choice == 3:
                start, name = generate_other_imei(
                    sdx62,
                    sdx55,
                    sdx65,
                    ZTECat12,
                    huaCPEpro2,
                    MC888s,
                    Unilink200,
                    ZLTX21,
                    MC801A,
                    WA2000,
                    K10
                )
                break

            elif choice == 4:
                clear_screen()
                print("\n Closing the application...")
                print("\n Application closed.")
                sys.exit()

            else:
                print(" Invalid input")
                main()

        except KeyboardInterrupt:
            print("")
            sys.exit()

        # If all conditions are met, the input is valid
        if start.isdigit() and len(start) >= 8 and len(start) <= 12:
            break

        # Tell the user why their input is  invalid
        if not start.isdigit():
            print("***  Invalid input: you must enter digits only\n")
        elif len(start) <= 8:
            print("***  Invalid input: you must enter at least 8 digits\n")
        elif len(start) >= 12:
            print("***  Invalid input: you must enter no more than 12 digits\n")

    # Loop until we know how many random numbers to generate
    count = 0
    while True:
        try:
            count_input = str(
                input(" Enter the number of IMEI numbers to generate: ")
            ).strip()
            print(
                " ======================================================================"
            )
        except KeyboardInterrupt:
            print("")
            sys.exit()

        # If all conditions are met, the input is valid
        if count_input.isdigit() and int(count_input) > 0:
            count = int(count_input)
            break

        # Tell the user that they need to enter a number > 0
        print("***  Invalid input: you must enter a number greater than zero\n")

    # IMEIs will be generated based on the first 8 digits (TAC; the number
    #   used to identify the model) and the next 2-6 digits (partial serial #).
    #   The final, 15th digit, is the Luhn algorithm check digit.

    # Generate and print random IMEI numbers
    imei_list = []  # Store generated IMEIs in a list
    for _ in range(count):
        imei = start

        # Randomly compute the remaining serial number digits
        while len(imei) < 14:
            imei += str(random.randint(0, 9))

        # Calculate the check digit with the Luhn algorithm
        imei += calc_check_digit(imei)
        imei_list.append(imei)  # Add IMEI to the list
        print(" ", imei)

    # Save generated IMEIs to a text file
    save_to_file(imei_list, name)

    print("")
    print(" ======================================================================")
    choiceA = int(input(" Type 1 to generate again or 2 to exit: "))
    if choiceA == 1:
        os.system("cls" if os.name == "nt" else "clear")
        main()

    if choiceA == 2:
        os.system("exit")


# Backwards compatibility (raw_input was renamed to input in Python 3.x)
try:
    # Using Python 2.x; calls to input will be treated as calls to raw_input
    input = raw_input
except NameError:
    # Using Python 3.x; no action required
    pass

if __name__ == "__main__":
    main()
