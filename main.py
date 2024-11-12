

def ces1():
    a = [1, 2, 3, 4, 5]
    for i in a:
        if i == 3:
            continue
        if i == 4:
            print(f'当前参数：{i}')
        print(i)

if __name__ == '__main__':
    ces1()
