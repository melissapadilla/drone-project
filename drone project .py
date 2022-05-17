from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()
#starting point
me.move_up(80)
me.move_forward(500)
sleep(.5)
#turning into "must fly zone"
me.rotate_counter_clockwise(90)
me.move_forward(300)
sleep(.5)
#turn into next square
me.rotate_counter_clockwise(90)
me.move_forward(500)
sleep(.5)
#back to start5
me.rotate_counter_clockwise(90)
me.move_forward(300)
me.rotate_counter_clockwise(90)
#turn forward
me.rotate_counter_clockwise(90)
me.move_forward(300)
me.rotate_counter_clockwise(90)
#landing
sleep(.5)
me.land()
