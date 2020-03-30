from PIL import Image,ImageDraw,ImageFont
import win32api, win32gui, win32con
import time
import sys

tmp = "C:\\temp\\bg_tmp.png"

def add_text(text,image_path,save_path_name,text_RGBA=(255,255,255,50),text_xy = (1.0,1.0),text_font = 'C:\Windows\Fonts\simhei.ttf',text_font_size=100):
    # 读入原图
    image = Image.open(image_path)
    # 字体
    font = ImageFont.truetype(text_font,text_font_size)
    layer = image.convert('RGBA')
    text_overlay = Image.new('RGBA',layer.size,(255,255,255,0))
    image_draw = ImageDraw.Draw(text_overlay)
    # 文字长宽
    text_size_x,text_size_y = image_draw.textsize(text,font)
    # 文字位置
    text_xy = ((layer.size[0]-text_size_x)*text_xy[0],(layer.size[1]-text_size_y)*text_xy[1])
    image_draw.text(text_xy,text,font=font,fill=text_RGBA)
    # 合成
    after = Image.alpha_composite(layer,text_overlay)
    # 导出
    after.save(save_path_name)

def setWallPaper(pic):
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    
    # open register
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "3")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)

add_text(time.strftime('%Y-%m-%d %A', time.localtime(time.time())),sys.argv[1],tmp,text_xy =(0.98,0.98),text_font_size=60)
setWallPaper(tmp)