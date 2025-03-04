from collections import deque

class OverworldEventManager:
    def __init__(self):
        self.event_queue = deque()  # Queue for ordered events

    def add_event(self, event_func, *args, **kwargs):
        """Adds an event (function) to the queue."""
        self.event_queue.append((event_func, args, kwargs))

    def run_next_event(self):
        """Runs the next event if available."""
        if self.event_queue:
            event_func, args, kwargs = self.event_queue.popleft()
            event_func(*args, **kwargs)  # Execute the event function

    def run_all_events(self):
        """Runs all events sequentially until queue is empty."""
        while self.event_queue:
            self.run_next_event()