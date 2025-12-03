""" This program can calculate the area of the following 2D shapes:
Circle
Triangle
Parallelogram
Pentagon
Hexagon
Octagon
To use the program, simply run it and follow the prompts.
Thanks for using!"""
print ("The calculator is starting up...")
while True: 
  option = input("Enter C, E, H, Pa, Pe, or O to calculate the area of your circle, ellipse, hexagon, parallelogram, pentagon, or octagon respectively. Enter x to leave the program. Enter answer here: ")
  if option == 'C':
    radius = float(input("Enter the radius of your circle: "))
    area = 3.14159 * radius**2
    print ("Area of your circle: %f" % area)
  elif option == 'E':
    axis_a = float(input("Enter the value of the semi-major axis (a) of your ellipse: "))
    axis_b = float(input("Enter the value of the semi-minor axis (b) of your ellipee: "))
    area = 3.14159 * axis_a * axis_b
    print ("Area of your ellipse: %f" % area)
  elif option == 'T':
    base = float(input("Enter the base of your triangle: "))
    height = float(input("Enter the height of your triangle: "))
    area = 0.5 * base * height
    print ("Area of your triangle: %f" % area)
  elif option == 'Pa':
    side1 = float(input("Enter the length of side 1 of your parallelogram: "))
    side2 = float(input("Enter the length of side 2 of your parallelogram: "))
    area = side1 * side2
    print ("Area of your parallelogram: %f" % area)
  elif option == 'O':
    side = float(input("Enter the length of a side of your octagon: "))
    area = 2 * (1 + 2**0.5) * side**2
    print ("Area of your octagon: %f" % area)
  elif option == 'Pe':
    side = float(input("Enter the length of a side of your pentagon: "))
    area = (1/4) * (5 * (5 + 2 * (5)**0.5))**0.5 * side**2
    print ("Area of your pentagon: %f" % area)
  elif option == 'H':
    side = float(input("Enter the length of a side of your hexagon: "))
    area = (3 * 3**0.5 / 2) * side**2
    print ("Area of your hexagon: %f" % area)
  elif option == "x":
    print ("Goodbye!")
    break
  else:
    print ("You have entered an invalid response. Please restart the program and try again.")
    break

print ("Closing calculator...")
