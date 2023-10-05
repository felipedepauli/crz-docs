from multiprocessing import Process
from time import sleep

def msg(diga_a_mensagem, max):
    count = 0
    while count < max:
        count += 1
        print(f'{__name__}: {diga_a_mensagem}')
        sleep(0.7)

if __name__ == '__main__':
    print("Tamo começando esta parada...")

    msg01 = Process(target=msg, args=("slk", 5))
    msg01.start()

    msg02 = Process(target=msg, args=("tamo na área", 2))
    msg02.start()

    print("E agora acabou.")