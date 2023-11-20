import numpy as np
import laspy
data = np.genfromtxt("./2023-11-10_12-12-35.xyz", delimiter=" ")
print(data)
out_file = laspy.file.File("./2023-11-10_12-12-35.las", mode="w",header=laspy.header.Header())
print(out_file)
out_file.header.scale = [0.001, 0.001, 0.001]  # Set scaling to millimeters
out_file.header.offset = [0, 0, 0]  # Set the offset to zero
out_file.header.x_scale_factor = 0.001  # Set the X scale factor to millimeters
out_file.header.y_scale_factor = 0.001  # Set the Y scale factor to millimeters
out_file.header.z_scale_factor = 0.001
out_file.x = data[:,0]  # Set X coordinates
out_file.y = data[:,1]  # Set Y coordinates
out_file.z = data[:,2]  # Set Z coordinates
out_file.close()