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
        else:
            self.map_input_lock.unlock()

    '''
    #no longer useful, since it processes the same key input for all
    #functions, instead of checking separate inputs for each call.
    #Might be useful for debugging, though.

    def run_all_events(self):
        """Runs all events, but stops if a persistent event remains active."""
        while self.event_queue:
            previous_size = len(self.event_queue)
            self.run_next_event()
            
            # If the queue size didn’t change, a persistent event is blocking execution
            if len(self.event_queue) == previous_size:
                break
        
        if not self.event_queue:
            self.map_input_lock.unlock()'''