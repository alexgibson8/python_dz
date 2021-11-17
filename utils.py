def currency_translate():
    from requests import get
    import datetime
    value = str(input('Введите код валюты: '))
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    if value not in content:
        result = None
        return result
    else:
        for el in content.split(f'{value}')[1:]:
            for el_1 in el.split('</Value>')[:1]:
                result_val = round(float(el_1.split('<Value>')[1].replace(',', '.')), 2)
        for el in content.split('Date="')[1:]:
            for el_1 in el.split('" name')[:1]:
                temp = str(el_1)
                temp_date = datetime.datetime.strptime(temp, '%d.%m.%Y')
                result_date = temp_date.date()
        return f'Курс валюты {result_val} руб. Дата: {result_date}'