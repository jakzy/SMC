import AppClass
import time

counter = 0
System = dict()

_time = open('SMC_time_test.txt', 'w')
#_data = open(r'C:\Users\1\PycharmProjects\my_first_project\test.txt', 'r')
_data = open('test.txt', 'r')
_analyze = open('SMC_analyze_test.txt', 'w')
start_time = time.perf_counter()
machine = AppClass.AppClass()
for line in _data:
    match = machine.CheckString(line.split('\n')[0])
    if match:
        counter += 1
        _analyze.write('+ ' + line)
        server = line[2:line.find('\\', 2)]
        if server in System:
            System[server] += 1
        else:
            System[server] = 1
    else:
        _analyze.write('- ' + line)

_time.write('Result time: ' + str(time.perf_counter() - start_time))
_time.close()
_result = open('SMC_servers_test.txt', 'w')
for i in System:
    _result.write(i + '\t' + str(System[i]) + '\n')
_analyze.close()
_data.close()
_result.close()