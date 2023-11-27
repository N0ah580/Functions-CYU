# Programmer: Noah
# Description: Grade

def convert_grade (grade):
    
    if grade > 80:
        return ("A")
    
    elif grade > 70:
        return ("B")
    
    elif grade > 60:
        return ("C")
    
    elif grade > 50:
        return ("D")
    
    elif grade < 50:
        return ("F")
    
    else:
        return ("Invalid percent!")