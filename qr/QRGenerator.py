import qrcode
import os
from PIL import Image
import matplotlib.pyplot as plt

qr_path = os.path.expanduser('~') + "\\qr.png"


class QRGenerator:
    """
      PIL Python Image Library
    """
    @staticmethod
    def generate_uri_qr(uri):
        """
         生成URI的二维码
        :return: void
        """
        qr_image = qrcode.make(uri)
        with open(qr_path, "wb") as fo:
            qr_image.save(fo)
            fo.close()
        return qr_path

    @staticmethod
    def generate_qr_params(qr_name):
        """
          version  二维码尺寸[1,40] 最小尺寸为1,21*21，每+1，尺寸+4
          box_size 二维码格子像素大小
          border   边框格子大小
        :param qr_name:
        :return:
        """
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1
        )
        qr.add_data(qr_name)  # 扫描后显示的跳转名称，比如公众号名称
        qr.make(fit=True)  # 编译data到QR数组
        qr_image = qr.make_image()  # 生成图片
        qr_image.save(qr_path)  # 保存文件
        return qr_path

    @staticmethod
    def generate_qr_icon(qr_name, logo):
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1
        )
        qr.add_data(qr_name)
        qr.make(fit=True)
        # 设置填充颜色
        qr_image = qr.make_image(fill_color="green", back_color="white")
        qr_image.convert("RGBA")
        icon = Image.open(logo).convert("RGBA")
        img_w, img_h = qr_image.size
        size_w = int(img_w / 3)
        size_h = int(img_h / 3)

        icon_w, icon_h = icon.size
        if icon_w > size_w or icon_h > size_h:
            icon_w = size_h
            icon_h = size_h
        icon_resize = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
        # 居中显示
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)

        qr_image.paste(icon_resize, (w, h), mask=None)
        qr_image.save(qr_path)
        plt.imshow(qr_image)
        plt.show()
        return


if __name__ == '__main__':
    print(QRGenerator.generate_qr_icon("http://www.baidu.com", "C:\\Users\\lenovo\\Desktop\\p.gif"))
