for trail in range(3):
    email=input("please enter an email:")
    try:
        if "@" not in email or "." not in email:
            
            raise ValueError(" email should contin '@'and '.'") 
        else :
            parts=email.split('@')
            if len(parts) != 2 :
                
                raise ValueError("invalid email")
            else :
                domain=parts[1]
                if '.' in domain :
                    # raise ValueError("invalid domain")
                    print("email is valid")
                    break
                else:
                    raise ValueError("invalid email")
    except ValueError:
        print("error")
else:
    print("email is unvalid")