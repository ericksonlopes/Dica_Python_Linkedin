from validate_email import validate_email

print(validate_email('exemple@gmail.com'))
# True

print(validate_email('exemple@.com'))
# False