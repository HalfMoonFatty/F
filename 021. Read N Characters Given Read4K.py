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
        buffer = [None]*4096    # internal 4k buffer
        EOF = False
        totalRead = 0

        while totalRead < n and not EOF:
            curRead = read4(buffer)     # call read4(buf): to read into internal buffer
            if curRead < 4:
                EOF = True
            length = min(n-totalRead, curRead)
            for i in range(length):
                buf[totalRead+i] = buffer[i]
            totalRead += length
        return totalRead
        
        


# Follow-Up: The read function may be called multiple times.
# record what previously has been read

class Solution(object):
    def __init__(self):
        self.buff = [None]*4096
        self.buffPtr = 0
        self.hasRead = 0
        self.count = 0
        self.EOF = False


    def read(self, buf, n):
        """
            :type buf: Destination buffer (List[str])
            :type n: Maximum number of characters to read (int)
            :rtype: The number of characters read (int)
            """
        
        while self.count < n and not EOF:
         
            # no more data in the internal buffer, need to read in new data
            if self.buffPtr == 0:
                self.hasRead = read4K(self.buff)

            # have no more to read-in
            if self.hasRead < 4096:
                EOF = True

            # 搬砖ing, 一次搬4块
            while self.count < n and self.buffPtr < self.hasRead:    # note loop condition
                buf[self.count] = self.buff[self.buffPtr]
                self.buffPtr += 1
                self.count += 1

            # drained up the internal buffer, reset the buffPtr to 0
            if self.buffPtr == self.hasRead:
                self.buffPtr = 0

        return self.count
