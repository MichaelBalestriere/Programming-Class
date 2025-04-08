import re
import getpass # To hide password input

def check_password_strength(password):
    """
    Analyzes the strength of a given password based on common criteria.

    Args:
        password (str): The password string to analyze.

    Returns:
        str: A string indicating the password strength level.
    """
    strength_score = 0
    feedback = []

    # --- Criteria ---
    # 1. Length (score +1 for >= 8, +1 for >= 12)
    length = len(password)
    if length >= 12:
        strength_score += 2
        feedback.append("Good length (12+ characters).")
    elif length >= 8:
        strength_score += 1
        feedback.append("Minimum length (8+ characters) met.")
    else:
        feedback.append(f"Too short (needs at least 8 characters, currently {length}).")

    # 2. Uppercase Letters (score +1)
    if re.search(r"[A-Z]", password):
        strength_score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Missing uppercase letters (A-Z).")

    # 3. Lowercase Letters (score +1)
    if re.search(r"[a-z]", password):
        strength_score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Missing lowercase letters (a-z).")

    # 4. Numbers (score +1)
    if re.search(r"\d", password): # \d is equivalent to [0-9]
        strength_score += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("Missing numbers (0-9).")

    # 5. Special Characters (score +1)
    # You can customize the list of special characters
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?~`]", password):
        strength_score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Missing special characters (e.g., !@#$%).")

    # --- Determine Strength Level ---
    if strength_score <= 1:
        level = "Very Weak"
    elif strength_score == 2:
        level = "Weak"
    elif strength_score == 3:
        level = "Moderate"
    elif strength_score == 4:
        level = "Strong"
    else: # score == 5 or 6
        level = "Very Strong"

    # --- Return Result ---
    print("\n--- Password Analysis ---")
    for item in feedback:
        print(f"- {item}")
    print("-------------------------")
    return f"Overall Strength: {level} (Score: {strength_score}/6)"

# --- Main Execution ---
if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    # Use getpass to hide the password as the user types it
    # Note: getpass might not work well in all IDEs/terminals (like simple web-based ones)
    # If it causes issues, you can replace it with: user_password = input("Enter the password to check: ")
    try:
        user_password = getpass.getpass("Enter the password to check: ")
    except Exception as e:
        print(f"\nWarning: Could not use getpass for hidden input ({e}). Falling back to standard input.")
        user_password = input("Enter the password to check: ")


    if not user_password:
        print("No password entered. Exiting.")
    else:
        result = check_password_strength(user_password)
        print(result)
