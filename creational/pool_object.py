'''
The provided example illustrates the use of the Object Pool design pattern in a scenario involving 
the management and reuse of worker objects for processing requests in a web server application.

Here's a breakdown of the components and their roles in the example:

1. **`Worker` Class**:
   - Represents worker objects that can process requests.
   - The `process()` method simulates the processing of a request.

2. **`HTTPRequest` Class**:
   - Represents a model of an HTTP request.

3. **`WorkerPool` Class**:
   - Serves as the object pool, managing the worker objects.
   - Manages a collection of worker objects, both available (idle) and busy (processing requests).
   - Provides methods to acquire a worker from the pool (`get_worker()`) and release it back to the
    pool after processing (`release_worker()`).

In this scenario, the Object Pool pattern is used to efficiently manage worker objects that 
are used to process incoming HTTP requests in a web server. Instead of creating a new worker for 
each request and incurring the overhead of object creation and destruction, the Object Pool maintains
a set of pre-allocated worker objects. These workers can be reused for processing multiple requests,
improving performance and resource utilization.

The benefits of using the Object Pool pattern in this example include:

- Reducing the overhead of object creation and destruction, which can be resource-intensive.
- Enhancing performance by reusing existing objects, thus avoiding unnecessary memory allocation and deallocation.
- Managing the maximum number of workers, preventing resource exhaustion in scenarios with high demand.

In the provided example, the client code demonstrates how the `WorkerPool` can be used to manage
the worker objects. It acquires a worker from the pool, simulates processing an HTTP request,
and then releases the worker back to the pool. If all workers are busy, the pool prevents further 
requests from being processed, preventing potential resource exhaustion.

Overall, the Object Pool pattern helps optimize resource usage and improve the efficiency of
processing tasks that involve the creation and reuse of objects, such as managing worker threads 
in a web server.
'''
class Worker:
    def process(self, request):
        pass


class HTTPRequest:
    def __init__(self, data):
        self.data = data


class WorkerPool:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.available_workers = []
        self.busy_workers = []

    def get_worker(self):
        if not self.available_workers:
            if len(self.busy_workers) < self.max_workers:
                worker = Worker()
                self.busy_workers.append(worker)
                return worker
            else:
                raise Exception('No available workers')
        else:
            worker = self.available_workers.pop()
            self.busy_workers.append(worker)
            return worker
        
    def release_worker(self, worker):
        self.busy_workers.remove(worker)
        self.available_workers.append(worker)


pool = WorkerPool(max_workers=5)

try:
    worker = pool.get_worker()
    request = HTTPRequest("GET /api/data")
    worker.process(request)
    pool.release_worker(worker)
except Exception as e:
    print(e)
