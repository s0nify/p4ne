import glob

ips = {}
count = 0
for i in glob.glob("/Users/sonify/PycharmProjects/config_files/*.txt"):
    with open(i) as file:
        for line in file:
            if 'ip address ' in line:
                ipmask = line.replace(" ip address ", "").replace("\n", "", 1).split(' ')
                try:
                    if len(ipmask[0]) != 0 or len(ipmask[1]) !=0:
                        ipaddr = ipmask[0]
                        mask = ipmask[1]

                        ips[count] = {ipaddr: mask}
                        count += 1
                except:
                    pass

print("Всего значений: " + str(count))

print(ips)
