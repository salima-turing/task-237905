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
    def __init__(self, resource):
        super().__init__()
        self.resource = resource
        self.hunger_threshold = 0.5  # Simulate hunger threshold

    def run(self):
        while True:
            if random.random() < self.hunger_threshold:
                # Simulate thread starvation by introducing a delay
                time.sleep(0.1)
            else:
                self.resource.increment()

def main():
    resource = SharedResource()
    num_threads = 10
    threads = []

    # Create worker threads
    for _ in range(num_threads):
        thread = WorkerThread(resource)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print(f"Final value of the shared resource: {resource.value}")

if __name__ == "__main__":
    main()
