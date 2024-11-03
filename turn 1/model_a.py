import threading
import time
import random


class SharedResource:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        with self.lock:
            self.value += 1


class WorkerThread(threading.Thread):
    def __init__(self, name, resource, delay):
        super().__init__(name=name)
        self.resource = resource
        self.delay = delay

    def run(self):
        while True:
            time.sleep(self.delay)
            self.resource.increment()


def simulate_thread_starvation():
    resource = SharedResource()

    threads = []
    for i in range(5):
        delay = random.uniform(0.01, 0.1)  # Simulate varying delays
        thread = WorkerThread(f"Worker-{i}", resource, delay)
        thread.start()
        threads.append(thread)

    # Main thread keeps accessing the resource frequently
    while True:
        time.sleep(0.001)
        resource.increment()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    simulate_thread_starvation()
