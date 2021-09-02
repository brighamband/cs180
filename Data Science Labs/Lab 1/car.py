class Car:
  def __init__(self, color, model, year, max_speed, mileage, cur_speed):
    self.color = color
    self.model = model
    self.year = year
    self.max_speed = max_speed
    self.mileage = mileage
    self.cur_speed = cur_speed

  def print_speed(self):
    print('New speed: ', self.cur_speed)

  def accelerate(self, amount):
    '''Increase current speed by 'amount' miles per hour'''
    self.cur_speed += amount
    self.print_speed()

  def brake(self):
    '''Decrease current speed by 20%'''
    self.cur_speed *= 0.8
    self.print_speed()
  
car = Car('blue', 'Corolla', 2007, 100, 40, 0)

print('Speeding up.')
while (car.cur_speed + 10) <= car.max_speed:
  car.accelerate(10)

print('Max speed reached. Slowing back down.')
car.brake()
while car.cur_speed > 0:
  car.cur_speed -= 10
  car.print_speed()

print('Car has stopped')