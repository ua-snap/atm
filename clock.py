import datetime, time
from matplotlib.dates import date2num
from matplotlib.dates import num2date

def start(self):
    self.start = time.time()
    self.start_time = time.asctime( time.localtime(time.time()) )
    self.archive_time = time.strftime("%Y_%m.%d_%H%M")

def finish(self):
    self.finish = time.time()
    self.finish_time = time.asctime( time.localtime(time.time()) )
