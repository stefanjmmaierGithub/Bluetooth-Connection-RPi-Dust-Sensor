# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:54:08 2015

@author: stefan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:33:25 2015
"""

import numpy as np
import time
import datetime

class RingBuffer_string(object):
    def __init__(self, size_max, default_value='', dtype='|S25'):
        """initialization"""
        self.size_max = size_max

        self._data = np.empty(size_max, dtype=dtype)
        self._data.fill(default_value)

        self.size = 0

    def append(self, value):
        """append an element"""
        self._data = np.roll(self._data, 1)
        self._data[0] = value 

        self.size += 1

        if self.size == self.size_max:
            self.__class__  = RingBufferFull

    def get_all(self):
        """return a list of elements from the oldest to the newest"""
        return(self._data)

    def get_partial(self):
        return(self.get_all()[0:self.size])

    def __getitem__(self, key):
        """get element"""
        return(self._data[key])

    def __repr__(self):
        """return string representation"""
        s = self._data.__repr__()
        s = s + '\t' + str(self.size)
        s = s + '\t' + self.get_all()[::-1].__repr__()
        s = s + '\t' + self.get_partial()[::-1].__repr__()
        return(s)

    def __reset__(self):
        default_value=''
        self._data.fill(default_value)

class RingBufferFull(RingBuffer_string):
    def append(self, value):
        """append an element when buffer is full"""
        self._data = np.roll(self._data, 1)
        self._data[0] = value


"""
#def ringbuff_numpy_test():
ringlen = 10
ringbuff = RingBuffer_string(ringlen)
for i in range(40):    
        x = np.datetime64(datetime.datetime.now())
        ringbuff.append(x) # write

print("Get RingbuffValue: ",ringbuff.get_all())

print("Get Ringbuff Item: ",ringbuff.__getitem__(4))



import numpy as np
import datetime

current = np.datetime64(datetime.datetime.now())
current
"""








"""
import numpy as np
import time
import datetime
from dateutil import tz
ts = time.time()   
dt = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
x = str(dt)




ts = time.time()   
dt = datetime.datetime.fromtimestamp(ts).replace(tzinfo=tz.tzutc())
x = np.array(np.datetime64(dt.isoformat()))
x

import time
ts = time.time() 
ts
import datetime
datetime.datetime.utcnow()
x = str(datetime.datetime.now())
x
"""