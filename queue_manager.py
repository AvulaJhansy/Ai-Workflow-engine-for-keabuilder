from queue import Queue

request_queue = Queue()


def add_request(request):
    request_queue.put(request)


def process_requests():
    processed = []

    while not request_queue.empty():
        processed.append(request_queue.get())

    return processed