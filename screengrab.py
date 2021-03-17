import numpy as np
import cv2
from PIL import ImageGrab
from pprint import pprint
Colors = {
    'DemUpper':[228, 180, 115],
    'DemLower':[210, 140, 49],
    'SwingUpper':[193, 107, 167],
    'SwingLower':[171, 100, 151],
    'RepUpper':[135, 90, 225],
    'RepLower':[105, 80, 190],
    'UnownedUpper':[240, 240, 255],
    'UnownedLower':[210, 210, 220],
    
    }
StateDict = {
    'WA':[103,293],
    'ID':[168,335],
    'MT':[126,387],
    'ND':[133,482],
    'MN':[170,521],
    'WI':[179,572],
    'MI':[186,624],
    'NH':[84,660],
    'VT':[110,681],
    'ME':[137,757],
    'NY':[169,724],
    'PA':[202,712],
    'RI':[180,819],
    'CT':[206,820],
    'NJ':[239,822],
    'DC':[265,822],
    'DE':[295,821],
    'MD':[315,821],
    'HI':[365,201],
    'AK':[229,155],
    'OR':[154,279],
    'CA':[269,264],
    'NV':[226,298],
    'AZ':[312,340],
    'UT':[234,328],
    'NM':[274,377],
    'CO':[234,380],
    'WY':[186,374],
    'SD':[177,454],
    'NE':[204,448],
    'KS':[249,461],
    'TX':[334,440],
    'LA':[340,540],
    'AR':[314,537],
    'MO':[236,531],
    'IA':[195,513],
    'IL':[246,582],
    'KY':[258,619],
    'TN':[290,596],
    'MS':[342,580],
    'AL':[338,624],
    'FL':[360,672],
    'GA':[329,666],
    'SC':[303,669],
    'NC':[279,692],
    'VA':[247,690],
    'IN':[240,607],
    'OH':[225,634],
    'WV':[245,675],
    'MA':[155,847]
}

gameBox = [483,247,1420,832]

image = ImageGrab.grab(bbox= gameBox)
image.save('test.png')
img = cv2.imread('test.png')
Dem_upper_range = np.array(Colors['DemUpper'])
Dem_lower_range = np.array(Colors['DemLower'])
Dem_mask = cv2.inRange(img, Dem_lower_range, Dem_upper_range)
Rep_upper_range = np.array(Colors['RepUpper'])
Rep_lower_range = np.array(Colors['RepLower'])
Rep_mask = cv2.inRange(img, Rep_lower_range, Rep_upper_range)
Swing_upper_range = np.array(Colors['SwingUpper'])
Swing_lower_range = np.array(Colors['SwingLower'])
Swing_mask = cv2.inRange(img, Swing_lower_range, Swing_upper_range)
Unowned_upper_range = np.array(Colors['UnownedUpper'])
Unowned_lower_range = np.array(Colors['UnownedLower']) 
Unowned_mask = cv2.inRange(img, Unowned_lower_range, Unowned_upper_range)

for state in StateDict:
    r = str(img[StateDict[state][0],StateDict[state][1],2])
    g = str(img[StateDict[state][0],StateDict[state][1],1])
    b = str(img[StateDict[state][0],StateDict[state][1],0])
    # print(int(r))
    # print(Colors['DemLower'][2])
    print(state + " : " + r + ", " + g + ", " + b)
    if 49 <= int(r) <= 115:
        print("Democratic State ")

while(1):
    cv2.imshow('image', img)
    cv2.imshow('Unowned_mask', Unowned_mask)
    k = cv2.waitKey(33)
    if k == 27:
        break
#cv2.imshow('Dem_mask', Dem_mask)
#cv2.imshow('Rep_mask', Rep_mask)
#cv2.imshow('Swing_mask', Swing_mask)