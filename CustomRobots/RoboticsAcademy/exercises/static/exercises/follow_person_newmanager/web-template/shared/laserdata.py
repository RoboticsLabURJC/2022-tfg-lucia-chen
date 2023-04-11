import numpy as np
import mmap
from posix_ipc import Semaphore, O_CREX, ExistentialError, O_CREAT, SharedMemory, unlink_shared_memory
from ctypes import sizeof, memmove, addressof, create_string_buffer, c_float
import struct

class SharedLaserData:
    def __init__(self, name):
        # Initialize varaibles for memory regions and buffers and Semaphore
        self.shm_buf = None; self.shm_region = None
        self.values_lock = None

        self.shm_name = name; 
        self.values_lock_name = name

        # Initialize shared memory buffer
        try:
            self.shm_region = SharedMemory(self.shm_name)
            self.shm_buf = mmap.mmap(self.shm_region.fd, sizeof(c_float)*180)
            self.shm_region.close_fd()
        except ExistentialError:
            self.shm_region = SharedMemory(self.shm_name, O_CREAT, size=sizeof(c_float)*180)
            self.shm_buf = mmap.mmap(self.shm_region.fd, self.shm_region.size)
            self.shm_region.close_fd()

        # Initialize or retreive Semaphore
        try:
            self.values_lock = Semaphore(self.values_lock_name, O_CREX)
        except ExistentialError:
            values_lock = Semaphore(self.values_lock_name, O_CREAT)
            values_lock.unlink()
            self.values_lock = Semaphore(self.values_lock_name, O_CREX)

        self.values_lock.release()

    # Get the shared value
    def get(self):
        # Retreive the data from buffer
        self.values_lock.acquire()
        values = struct.unpack('f', self.shm_buf)
        self.values_lock.release()

        return values

    # Add the shared value
    def add(self, values):
        # Send the data to shared regions
        self.values_lock.acquire()
        self.shm_buf[:] = struct.pack('f', values)
        self.values_lock.release()

    # Destructor function to unlink and disconnect
    def close(self):
        self.values_lock.acquire()
        self.shm_buf.close()

        try:
            unlink_shared_memory(self.shm_name)
        except ExistentialError:
            pass

        self.values_lock.release()
        self.values_lock.close()
