import re

def main1():
    # Option 1 : All criteria are checked by RegEx
    log_file = open('access_log_Jul95.txt', 'r')
    for each_log in log_file:
        #wanted_log = re.findall(r'(\d{4}:(03:22:(3[3-9]|[45][0-9])|(03:2[3-9]:\d{2})|(03:[3-5][0-9]:\d{2})|((0[4-5]):\d{2}:\d{2})|(06:0[0-8]:\d{2}))).*\.(gif|jpg|jpeg|mpg).*(\b4[0-9][0-9]\b|\b5[0-5][0-9])\b\s\S', each_log)
        attr_time = re.search(r'(?P<time>(03:22:(3[3-9]|[45][0-9])|(03:2[3-9]:\d{2})|(03:[3-5][0-9]:\d{2})|((0[4-5]):\d{2}:\d{2})|(06:0[0-8]:\d{2})))', each_log)
        attr_ext = re.search (r'(?P<ext>\.(gif|jpg|jpeg|mpg))', each_log)
        attr_code = re.search(r'(?P<code> 4[0-9][0-9] | 5[0-5][0-9] )', each_log)

        if (attr_time is None) | (attr_code is  None) | (attr_ext is  None):
            continue
        else:
            print(each_log)        
    print ('Done')
           

def main2():
    # Option 2 : Human-like version )
    log_file = open('access_log_Jul95.txt', 'r')
    for each_log in log_file:
        attr_time = re.search(r'(?P<time>(\d{2}:\d{2}:\d{2} ))', each_log)
        attr_ext = re.search (r'(?P<ext>\.(gif|jpg|jpeg|mpg))', each_log)
        attr_code = re.search(r'(?P<code> 4[0-9][0-9] | 5[0-5][0-9] )', each_log)

        if (attr_time is None) | (attr_code is  None) | (attr_ext is  None):
            continue
        else:
            if (attr_time.group('time')>='03:22:33') and (attr_time.group('time')<='06:08:59'):
                print(each_log)        
    print ('Done')
           


if __name__ == "__main__":
    main2()


# extansion and code:      \.(gif|jpg|jpeg|mpg).*(\b4[0-9][0-9]\b|\b5[0-5][0-9])\b\s-
# time:    (\d{4}:(03:22:(3[3-9]|[45][0-9])|(03:2[3-9]:\d{2})|(03:[3-5][0-9]:\d{2})|((0[4-5]):\d{2}:\d{2})|(06:0[0-8]:\d{2})))
