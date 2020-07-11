# 二维码生成器

    QRCode依赖于pillow，在使用该库的时候请安装pillow库
    
    ```shell
        pip install pillow
        pip install numpy
    ```
   
   ```python
           import qrcode
           qr = qrcode.QRCode(
               version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_L,
               box_size=10,
               border=4,
           )
           qr.add_data('Some data')
           qr.make(fit=True)
           
           img = qr.make_image(fill_color="black", back_color="white")
   ``` 
   
   version  参数范围为[1,40] 控制二维码的大小，1代表21*21，当设置为None或fit的时候自动赋值
   fill_color 和 back_color改变背景颜色
   error_correction 控制容错率，具有四个级别，分别如下：
      ERROR_CORRECT_L 容错率7%
      ERROR_CORRECT_M 默认容错率 15%
      ERROR_CORRECT_Q 25%以内
      ERROR_CORRECT_H 30%以内
   box_size 设置二维码每个方块大小单位为px
   border 控制边框px
   
# Python生成炫酷二维码
```shell
    pip install pillow
    pip install numpy
    pip install imageio
    pip install myqr
```

###使用myqr生成艺术二维码：
```sbtshell
   myqr 跳转路径 -p 美化图片路径 -c -con 1.5 -bri 1.6   # 将连接生成URL
```

### myqr选项：

  -h, --help            显示myqr的帮助信息
  -v {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40}, 
  --version {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40}
                        The version means the length of a side of the QR-Code
                        picture. From little size to large is 1 to 40.
  -l {L,M,Q,H}, --level {L,M,Q,H}
                        Use this argument to choose an Error-Correction-Level:
                        L(Low), M(Medium) or Q(Quartile), H(High). Otherwise,
                        just use the default one: H
  -p PICTURE, --picture PICTURE
                        the picture e.g. example.jpg
  -c, --colorized       Produce a colorized QR-Code with your picture. Just
                        works when there is a correct '-p' or '--picture'.
  -con CONTRAST, --contrast CONTRAST
                        A floating point value controlling the enhancement of
                        contrast. Factor 1.0 always returns a copy of the
                        original image, lower factors mean less color
                        (brightness, contrast, etc), and higher values more.
                        There are no restrictions on this value. Default: 1.0
  -bri BRIGHTNESS, --brightness BRIGHTNESS
                        A floating point value controlling the enhancement of
                        brightness. Factor 1.0 always returns a copy of the
                        original image, lower factors mean less color
                        (brightness, contrast, etc), and higher values more.
                        There are no restrictions on this value. Default: 1.0
  -n NAME, --name NAME  The filename of output tailed with one of {'.jpg',
                        '.png', '.bmp', '.gif'}. eg. exampl.png
  -d DIRECTORY, --directory DIRECTORY
                        The directory of output.


参考：
 [qrcode](https://pypi.org/project/qrcode/)
 [python生成个性化二维码](https://blog.csdn.net/xc_zhou/article/details/80952036)
 [python生成炫酷的二维码](https://blog.csdn.net/csdnnews/article/details/81880380)