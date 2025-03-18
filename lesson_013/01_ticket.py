# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

print(os.getcwd())
print(os.listdir())


class TicketMarker:
    def __init__(self, name, where, whither, date, font_path=None):
        self.name = name
        self.where = where
        self.whither = whither
        self.date = date

        if font_path is None:
            self.font_path = os.path.join("Poppins-Black.ttf")
        else:
            self.font_path = font_path

    def make(self):
        image_ticket = Image.open('ticket_template.png')
        print(image_ticket.format, image_ticket.size, image_ticket.mode)

        draw = ImageDraw.Draw(image_ticket)
        font = ImageFont.truetype(self.font_path, size=20, encoding='UTF-8')

        text = f"{self.name}"
        draw.text((60, 120), text, font=font, fill=ImageColor.colormap["darkslategray"])

        text = f"{self.where}"
        draw.text((60, 190), text, font=font, fill=ImageColor.colormap["darkslategray"])

        text = f"{self.whither}"
        draw.text((60, 255), text, font=font, fill=ImageColor.colormap["darkslategray"])

        text = f"{self.date}"
        draw.text((260, 250), text, font=font, fill=ImageColor.colormap["darkslategray"])

        image_ticket.show()
        image_ticket.save("probe.png")


if __name__ == '__main__':
    ticket = TicketMarker(name="Lost name", where="City_1", whither="City_2", date="01.01.2025")
    ticket.make()
