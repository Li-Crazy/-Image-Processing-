# Author image
# !/usr/python3/bin/python3.6
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np

def BGR2HSI(bgr_img):
    #拷贝副本
    bgr=bgr_img.copy()
    B,G,R=cv.split(bgr/255.0)
    hsi_img=bgr.copy()/255.0
    H,S,I=cv.split(hsi_img)
    h,w=B.shape
    for i in range(h):
        for j in range(w):
            bgr_min=min(B[i,j],G[i,j],R[i,j])
            bgr_sum=B[i,j]+G[i,j]+R[i,j]
            I[i,j]=bgr_sum/3
            S[i,j]=1-3*bgr_min/bgr_sum
            cov=(R[i,j]-G[i,j])+(R[i,j]-B[i,j])
            var=2*np.sqrt((R[i,j]-G[i,j])**2+(R[i,j]-B[i,j])*(G[i,j]-B[i,j])**2)
            theta=np.arccos(cov/var)
            if G[i,j]>=B[i,j]:
                H[i,j]=theta/(2*np.pi)
            else:
                H[i,j]=(2*np.pi-theta)/(2*np.pi)
    hsi_img[:,:,0]=H
    hsi_img[:,:,1]=S
    hsi_img[:,:,2]=I
    return hsi_img
def HSI2BGR(hsi_img):
    hsi=hsi_img.copy()
    H,S,I=cv.split(hsi)
    bgr_img=hsi_img.copy()
    B,G,R=cv.split(bgr_img)
    h,w=B.shape
    for i in range(h):
        for j in range(w):
            if S[i,j]<1e-6:
                R[i,j]=I[i,j]
                G[i,j]=I[i,j]
                B[i,j]=I[i,j]
            else:
                H[i,j]*=360
                if H[i,j]>0 and H[i,j]<=120:
                    B[i,j]=(1-S[i,j])*I[i,j]
                    sigma=(H[i,j]-60)*np.pi/180
                    temp=np.tan(sigma)/np.sqrt(3)
                    G[i,j]=(1.5+1.5*temp)*I[i,j]-(0.5+1.5*temp)*B[i,j]
                    R[i,j]=3*I[i,j]-G[i,j]-B[i,j]
                elif H[i,j]>120 and H[i,j]<=240:
                    R[i,j]=(1-S[i,j])*I[i,j]
                    sigma=(H[i,j]-180)*np.pi/180
                    temp=np.tan(sigma)/np.sqrt(3)
                    B[i,j]=(1.5+1.5*temp)*I[i,j]-(0.5+1.5*temp)*R[i,j]
                    G[i,j]=3*I[i,j]-R[i,j]-B[i,j]
                elif H[i,j]>240 and H[i,j]<=360:
                    G[i,j]=(1-S[i,j])*I[i,j]
                    sigma=(H[i,j]-300)*np.pi/180
                    temp=np.tan(sigma)/np.sqrt(3)
                    R[i,j]=(1.5+1.5*temp)*I[i,j]-(0.5+1.5*temp)*G[i,j]
                    B[i,j]=3*I[i,j]-G[i,j]-R[i,j]
    bgr_img[:,:,0]=B
    bgr_img[:,:,1]=G
    bgr_img[:,:,2]=R
    return bgr_img

if __name__ == '__main__':
    bgr_img = cv.imread('/home/image/Pictures/sence.jpg')
    cv.imshow('Original',bgr_img)
    (W,H,chan) =bgr_img.shape

    hsi_img=BGR2HSI(bgr_img)
    cv.imshow('BGR2HSI',hsi_img)
    nimg=HSI2BGR(hsi_img)
    cv.imshow('HSI2BGR',nimg)
    cv.waitKey()
