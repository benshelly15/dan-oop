import math
from random import randint
if __name__ == "__main__":
    # Input sides
    sides = [float(side) for side in input("Input sides (space separated): ").split()]
    # Output stats
    print(sides)


    no_sides = len(sides)
    s = sum(sides)/2
    
    def triangle():        
        tri_area = math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2]))
        print(tri_area,'units^2')
        angle_a = math.degrees(math.asin((2*tri_area)/(sides[1]*sides[2])))
        angle_b = math.degrees(math.asin((2*tri_area)/(sides[0]*sides[2])))
        angle_c = math.degrees(math.asin((2*tri_area)/(sides[0]*sides[1])))
        tri_angles = [angle_a, angle_b, angle_c]
        print(tri_angles)
        
        for a in tri_angles:
            if 90.0 == a:
                print("Right Angled Triangle")        
        if tri_angles.count(tri_angles[0]) == (no_sides/3):
                print("Scalene Triangle")
        elif tri_angles.count(tri_angles[0]) == (no_sides*2/3):            
            print("Isosocles Triangle")         
        else:
            print("Equilateral Triangle")
    
    def quadrilateral():
        first_angle = randint(1, 179)
        if (first_angle >= 90):
            second_angle = randint(1,90)
        else:
            second_angle = randint(90,179)
        third_angle = randint(1,179)
        rand_angles = [first_angle, second_angle, third_angle, 360 - (first_angle + second_angle + third_angle)]
        print(rand_angles)
        for x in rand_angles:
            if 90.0 == x and rand_angles.count(rand_angles[0])==no_sides:
                print('Square')
            elif sides[0] == sides[2] and sides[1] == sides[3] and sides[0] != sides[3] and x == 90:
                print('Rectangle')
            elif x != 90 and sides[0] == sides[2] and sides[1] == sides[3]:
                print('Parallelogram')
            elif sides[0] == sides[1] or sides[2] == sides[3] and rand_angles[0] == rand_angles[2] or rand_angles[1] == rand_angles[3]:
                print('Kite')
            elif 90.0 != x and no_sides == 4:
                print('Rhombus')

        theta = first_angle + third_angle
        quad_area = math.sqrt((s-sides[0])*(s-sides[1])*(s-sides[2])*(s-sides[3])-(sides[1]*sides[2])*(sides[1]*sides[2])*math.sin(theta/2)**2)
        print(quad_area,'units^2')

    def pentagon():
        if sides.count(sides[0])==no_sides:
            pen_area = (sides[0]**2/4)*math.sqrt(5*(5+2*math.sqrt(5)))
            print('Pentagon')
            print(pen_area,'units^2')                    
            print('Interior angles are 108')
        else:
            print('Sorry, all sides must be equal.')


    def hexagon():
        if sides.count(sides[0])==no_sides:
            hex_area = (sides[0]**2)*(3*math.sqrt(3))/2
            print('Hexagon')
            print(hex_area,'units^2')                    
            print('Interior angles are 120')
        else:
            print('Sorry, all sides must be equal.')

        

if no_sides == 3:
    triangle()
elif no_sides == 4:
    quadrilateral()
elif no_sides == 5:
    pentagon()
elif no_sides == 6:
    hexagon()
else:
    print('Please input number of sides between 3 and 6.')   