import struct
import numpy as np

ULONG_MASK = 0xffffffff # Use to manually unsign an integer

def read_ulong(datastream):
    #Read Little Endian Long from datastream
    date, = struct.unpack("<L", datastream.read(4))
    return date

def read_double_arr(size, datastream):
    #Read little endian double from datastream into an array with size size
    data = np.fromfile(datastream, dtype=np.dtype('<d'), count=size)
    #Then reshape it into Fortran index order
    array = np.reshape(data, size, order='F')
    return array

def read_uint_arr(x,y,z, datastream):
    #Read uint16 into a 1-D array with size x y z
    data = np.fromfile(datastream, dtype=np.uint16, count=x*y*z)
    #then reshape it into a 3-D array with Fortran indexing order
    array = np.reshape(data, [x,y,z], order="F")
    return array

if __name__ == "__main__":
    # trivial
    with open("data.dat", "rb") as data:

        time_arr_size = read_ulong(data)
        
        time = read_double_arr(time_arr_size, data)

        camera_image_frames = read_ulong(data)
        image_frame_size_x = read_ulong(data)
        image_frame_size_y = read_ulong(data)

        signal = read_uint_arr(image_frame_size_y, image_frame_size_x, camera_image_frames, data)

        pass

