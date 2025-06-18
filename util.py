import numpy as np

def get_angle(a, b, c):
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])  # calculating a radians based on  x y coordinates
    angle = np.abs(np.degrees(radians))  # convert values that is in variable radians into a angle
    return angle

def get_distance(landmarks_list):
    if len(landmarks_list)<2:  # will exit if values in landmarks_list is less than 2 else it will execute the function
        return
    
    (x1,y1), (x2,y2) = landmarks_list[0], landmarks_list[1]
    l = np.hypot(x2 - x1, y2 - y1)  # calculating the didtance
    return np.interp(l, [0,1], [0,1000])