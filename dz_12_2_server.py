import socket
import asyncio


async def plus(a, b):
    await asyncio.sleep(0)
    return a + b


async def minus(a, b):
    await asyncio.sleep(0)
    return a - b


async def multiplication(a, b):
    await asyncio.sleep(0)
    return a * b


new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 55000

new_socket.bind((host_name, port))
new_socket.listen(10)
print('Server is running')
conn, add = new_socket.accept()
print('Connected:', add)
while True:
    message = conn.recv(1024)
    message = message.decode()
    print('Client: ', message)

    num = []
    for i in message.split():
        num.append(int(i))

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(plus(num[0], num[1])), ioloop.create_task(minus(num[0], num[1])),
             ioloop.create_task(multiplication(num[0], num[1]))]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)

    answer = f"{str(tasks[0].result())}, {str(tasks[1].result())}, {str(tasks[2].result())}"
    conn.send(answer.encode())
conn.close()
ioloop.close()
