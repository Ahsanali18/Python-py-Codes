#Write a python program in which you have to set a logic like:

has_high_income=True    
has_good_income=False

                    # and Operator 
#If applicant has high income and good credit Eligible for loan.
if has_high_income and has_good_income:
    print("Eligible for loan.")

                    #or Operator
#If applicant has low  income or  good credit Eligible for loan.
if has_high_income or has_good_income:
    print("Eligible for loan?")

                    #not operator
if has_high_income and not has_good_income:
    print("Eligible for loan.....")
