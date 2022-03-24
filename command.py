import os

address = os.getcwd()
# fr = open(os.path.join(address, 'command.txt'), 'r')
# fw = open(os.path.join(address, 'droneCommand.txt'), 'w')


def returnCommand():
    fr = open(os.path.join(address, 'command.txt'), 'r')
    fw = open(os.path.join(address, 'droneCommand.txt'), 'w')
    file_read_write(fr, fw)
    fr.close()
    fw.close()


def file_read_write(fr, fw):
    while True:
        line = fr.readline()
        if line == '':
            break

        if line.split(" ")[0] == 'controls_repeat_ext':
            repeat(fr, fw, line.split(" ")[1])
        else:
            fw.write(line)


def repeat(fr, fw, num):
    lines = ""
    while True:
        line = fr.readline()
        if line == '.\n':
            break
        lines += line

    for n in range(int(num)):
        fw.write(lines)  # lines+'\n'