'''
Problem:

The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
     The read function will only be called once for each test case.

Similar Problems:
     (E) 157. Read N Characters Given Read4
     (H) 158. Read N Characters Given Read4 II - Call multiple times
'''

# Read single time

# The read4K API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
            :type buf: Destination buffer (List[str])
            :type n: Maximum number of characters to read (int)
            :rtype: The number of characters read (int)
            """
        buff = [None]*4096
        EOF = False
        ptr = 0

        while ptr < n and not EOF:
            count = read4K(buff)     # call read4(buf): to read into internal buffer
            if count < 4096:
                EOF = True
            length = min(n-ptr, count)
            for i in range(length):
                buf[ptr+i] = buff[i]
            ptr += length
        return ptr
        
        


# Follow-Up: The read function may be called multiple times.
# record what previously has been read

class Solution(object):
    def __init__(self):
        self.buff = [None]*4096
        self.buffptr = 0
        self.buffcnt = 0
        

    def read(self, buf, n):
        """
            :type buf: Destination buffer (List[str])
            :type n: Maximum number of characters to read (int)
            :rtype: The number of characters read (int)
            """
        ptr = 0
        while ptr < n:

            if self.buffptr == 0:
                self.buffcnt = read4K(self.buff)

            if self.buffcnt == 0:
                break

            while ptr < n and self.buffptr < self.buffcnt:    # note loop condition
                buf[ptr] = self.buff[self.buffptr]
                self.buffptr += 1
                ptr += 1

            if self.buffptr >= self.buffcnt:
                self.buffptr = 0

        return ptr
