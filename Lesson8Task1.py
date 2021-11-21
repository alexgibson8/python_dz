import re


def email_parse(email):
    address = re.compile(r'(?P<username>\w+)@(?P<domen>\w+[.]\w+)')
    if not address.match(email):
        raise ValueError(f'wrong email: {email}')
    else:
        final_address = re.finditer(address, email)
        for i in final_address:
            print(i.groupdict())


email_parse('aleksand21k@mail.ru')
email_parse('aleksand21k@mailru')
email_parse('aleksand21kmail.ru')
