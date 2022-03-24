import socket
from time import sleep
from tello import Tello
from datetime import datetime
import time


if __name__ == "__main__":
    local_ip = ''
    local_port = 8890 ## read port
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
    socket.bind((local_ip, local_port))

    tello_ip = '192.168.10.1'
    tello_port = 8889 ## write port
    tello_adderss = (tello_ip, tello_port)

    socket.sendto('command'.encode('utf-8'), tello_adderss) ## Enter SDK Mode

    # try:
    #     index = 0
    #     while True:
    #         outStr=""
    #         response, ip = socket.recvfrom(1024)
    #         if response == 'ok':
    #             start_time = str(datetime.now())
    #             file_name = "command.txt"
    #             f = open(file_name, "r")
    #             commands = f.readlines()
    #             print(commands)
    #             tello = Tello()
    #
    #             for command in commands:
    #                 if command != '' and command != '\n':
    #                     command = command.rstrip()
    #                     if command.find('delay') != -1:
    #                         sec = float(command.partition('delay')[2])
    #                         print('delay %s' % sec)
    #                         time.sleep(sec)
    #                         pass
    #                     else:
    #                         tello.send_command(command)
    #
    #             log = tello.get_log()
    #             outFile = open('log.txt', 'w+')
    #             for stat in log:
    #                 stat.print_stats()
    #                 str = stat.return_stats()
    #                 outFile.write(str)
    #
    #             continue
    #         outStr = 'Tello State:' + str(response)
    #         print(outStr)
    #         sleep(0.2)
    # except KeyboardInterrupt:
    #     pass


start_time = str(datetime.now())
file_name = "command.txt"
f = open(file_name, "r")
commands = f.readlines()
print(commands)
tello = Tello()

for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()
        if command.find('delay') != -1:
            sec = float(command.partition()[2])
            print('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

log = tello.get_log()
outFile = open('log.txt', 'w+')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    outFile.write(str)









# from tello import Tello
# import sys
# from datetime import datetime
# import time
#
# start_time = str(datetime.now())
#
# file_name = sys.argv[1]
#
# f = open(file_name, "r")
# commands = f.readlines()
#
# tello = Tello()
# for command in commands:
#     if command != '' and command != '\n':
#         command = command.rstrip()
#
#         if command.find('delay') != -1:
#             sec = float(command.partition('delay')[2])
#             print 'delay %s' % sec
#             time.sleep(sec)
#             pass
#         else:
#             tello.send_command(command)
#
# log = tello.get_log()
#
# out = open('log/' + start_time + '.txt', 'w')
# for stat in log:
#     stat.print_stats()
#     str = stat.return_stats()
#     out.write(str)
