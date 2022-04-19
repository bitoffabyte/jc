import LSB as LSB
import PhaseCoding as PhaseCoding
import regex

def option(choose):
    '''
	Choose an action
	'''
    while True:
        choice = int(input("Option: "))
        if choice == 1:
            AudioPath = input("Enter the filepath you want to encode: ")
            hidden_message = input("Enter your message you want to hide: ")
            if choose == 1:
                result = LSB.encode(AudioPath, hidden_message)
            elif choose == 2:
                result = PhaseCoding.encode(AudioPath,hidden_message)
            print(f"Sucessfully encoded message from {result}")
            break
        elif choice == 2:
            filepath_decode = input("Enter the filepath you want to decode: ")
            if choose == 1:
                message = LSB.decode(filepath_decode)
            elif choose == 2:
                message = PhaseCoding.decode(filepath_decode)
            print(message)
            break
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please try again.")
            continue

def StartProgram():
    '''
    Start function
    '''
    
    while True:
        print("""
        ____________________________________

        Instruction:
        0: Quit.
        1: Steganography using LSB.
        2: Steganography using Phase Coding.
        ____________________________________
        """)

        choose = int(input("Your choice: "))
        if choose == 0:
            quit()
        elif choose == 1:
            print("""
            Choose an action:
                1) Encode.
                2) Decode.
                3) Quit.""")
            option(choose)
        elif choose == 2:
            print("""
            Choose an action:
                1) Encode.
                2) Decode.
                3) Quit.""")
            option(choose)
        else:
            print("\nInvalid option! Please try again.")
            continue

#Run program
if __name__ == '__main__':
    StartProgram()