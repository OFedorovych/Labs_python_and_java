import re

def main():

    log_file = open('access_log_Jul95.txt', 'r')

    for each_log in log_file:
        wanted_log = re.findall(r'(\d{4}:(03:22:(3[3-9]|[45][0-9])|(03:2[3-9]:\d{2})|(03:[3-5][0-9]:\d{2})|((0[4-5]):\d{2}:\d{2})|(06:0[0-8]:\d{2}))).*\.(gif|jpg|jpeg|mpg).*(\b4[0-9][0-9]\b|\b5[0-5][0-9])\b\s\S', each_log)
        
        if len(wanted_log) == 0:
            continue
        else:
            print(each_log)
            wanted_log.clear()


           
    

if __name__ == "__main__":
    main()


# extansion and code:      \.(gif|jpg|jpeg|mpg).*(\b4[0-9][0-9]\b|\b5[0-5][0-9])\b\s-

# time:    (\d{4}:(03:22:(3[3-9]|[45][0-9])|(03:2[3-9]:\d{2})|(03:[3-5][0-9]:\d{2})|((0[4-5]):\d{2}:\d{2})|(06:0[0-8]:\d{2})))