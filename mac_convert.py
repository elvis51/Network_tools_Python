while True :
    mac_income = input('enter mac address: ')
    mac_income_no_symbols = mac_income.translate({ord(c): "" for c in " !@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    #print(mac_income_no_symbols)
    #print(len(mac_income_no_symbols))
    if 12 == len(mac_income_no_symbols) :
        mac_with = ':'.join(mac_income_no_symbols[i:i + 2] for i in range(0, len(mac_income_no_symbols), 2))
        print(mac_with.lower())
        mac_with1 = '.'.join(mac_income_no_symbols[i:i + 4] for i in range(0, len(mac_income_no_symbols), 4))
        print(mac_with1.lower())
        mac_with2 = '-'.join(mac_income_no_symbols[i:i + 2] for i in range(0, len(mac_income_no_symbols), 2))
        print(mac_with2.lower())
        print(mac_with2.upper())
        print(mac_with.upper())
    else:
        print("(" + mac_income + ") MAC address invalid please try again")
