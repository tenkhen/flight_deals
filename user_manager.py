class UserManager:
    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.email = ''
        self.verify = ''
    def get_user_info(self):
        print("Welcome to Khenrab's Flight Club \nWe find the best flight deals and email you.\n")
        self.firstname = input('What is your first name?\n').title()
        self.lastname = input('What is your last name?\n').title()
        self.email = input('What is your email?\n')
        self.verify = input('Type your email again.\n')
        while self.email != self.verify:
            print("Your email didn't match!")
            self.verify = input('Type your email again.\n')
        print("You're in the club!")