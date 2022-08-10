email = input("Enter Email address: ").strip()

#slice out the user name
user_name = email[:email.index("@")] #www.xyz

#slice the domain name
domain_name = email[email.index("@")+1:] #gmail.com

#format message
output = "Username is '{}' and domain is '{}'".format(user_name,domain_name)

#display output message
print(output)