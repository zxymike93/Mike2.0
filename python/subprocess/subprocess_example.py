import subprocess


# # 最基本用法
s = subprocess.run(['ls', '-l'])
# s = subprocess.call(['pwd'])
# s = subprocess.run('echo $HOME', shell=True)
# print(s.returncode)
#
# # check 参数检查返回的 exit code 并在错误时 raise 错误
# # 相当与 check_call()
# try:
#     # subprocess.run(['false'], check=True)
#     subprocess.check_call(['ls'])
# except subprocess.CalledProcessError as e:
#     print(e)
#
# 输出结果要传到 stdout 才能存储起来
# 否则 s == -1
# s = subprocess.run(['ls'], stdout=subprocess.PIPE)
# print(len(s.stdout))
# print(s.stdout)
# print(subprocess.PIPE)
#
# 丢弃
# try:
#     s = subprocess.run(
#         'false',
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.DEVNULL
#     )
# except subprocess.CalledProcessError as e:
#     print('Error: {}'.format(e))
# else:
#     print('stdout: {}'.format(s.stdout))
#     print('stderr: {}'.format(s.stderr))
#
# # Popen 类
# # read
# s = subprocess.Popen(
#     ['echo', '"to stdout"'],
#     stdout=subprocess.PIPE,
# )
# stdout_value = s.communicate()
# print(stdout_value)
# # write
# s = subprocess.Popen(
#     ['echo', '"to stdout"'],
#     stdin=subprocess.PIPE,
# )
# s.communicate('to stdin\n'.encode('utf-8'))
#
# # Unix 管道重定向
ls = subprocess.Popen(
    ['ls', '-lhF'],
    stdout=subprocess.PIPE
)
grep = subprocess.Popen(
    ['grep', 'howto'],
    stdin=ls.stdout,
    stdout=subprocess.PIPE
)
# print(grep.stdout.read())
for line in grep.stdout:
    print(line.decode('utf-8').strip())
