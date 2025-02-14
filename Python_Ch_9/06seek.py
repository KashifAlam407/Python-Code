## .seek() method is used with file object to change the file pinter's position within a file. This is particularly useful when you're reading from or writing to a file and want to move to a specific byte location.

## Syntax:
# file_object.seek(offset, whence)  # offset means the number of bytes to move the file pinter. This can be positive (to move forward) or negative (to move backward) and whence is optional parameter determines the reference point for the offset. It can take the following value[0:The beginning of the file(default), 1:The current file position, 2: The end of the file.]


## Examples:
# file.seek(5)  # move the pointer to the 5th byte
# file.seek(0)  # move to the start of the file
# file.seek(0, 2)  # move to the end of the file



