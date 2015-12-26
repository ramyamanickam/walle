from subprocess import Popen, PIPE, STDOUT
p = Popen(['myapp'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
stdout_data = p.communicate(input='data_to_write')[0]
