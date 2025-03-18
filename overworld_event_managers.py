from collections import deque

class OverworldEventManager:
    def __init__(self,map_input_lock):
        self.event_queue = deque()
        self.map_input_lock=map_input_lock

    def add_event(self, event_func, args=[], kwargs={},persistent_condition=None):
        """Adds an event to the queue. If persistent_condition is provided, it persists."""
        self.event_queue.append((event_func, args, kwargs, persistent_condition))

    def run_next_event(self):
        """Runs the next event if available, blocking further events if persistent."""
        if self.event_queue:
            event_func, args, kwargs, persistent_condition = self.event_queue.popleft()
            event_func(*args, **kwargs)
            if persistent_condition and persistent_condition():
                self.event_queue.appendleft((event_func, args, kwargs, persistent_condition))
