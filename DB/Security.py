import bcrypt

"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""

class Password:
    def __init__(self):
        import bcrypt

        # Generate a salt
        salt = bcrypt.gensalt()

        # Hash a password using the salt
        password = b"my_password"
        hashed_password = bcrypt.hashpw(password, salt)

        # Check if a password matches a hashed password
        input_password = b"my_password"
        if bcrypt.checkpw(input_password, hashed_password):
            print("Passwords match!")
        else:
            print("Passwords do not match.")

    def _hash_password(self):
        hashed_password = bcrypt.hashpw(password, salt)
        pass




    def is_password_valid(self, password):
        return_value = False
        input_password = password.encode('utf-8')
        if bcrypt.checkpw(input_password, hashed_password):
            print("Passwords match!")
        else:
            print("Passwords do not match.")

        return return_value