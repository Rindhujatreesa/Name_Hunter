#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#the class EastCoastNames is created with its constructor.
class EastCoastNames:
    def __init__(self):
        #required libraries for the code are imported
        import pandas as pd
        import random
        #the three csv files are extracted and stored in three different pandas dataframes when a class instance is created
        self.male_frame = pd.read_csv('Male_names.csv')
        self.female_frame = pd.read_csv('Female_names.csv')
        self.last_frame = pd.read_csv('Last_names.csv')
    #the function first_name returns the first name as per the passed gender and state arguments
    def first_name(self,gender,state):
        firstname, y = self.random_name(gender,state)
        return firstname
    #the function last_name returns the last name as per the passed gender and state arguments
    def last_name(self,gender,state):
        x,lastname = self.random_name(gender,state)
        return lastname
    #the function full_name returns the first name as per the passed gender and state arguments. It internally calls the previous 
    #two functions and concatenates the first name and last name to form the full name
    def full_name(self,gender,state):
        firstname = self.first_name(gender,state)
        lastname = self.last_name(gender,state)
        return firstname + ' ' + lastname
    #The core function in the EastCoastNames class is random_name. When any of the other three methods are called by a class instant
    #The random_name function is called internally 
    def random_name(self,gender,state):
        import random
        #when both the state and gender are not preferred by the user
        if state == False and gender == False:
            row = random.randint(0,9) #a random integer between 0 and 9(included) is chosen to be the row count, since there are 10 names per state
            column = random.randint(0,10) #a random integer between 0 and 10(included) is chosen to be the column count, since there are 11 states
            file = random.randint(0,1) #a random file from the two csv files (male and female)is also chosen using a random integer
            if file == 1: #if the random method chose 1, then the male_frame dataframe is used to extract a random name
                firstname =self.male_frame.iat[row,column] #a random first name is extracted using the random row,column pair
            else: #this is the case when the random method chose 0
                firstname = self.female_frame.iat[row,column] # a random female name is chosen using the row,column pair
            lastname =self.last_frame.iat[row,column] #the last_name is also chosen from the last_frame randomly
            return firstname,lastname
        #if the gender is given, the below strategy is used
        elif state == False and gender == True:
            row = random.randint(0,9) # the row and column indices are chosen randomly as before
            column = random.randint(0,10)
            #here, the gender is available and is not arbitrary, therefore, we use conditional statement directly and names are chosen as before
            if gender == 'male':
                firstname =self.male_frame.iat[row,column]
            else:
                firstname = self.female_frame.iat[row,column]
            lastname =self.last_frame.iat[row,column]
            return firstname,lastname
        #If the state is given and the gender is not a preference, the following the code block runs
        elif state == True and gender == False:
            row = random.randint(0,9) #the row number is randomly chosen as before
            file = random.randint(0,1) # here, the file has to be chosen randomly, not the state
            if file == 1:
                column =self.male_frame.columns.get_loc(state) #the column index of the state is obtained using the get_loc() method
                firstname =self.male_frame.iat[row,column] #the random row and specific column indices for male are passed to obtain a random frst name
            else:
                column = self.female_frame.columns.get_loc(state) # simialr action is done for a female choice also
                firstname = self.female_frame.iat[row,column]
            lastname =self.last_frame.iat[row,column]
            return firstname,lastname
        else: # this is the case where both the arguments state and gender are passed
            row = random.randint(0,9) # only the row index is chosen randomly to generate a random first name
            if gender == 'male':
                column =self.male_frame.columns.get_loc(state)
                firstname =self.male_frame.iat[row,column]
            else:
                column = self.female_frame.columns.get_loc(state)
                firstname = self.female_frame.iat[row,column]
            row = random.randint(0,9)
            column =self.last_frame.columns.get_loc(state)
            lastname =self.last_frame.iat[row,column]
            return firstname,lastname
#the class terminates and is ready for execution.

