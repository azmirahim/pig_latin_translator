#   Name: Azmi Rahim
#   Date: Thursday, March 18, 2021
#   Description: This program gives the user instructions on how to use the
#                English -> Pig-Latin translator. It then prompts the user
#                to enter a sentence and outputs the translated sentence in
#                Pig-Latin. The sentence is checked to ensure there are no
#                numbers, punctuation, or uppercase letters in the input. 


# This function outputs the intro, how the translator works,
# and instuctions on how to use the translator.
def instructions():
    """ Outputs an introduction to the translator, how the translator
        works, and how to use the translator.

    Args:
            None

    Returns:
            No value returned. Prints out the translator introduction,
            how it works, and how to use it.
    """

    print("---".center(100))
    print("Welcome to the Pig-Latin Translator!".center(100))               # Outputs: Introduction
    print("---".center(100))
    print("How it Works")                                                   # Outputs: How the translator works
    print("------------")
    print("This translator first allows you to enter a sentence.")
    print("It then translates your sentence to Pig-Latin!")
    print(" ")
    print("How to us the Translator")                                       # Outputs: How to use the translator
    print("------------")
    print("1. Use the prompt below to enter an engligh sentence.")
    print("2. Ensure your sentence does not include any punctuation.")
    print("3. Ensure your sentence does not include any numbers.")
    print("4. Ensure your sentence does not include any uppercase characters.")
    print("5. Ensure there is a white space between every work in your sentence.")
    print(" ")
    print("Lets get started!")                                              # Prompts the user to get started
    print("------------")

# This function asks the user to enter a sentence.
def input_english_text():
    """ Asks the user to enter a sentence of words with only lowercase letters.

    Args:
            None

    Returns:
            sentence(str): The sentence entered by the user.
    """

    count = 0       # Used to count any errors in the user's entry (such as numbers punctuation, uppercase letters)
    while True:
        try:
            sentence = input("Please enter a word or sentence to be translated: ")  # Takes the user's sentence input.
            words = sentence.split()
            for word in words:                                                      # Determines errors in the entry, if any.
                if word.isalpha() != True or word.islower() != True:
                    count += 1
            if len(sentence) == 0:                                                  # If the user enters nothing, it prompts the user to make an entry.
                print("You must make an entry. Please try again.")
                print(" ")
            elif count != 0:                                                        # Prompts the user to enter another sentence if errors are found in the entry.
                count = 0
                print("You must enter lowercase alphabetical characters only. "
                      "Please try again.")
                print(" ")
            else:
                break
        except:
            print("You must make an entry. Please try again.")
            print(" ")

    return sentence

# This function takes the user's sentence and translates it to Pig-Latin.
def translate_to_pig(sentence):
    """ Translates sentence to Pig-Latin.

    Args:
            sentence(str): The sentence to be translated.
            Assumption: The sentence contains only lowercase letters
                        and one white space between each word.

    Returns:
            new_sentence(str): The original sentence translated to Pig-Latin.
    """
    
    word_list = sentence.split()                                        # Creates a list of words in the sentence to be translated
    new_sentence = ""                                                   # This will hold the newly translated sentence.
    
    for word in word_list:                                              # Checks what each word in the sentence starts with and translates it.
        if word[0] in "aeiou":                                          # Translates the word if it starts with a vowel accordingly. 
            new_word = word + "hay"
            new_sentence = new_sentence + " " + new_word
        else:                                                           # Translates the word if it starts with a consonant accordingly. 
            new_word = word.replace(word[0], "", 1) + word[0] + "ay"
            new_sentence = new_sentence + " " + new_word

    return new_sentence                                                 # Returns the original sentence translated. 

# This runs all the functions above to form a fully functioning translator
def main():
    instructions()                                                      # Runs the instruction() function and outputs instructions to the user.
    user_sentence = input_english_text()                                # Stores the user's sentence input.
    sentence_translated = translate_to_pig(user_sentence)               # Stores the translated sentence.
    print("Here is your translated sentence in Pig-Latin:{0}"           # Outputs the translated sentence to the user.
          .format(sentence_translated))
    print(" ")
    print("---".center(100))
    print("Thank you for using the Pig-Latin Translator!".center(100))  # Outputs: Closing statement.
    print("---".center(100))


main()
    

            
            

        

