import time

class Debug(object):
    def __init__(self, output = print):
        self.debug_start_time = self.debug_time = time.time()        
        self.output = output
        self.log = []

    def trace(self, message = None, trace_type = 'Trace'):
        if message is None:
            message = ''
        time_step = time.time() - self.debug_time
        time_total = time.time() - self.debug_start_time
        message = '[%s] [Time %.2f / %.2f sec] %s' % (trace_type, time_step, time_total, message)
        self.debug_time = time.time()
        self.output(message)
        self.log.append(message)
        self.save_log()
        
    def save_log(self):
        with open(f'.\log\log.txt', 'w', encoding='utf-8') as outfile:
            for item in self.log:
                outfile.write(f'{item}\n')
