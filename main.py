import struct
import numpy as np

ULONG_MASK = 0xffffffff

def read_ulong(datastream):
      date, = struct.unpack("<L", datastream.read(4))
      return date

def read_double_arr(size, datastream):
    data = np.fromfile(datastream, dtype=np.dtype('<d'), count=size)
    array = np.reshape(data, size, order='F')
    return array

def read_uint_arr(x,y,z, datastream):
    data = np.fromfile(datastream, dtype=np.uint16, count=x*y*z)
    array = np.reshape(data, [x,y,z], order="F")
    return array

if __name__ == "__main__":
    with open("data.dat", "rb") as data:

        time_arr_size = read_ulong(data)
        
        time = read_double_arr(time_arr_size, data)

        camera_image_frames = read_ulong(data)
        image_frame_size_x = read_ulong(data)
        image_frame_size_y = read_ulong(data)

        signal = read_uint_arr(image_frame_size_y, image_frame_size_x, camera_image_frames, data)

        pass

