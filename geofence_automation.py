import os as o
import time
import subprocess

o.chdir('/home/kartikey/loca')
print("in directory")
p = o.listdir()
i = 0.00
for file in p :
    k = (o.path.getmtime(file))


    print(str(file) + "  mod time is " + str(k))
    if k > i:
        f = file
        i = k
print("latest file is :- " + str(f))
print("modified at " + time.ctime(i))
while True:
    o.chdir('/home/kartikey/loca')
    time.sleep(10)
    p1 = o.listdir()
    h = 0.00
    for file in p1:
        k1 = (o.path.getmtime(file))
        if k1 > h:
            f1 = file
            h = k1

    if h != i:
        print("new file " + str(f1))
        i = h
        pwd = '123456'
        cmd = 'ps -a'
        t = []

        p = subprocess.call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
         # print(p)
        data = subprocess.Popen(['ps', '-a'], stdout=subprocess.PIPE)
        # print(data)

        output = data.communicate()
        # print((output))
        j = output[0].split()
        kr = 0
        for i4 in j:
            if ("mavproxy" in str(i4)):
                p = j[kr - 2]
            kr += 1
        p1 = p.decode('UTF-8')
        print(p1)
        file_path = o.path.abspath(f1)

        sudoPassword = '123456'  # password
        o.chdir('/home/kartikey') #to run ttyecho
        command = ' sudo ./ttyecho -n /dev/' + str(p1) + ' fence load ' + str(file_path)
        print(command)

        p = o.system('echo %s|sudo -S %s' % (sudoPassword, command))


