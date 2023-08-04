import argparse
import qrcode
import cv2
import os

width = 153 #Breite QR Code
height = 215 #Höhe QR Code
dim = (width, height)
font = cv2.FONT_HERSHEY_SIMPLEX #Font
org = (160, 50) #Org Name
orgTEXT1 = (160, 100) #Org Text1
orgTEXT2 = (160, 120) #Org Text2
orgTEXT3 = (160, 140) #Org Text3
orgTEXT4 = (160, 160) #Org Text4
orgMSM = (160, 190) #Org MSM Eigentum
fontScale = 1
color = (0, 0, 0) #Schriftfarbe
thickness = 1 #Schriftdicke
parser = argparse.ArgumentParser()

pfadLeer = "/Users/test/Desktop/Space/"

parser.add_argument('--name', type=str, required=True, help='Name des Geräts') 
parser.add_argument('--url', type=str, required=True, help='URL im QR Code') #URL im QR Code
parser.add_argument('--text1', type=str, required=False, default="", help='Freitext Zeile 1') #Freitext Zeile 1
parser.add_argument('--text2', type=str, required=False, default="", help='Freitext Zeile 2') #Freitext Zeile 2
parser.add_argument('--text3', type=str, required=False, default="", help='Freitext Zeile 3') #Freitext Zeile 3
parser.add_argument('--text4', type=str, required=False, default="", help='Freitext Zeile 4') #Freitext Zeile 4
parser.add_argument('--foot', type=str, required=False, default="Eigentum MakerSpace Minden e.V.", help='Fusszeile. Default: Eigentum MakerSpace Minden e.V.') #Fusszeile
parser.add_argument('--out', type=str, required=True, help='Pfad zum Speicherort') #Pfad zum speichern 
args = parser.parse_args()

path = args.out 
name = args.name
URL = args.url
qr = qrcode.make(URL)
text1 = args.text1
text2 = args.text2
text3 = args.text3
text4 = args.text4
qr.save(path + name + ".png")
s_img = cv2.imread(path + name + ".png")
l_img = cv2.imread(pfadLeer + "StickerLeer.png")
s_img = cv2.resize(s_img, dim, interpolation = cv2.INTER_AREA)
x_offset=y_offset=1
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
l_img = cv2.putText(l_img, name, org, font, fontScale, color, thickness, cv2.LINE_AA)
l_img = cv2.putText(l_img, text1, orgTEXT1, font, 0.6, color, thickness, cv2.LINE_AA)
l_img = cv2.putText(l_img, text2, orgTEXT2, font, 0.6, color, thickness, cv2.LINE_AA)
l_img = cv2.putText(l_img, text3, orgTEXT3, font, 0.6, color, thickness, cv2.LINE_AA)
l_img = cv2.putText(l_img, text4, orgTEXT4, font, 0.6, color, thickness, cv2.LINE_AA)
l_img = cv2.putText(l_img, args.foot, orgMSM, font, 0.5, color, thickness, cv2.LINE_AA)
l_img = cv2.rotate(l_img, cv2.ROTATE_90_CLOCKWISE) 
cv2.imwrite(path + "sticker" + name + ".png", l_img)
os.remove(path + name + ".png")  
