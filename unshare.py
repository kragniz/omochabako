import ctypes

sys_unshare = 272  # https://filippo.io/linux-syscall-table/

libc = ctypes.CDLL("libc.so.6")
libc.syscall.argtypes = [ctypes.c_int, ctypes.c_int]

def unshare(flags: int) -> int:
    return libc.syscall(sys_unshare, flags)
