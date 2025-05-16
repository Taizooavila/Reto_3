class Point:
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y
  def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y
  def reset(self):
    self.x = 0
    self.y = 0
  def compute_distance(self, point: "Point")-> float:
    distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
    return distance
  
class Rectangle:
  
  def __init__(self, method:list):
    #method = [#method, Bottom-left, width, height, center, top-right, vertical_line, horizontal_line]
    if method[0] == 1:
      self.center_point = Point(x = (method[1].x + (method[2]/2)),
                                y = (method[1].y + (method[3]/2)))
      self.height = method[3]
      self.width = method[2]
    elif method[0] == 2:
      self.center_point = method[4]
      self.height = method[3]
      self.width = method[2]
    elif method[0] == 3:
      self.height = (method[5].y - method[1].y)
      self.width = (method[5].x - method[1].x)
      self.center_point = Point(x = (method[1].x + (self.width/2)),
                                y = (method[1].y + (self.height/2)))
    else:
      self.height = (method[6].end.y - method[6].start.y)
      self.width = (method[7].end.x - method[7].start.x)
      self.center_point = Point(x = (method[6].start.x + (self.width/2)),
                                y = (method[6].start.y + (self.height/2)))

  def compute_area(self)->float:
    return self.height*self.width
  
  def compute_perimeter(self)->float:
    return (2*self.height)+(2*self.width)
  
  def compute_interference_point(self, point:Point):
    if (point.x > (self.center_point.x + self.height/2) or
        point.x < (self.center_point.x - self.height/2)):
      return False
    elif (point.y > (self.center_point.y + self.width/2) or
        point.y < (self.center_point.y - self.width/2)):
      return False
    else:
      return True
  
class Square(Rectangle):
  def __init__(self, center_point, height):
    super().__init__(center_point, height, height)

class Line:
  def __init__(self, point_1, point_2):
    self.start:Point = point_1
    self.end:Point = point_2
    self.length:float = ((((point_2.x - point_1.x)**2)
                        + ((point_2.y - point_1.y)**2))**0.5)
    if point_1.x == point_2.x:
      self.slope:float = 0
    else:
      self.slope:float = ((point_2.y - point_1.y)/(point_2.x - point_1.x))

  def compute_length (self):
    return self.length
  def compute_slope (self):
    return self.slope
  def compute_horizontal_cross (self):
    return ((self.start.x > 0 and self.end.x < 0) 
           or (self.start.x < 0 and self.end.x > 0))
  def compute_vertical_cross (self):
    return ((self.start.y > 0 and self.end.y < 0) 
           or (self.start.y < 0 and self.end.y > 0))