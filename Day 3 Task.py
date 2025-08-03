#name:mayar muhammad elsayed muhmmad
data=["mayar@gmail.com","arwa@yahoo.com","noha33hotmail.com","ahmad3@hotmail.com","omar12@gmailcom","kareem5.com@gamil"]
validemails=[]

for email in data:
    if '@' in email:
        part = email.split('@',1)
        domain=part[1]
        
        if '.' in domain:
         validemails.append(email)

print (validemails)

domains = list(map(lambda email: email.split('@',1)[1],validemails))
print(domains)
