import urllib.request
import re

with urllib.request.urlopen('https://mkwrs.com/mk8dx/') as res:
    data = res.read().decode('utf-8').split('\n')
    course = []
    time = []
    for line in data:
        m = re.search(r'display\.php[^>]*>([^<]+)', line)
        if m is not None:
            c = m.group(1)
            if c != '200cc':
                if len(course) == 0:
                    course.append(c)
                elif course[-1] != c:
                    course.append(c)
        m = re.search(r'\d\'\d{2}\"\d{3}', line)
        if m is not None:
            t = m.group(0)
            if len(time) == 0:
                time.append(t)
            elif time[-1] != t:
                time.append(t)
    time = time[:-3][::2]
    assert len(course) == len(time)

with open('mk8dxwr.txt', 'w') as f:
    for i in range(len(course)):
        f.write('{}: {}\n'.format(course[i], time[i]))
