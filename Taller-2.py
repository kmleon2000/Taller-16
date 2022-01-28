import cv2 as draw, numpy as np

def draw_line():
  window = np.ones((500,700,3), dtype = np.uint8) * 40
  draw.line(
    window,
    (100,250),
    (600,250),
    (160, 93, 20),
    5
  )
  draw.imshow('Line',window)
  draw.waitKey()
  draw.destroyAllWindows()

def draw_ellipse():
  window = np.ones((500,700,3), dtype = np.uint8) * 40
  draw.ellipse(
    window,
    (350,250),
    (200,150),
    0,
    0,
    360,
    (160, 93, 20),
    5
  )
  draw.imshow('Ellipse',window)
  draw.waitKey()
  draw.destroyAllWindows()

draw_line()
draw_ellipse()