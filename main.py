import whois11
import os


print('''
enter domains to query whois information from
(ex' yahoo.com )
this information will be stored in a *whois-info.txt
file in the whois directory.

enter the 'finish' keyword to end process:
''')
finish = False
while not finish:
    domain_to_check = input('>> ')
    if domain_to_check == 'finish':
        break
    try:
        info = whois11.whois(domain_to_check)
        if info is not None:
            f = open(f'whois/{domain_to_check}.whois-info.txt', 'w')
            f.write(whois11.whois(domain_to_check))
            print(fr'info added to \whois\{domain_to_check}.whois-info.txt')
    except Exception as ex:
        print('''
                        -----------------------
                                  BAD
                                  URL 
                        ------------------------ 

    ''', ex)
