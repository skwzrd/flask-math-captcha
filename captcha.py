from random import random
from PIL import Image, ImageDraw, ImageFont, ImageColor
import base64
from io import BytesIO
import os

class MathCaptcha:
  """
  You will need a tff from somewhere as pillow (PIL) doesnt provide any.
  
  Tested on pillow-8.4.0 and pillow-9.4.0
  """
  def __init__(self,
    tff_filename='EXAMPLE.ttf',
    tff_dir=None,
    size = (90, 40),
    font_size=25,
    font_color=ImageColor.getcolor('black', 'RGB'),
    background_color=ImageColor.getcolor('white', 'RGB')
  ):
    tff_dir = os.path.abspath(os.path.dirname(__file__)) if tff_dir is None else tff_dir
    tff_path = os.path.join(tff_dir, 'fonts', tff_filename)

    self.size = size
    self.font = ImageFont.truetype(tff_path, font_size)
    self.font_color = font_color
    self.background_color = background_color

    self.delimiter = ';.;'

  def is_valid(self, test_id, answer):
    if not test_id or not answer: return False
    try:
      decoded = base64.b64decode(test_id).decode()
      first, second = decoded.split(self.delimiter)
      first, second, answer = int(first), int(second), int(answer)
      return first + second == answer
    except:
      return False

  def generate_image(self, text):
    img = Image.new("RGB", self.size, self.background_color)
    draw = ImageDraw.Draw(img)
    xy = (5, 5)
    draw.text(xy, text, self.font_color, font=self.font)
    
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

  @staticmethod
  def generate_random():
    """Returns a random int between 0 and 10 (inclusive)."""
    return int(random()*10)

  def generate_captcha(self):
    first_num = MathCaptcha.generate_random()
    second_num = MathCaptcha.generate_random()

    captcha_id = base64.b64encode(f'{first_num}{self.delimiter}{second_num}'.encode()).decode()
    captcha_b64_img_str = self.generate_image(f'{first_num} + {second_num}')

    return captcha_id, captcha_b64_img_str
