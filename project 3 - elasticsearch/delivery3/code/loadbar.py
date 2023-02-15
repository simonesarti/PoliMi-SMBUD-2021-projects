import threading
import queue
import functools

class Loadbar:

    def __init__(self, total, prefix='', suffix='', length = 50, fill = '>'):
        self.iteration = 0
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill

    def print_loadbar(self):
        percent = ('{0}/{1}').format(self.iteration, self.total)
        filled_length = int(self.length * self.iteration // self.total)
        bar = self.fill * filled_length + '-' *(self.length-filled_length)
        if self.iteration == self.total:
            print(f'\r{self.prefix} |{bar}| {percent} {self.suffix}\n', end='\r')
        else:
            print(f'\r{self.prefix} |{bar}| {percent} {self.suffix}', end='\r')
            
    def next_and_print(self):
        self.iteration = self.iteration+1
        self.print_loadbar()

def worker(queue_t, process_element, loadbar):
    while not queue_t.empty():
        partecipant = queue_t.get()
        process_element(partecipant)
        queue_t.task_done()
        loadbar.next_and_print()

def build_loadbar(num_elements, title):
    name = title + " Progress:"
    return Loadbar(num_elements, prefix=name, suffix='Complete')

def start_threads(number_of_threads, worker_function, queue_t):
    for i in range(number_of_threads):
        t = threading.Thread(target=worker_function, daemon=True) # daemon means that all threads will exit when the main thread exits
        t.start()

    queue_t.join()

def create_queue(list_of_items):
    queue_t = queue.Queue()
    for item in list_of_items:
        queue_t.put(item)

    return queue_t

def multithread(items, processing_function, num_threads, title=""):
    queue_t = create_queue(items)
    loadbar = build_loadbar(len(items), title)
    worker_func = functools.partial(worker, queue_t=queue_t, process_element = processing_function, loadbar = loadbar)
    start_threads(num_threads, worker_func, queue_t)

