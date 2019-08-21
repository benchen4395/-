#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:40:28 2019

@author: chenben
"""

# IOU计算方法

def iou_compute(box1,box2):
    # box:x0,y0,x1,y1,score
    area1 = (box1[2]-box1[0]+1)*(box1[3]-box1[1]+1)
    area2 = (box1[2]-box1[0]+1)*(box1[3]-box1[1]+1)
    
    xx1 = max(box1[0],box2[0])
    yy1 = max(box1[1],box2[1])
    xx2 = min(box1[2],box2[2])
    yy2 = min(box1[3],box2[3])
    
    if xx1>=xx2 or yy1>=yy2:
        return 0
    
    intersect = (xx2-xx1+1)*(yy2-yy1+1)
    iou = intersect/(area1+area2-intersect)
    
    return iou

# nms:
import numpy as np
def nums(boxes,thresh):
    # boxes:[x0,y0,x1,y1,score]
    x1,y1,x2,y2,score = boxes[:,0],boxes[:,1],boxes[:,2],boxes[:,3],boxes[:,4]
    
    area = (x2-x1+1)*(y2-y1+1)
    nidx = np.argsort(score)[::-1]
    res = []
    
    while len(nidx):
        i = nidx[0]
        res.append(i)
        
        xx1 = np.maximum(x1[i],x1[nidx[1:]])
        yy1 = np.maximum(y1[i],y1[nidx[1:]])
        xx2 = np.minimum(x2[i],x2[nidx[1:]])
        yy2 = np.minimum(y2[i],y2[nidx[1:]])
        
        w = np.maximum(0,xx2-xx1+1)
        h = np.maximum(0,yy2-yy1+1)
        
        iou = w*h / (area[i]+area[nidx[1:]]-w*h)
        
        idx = np.where(iou<thresh)[0]
        nidx = nidx[idx+1]
    return res