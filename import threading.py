import threading
import multiprocessing

class Pasaload:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()  # Mutual exclusion lock

    def pasaload(self, amount, cellphone_number):
        with self.lock:
            if self.balance >= amount:
                print(f"Transferring {amount} pesos to {cellphone_number}...")
                self.balance -= amount
                print(f"New balance: {self.balance}")
            else:
                print("Insufficient funds!")

def pasaload_thread(pasaload, amount, cellphone_number):
    pasaload.pasaload(amount, cellphone_number)

def pasaload_process(pasaload, amount, cellphone_number):
    pasaload.pasaload(amount, cellphone_number)

if __name__ == "__main__":
    balance = int(input("Enter the current amount of your balance: "))
    pasaload = Pasaload(balance=balance)

    amount = int(input("Enter the amount to transfer: "))
    cellphone_number = input("Enter the cellphone number to transfer to: ")

    threads = []
    processes = []

    # Using threads
    for i in range(5):
        t = threading.Thread(target=pasaload_thread, args=(pasaload, amount, cellphone_number))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Using processes
    for i in range(5):
        p = multiprocessing.Process(target=pasaload_process, args=(pasaload, amount, cellphone_number))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
