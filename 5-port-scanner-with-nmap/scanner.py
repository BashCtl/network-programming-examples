# nmap should be installed https://nmap.org/download
import nmap


start_port = 20
end_port = 30
target = '127.0.0.1'
scanner = nmap.PortScanner()

print('Start scaning...')
for port in range(start_port, end_port + 1):
    res = scanner.scan(target, str(port))
    res = res['scan'][target]['tcp'][port]['state']
    print(f'Port {port} is {res}')
