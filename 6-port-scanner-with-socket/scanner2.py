from socket import *
import time

starttime = time.time()


if __name__ == '__main__':
    target = input('Enter host for scanning: ')
    target_ip = gethostbyname(target)
    print(f'Starting scanning on host: ', target_ip)
    for port in range(20, 500):
        s = socket(AF_INET, SOCK_STREAM)
        conn=s.connect_ex((target_ip, port))
        if conn == 0:
            print(f'Port {port}: OPEN')
        s.close()

print('Time taken: ', time.time() - starttime)