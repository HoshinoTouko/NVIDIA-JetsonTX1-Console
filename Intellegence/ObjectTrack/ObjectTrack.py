from __future__ import print_function
import sys
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range

import numpy as np
import cv2

import Modules.Camera as camModule

# local module
import video
from video import presets


class ObjTrack(object):
    def __init__(self, time):
        # self.cam = video.create_capture(video_src, presets['cube'])
        self.cam = camModule.Camera.getCamera()
        _ret, self.frame = self.cam.read()
        # cv2.namedWindow('camshift')
        # cv2.setMouseCallback('camshift', self.onmouse)
        self.width = 640
        self.height = 480
        
        self.selection = None
        self.drag_start = None
        self.show_backproj = False
        self.track_window = None
        self.run = False
        self.track_box = None
        self.time = time

    def track(self):
        if not self.run:
            for i in range(self.time):
                _ret, self.frame = self.cam.read()
            
            self.width = self.frame.shape[1]
            self.height = self.frame.shape[0]
            self.selection = (self.width/4, self.height/4, self.width-self.width/4 , self.height-self.height/4)
            self.track_window = (self.width/4, self.height/4, self.width/2, self.height/2)
            self.run = True
        # while True:
        _ret, self.frame = self.cam.read()
        vis = self.frame.copy()
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

        if self.selection:
            x0, y0, x1, y1 = self.selection
            hsv_roi = hsv[y0:y1, x0:x1]
            mask_roi = mask[y0:y1, x0:x1]
            hist = cv2.calcHist( [hsv_roi], [0], mask_roi, [16], [0, 180] )
            cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
            self.hist = hist.reshape(-1)
            # self.show_hist()

            vis_roi = vis[y0:y1, x0:x1]
            cv2.bitwise_not(vis_roi, vis_roi)
            vis[mask == 0] = 0

        if self.track_window and self.track_window[2] > 0 and self.track_window[3] > 0:
            self.selection = None
            prob = cv2.calcBackProject([hsv], [0], self.hist, [0, 180], 1)
            prob &= mask
            term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
            self.track_box, self.track_window = cv2.CamShift(prob, self.track_window, term_crit)

            if self.show_backproj:
                vis[:] = prob[...,np.newaxis]
            
            # try:
            #     cv2.ellipse(vis, self.track_box, (0, 0, 255), 2)
            # except:
            #     pass
            # cv2.imshow('camshift', vis)

        try:
            position = 100.0*self.track_box[0][0]/float(self.width) - 50.0
            area = 100.0*float(self.track_box[1][0]*self.track_box[1][1])/float(self.width*self.height)
            # area = 100.0*(track_box[0][0]/double(self.width))
            # return self.track_box[1][0]
            return position, area
        except:
            return (0, 50)


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    app = ObjTrack(cap, 50)
    while True:   
        pos = app.track()
        try:
            print(str(pos))
        except:
            pass
#         ch = cv2.waitKey(5)
#         if ch == 27:
#             break

    