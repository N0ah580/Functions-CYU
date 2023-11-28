# Programmer: Noah
# Description: Grade

def convert_grade (grade):
    
    if grade > 100:
        return ("Invalid percent!")
    
    elif grade >= 80:
        return ("A")
    
    elif grade >= 70:
        return ("B")
    
    elif grade >= 60:
        return ("C")
    
    elif grade >= 50:
        return ("D")
    
    elif grade >= 0:
        return ("F")
    
    else:
        return ("Invalid percent!")