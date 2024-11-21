import re

def assess_password_strength(password):
    length_cri = 0
    uppercase_cri = 0
    lowercase_cri = 0
    number_cri = 0
    special_cri = 0

    if len(password) >= 8:
        length_cri = 1

    if re.search(r'[A-Z]', password):
        uppercase_cri = 1

    if re.search(r'[a-z]', password):
        lowercase_cri = 1

    if re.search(r'\d', password):
        number_cri = 1

    if re.search(r'[@$!%*?&]', password):
        special_cri = 1

    score = length_cri + uppercase_cri + lowercase_cri + number_cri + special_cri

    feedback = ""
    if score < 3:
        feedback = "Weak password. Consider adding more characters, including uppercase letters, numbers, and special characters."
    elif score == 3:
        feedback = "Moderate password. Try adding more special characters and numbers to increase strength."
    elif score == 4:
        feedback = "Strong password, but adding a few more special characters or numbers can make it even better."
    else:
        feedback = "Very strong password! Well done."

    return score, feedback

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength_score, strength_feedback = assess_password_strength(user_password)
    print(f"Password Strength Score: {strength_score}/5")
    print(f"Feedback: {strength_feedback}")
