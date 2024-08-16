"""
Agenda:

Password Strength Checker: Develop a program that evaluates the strength
of a password based on criteria like length, complexity, and the presence 
of special characters. This exercise will help you understand string 
manipulation and validation.

"""
import os
import time


# Utility Functions:
def clear_screen(seconds=None):
    if isinstance(seconds, (int, float)):
        time.sleep(seconds)
        os.system("cls" if os.name == "nt" else "clear")
    elif seconds is None:
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("\033[31mInvalid input for clear_screen\033[0m")
# Main-Program Related Functions:
def password_checker_step1(password_to_check1, specific_reason):
    feedback = {}
    length_requirements = {
        "email account": (12, 16),
        "social media account": (12, 16),
        "financial account": (16, 20),
        "online banking": (16, 20),
        "online shopping account": (12, 16),
        "work/corporate account": (12, 20),
        "wi-fi network": (16, 20),
        "cloud storage account": (16, 20),
        "device login": (8, 12),
        "password manager": (16, 20)
    }
    if specific_reason.endswith("s"):
        specific_reason = specific_reason[:-1]
        
    if specific_reason == "gmail account" or specific_reason == "emails account":
        specific_reason = "email account"
    
    elif (specific_reason == "an account for work" or
          specific_reason == "work account"):
        specific_reason = "work/corporate account"
    
    elif specific_reason == "wifi network":
        specific_reason = "wi-fi network"

    elif (specific_reason == "shoppings account" or
          specific_reason == "online shoppings account"):
        specific_reason = "online shopping account"

    elif specific_reason == "business account":
        specific_reason = "financial account"


    if specific_reason in length_requirements:
        min_len, max_len = length_requirements[specific_reason]
        if len(password_to_check1) not in range(min_len, max_len + 1):
            feedback.update(
                {specific_reason: f"{min_len} between {max_len} characters."}
            )

    if feedback:
        return ("Recommended password length for " + "".join(feedback.keys())
                + " is " + "".join(feedback.values()))
    else:
        bvalue = len(password_to_check1) < 8
        if bvalue:
            return "Your password is less than 8 characters"
 
def password_checker_step2(password_to_check2):
    password_patterns_numerical = {"123456789", "12345678", "1234567", 
                             "123456", "12345", "1234",
                             "123", "12", "1"}
    
    password_patterns_alpabetical = {"abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxy",
                                      "abcdefghijklmnopqrstuvwx", "abcdefghijklmnopqrstuvw", 
                                      "abcdefghijklmnopqrstuv", "abcdefghijklmnopqrstu", 
                                      "abcdefghijklmnopqrst", "abcdefghijklmnopqrs", 
                                      "abcdefghijklmnopqr", "abcdefghijklmnopq", 
                                      "abcdefghijklmnop", "abcdefghijklmno",
                                      "abcdefghijklmn", "abcdefghijkl", 
                                      "abcdefghijk", "abcdefghij", 
                                      "abcdefghi", "abcdefgh", 
                                      "abcdefg", "abcdef", 
                                      "abcde", "abcd", 
                                      "abc", "ab",
                                      "a"}

    
    
    has_numeric_order_pattern = any(pattern == password_to_check2 
                                    for pattern in password_patterns_numerical)
    has_alphebatical_order_pattern = any(pattern == password_to_check2
                                         for pattern in password_patterns_alpabetical)

    feedback = []


    if has_alphebatical_order_pattern:
        feedback.append("alphetical order")
    if has_numeric_order_pattern:
        feedback.append("numeric order")

    if feedback:
        return ("Your password follows " + ", ".join(feedback) + 
                " which can be easy to guess!")

    return ""

def password_checker_step3(password_to_check3):
    special_chars = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                     "-", "_", "=", "+", "[", "]", "{", "}", "|", ";",
                     ":", ",", "<", ">", "?", "/"}
    has_special_char = any(special_char in password_to_check3
                           for special_char in special_chars)
    has_upper_char = any(char.isupper() for char in password_to_check3)
    has_lower_char = any(char.islower() for char in password_to_check3)
    has_digit_char = any(char.isdigit() for char in password_to_check3)
    
        
    feedback = [] 

    if not has_special_char:
        feedback.append("special characters")
    if not has_upper_char:
        feedback.append("uppercase letters")
    if not has_lower_char:
        feedback.append("lowercase letters")
    if not has_digit_char:
        feedback.append("digits")

    if feedback:  
        return "Your password is unsecure! It lacks " + ", ".join(feedback) + "."

    return ""
# Main Program Logic:
while True:
   password_entered = input("Enter your password for checking: ").strip()
   print()
   print("Also tell us for what are you making a password for?" 
         " For Example: (Online Shopping Account) or (Gmail Account).")
   print()
   specific_reason = input("Tell us so that we can provide a better service to you " 
                          "if you have any, if not no need to say anything: "
                          ).strip().lower()
   print()
   if password_entered:
       is_not_secure = password_checker_step1(password_entered, specific_reason)
       if is_not_secure:
            print("Our password checker stopped at processor: "
                  "'Step 1', Your password is unsecure!")
            print()
            print(is_not_secure)
            break
       else:
            is_not_secure2 = password_checker_step2(password_entered)
            if is_not_secure2:
                print("Our password checker stopped at processor: "
                      "'Step 2', Your password is unsecure!")
                print()
                print(is_not_secure2)
                break
            else:
                is_not_secure3 = password_checker_step3(password_entered)
                if is_not_secure3:
                    print("Our password checker stopped at processor: "
                              "'Step 3', Your password is unsecure!")
                    print()
                    print(is_not_secure3)
                    break
                else:
                    print("Your password passed all 3 verification steps.")
                    print("Your password is secure!")
                    print()
                    try_again = input("Do you want to try again? (y/n): ")
                    if try_again.lower() == "y":
                        clear_screen()
                    elif try_again.lower() == "n":
                        print("Thank you for using our password checker!")
                        break
   else:
        print("\033[31mEmpty input is not allowed! Please try again!\033[0m")
        clear_screen(1)