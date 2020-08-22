import fetch_records

def to_sec(s):
    return int(s[0]) * 60 + int(s[2:4]) + int(s[5:]) / 1000

wr_data = []
my_data = []

with open('mk8dxwr.txt', 'r') as f:
    for line in f.read().split('\n'):
        wr_data.append(line.split(': '))

with open('record.txt', 'r') as f:
    for line in f.read().split('\n'):
        my_data.append(line.split(': '))

data = []

for i in range(48):
    assert wr_data[i][0] == my_data[i][0]
    data.append((wr_data[i][0], to_sec(wr_data[i][1]), to_sec(my_data[i][1])))

def to_str(sec):
    sec = int(sec * 1000)
    return '{}\'{}"{}'.format(sec // 1000 // 60, sec // 1000 % 60, sec % 1000)

def make_markdown_table(data):
    ret = '|コース名|自己記録|WRとの差|\n'
    ret += '|--|--|--|\n'
    for t in data:
        ret += '|{}|{}|{:.3f}|\n'.format(t[0], to_str(t[1]), t[1] - t[2])
    return ret

def format_summary(data):
    data = sorted(data, key = lambda x: x[2] - x[1])
    ret = '# TA記録（6秒落ち以内）\n\n'
    ret += make_markdown_table(filter(lambda x: x[2] - x[1] <= 6, data))
    return ret

def format_all(data):
    data = sorted(data, key = lambda x: x[2] - x[1])
    ret = '# 全コース記録\n\n'
    ret += make_markdown_table(data)
    return ret

with open('README.md', 'w') as f:
    f.write(format_summary(data))
    f.write('\n')
    f.write('[全記録](https://github.com/xuzijian629/xuzijian629/blob/master/ALL.md)')

with open('ALL.md', 'w') as f:
    f.write(format_all(data))
