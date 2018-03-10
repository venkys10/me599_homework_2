#!usr/bin/env python

from subprocess import call

class Simulator:
    def __init__(self, inst_number):
        self.num = inst_number

    def evaluate(self):
        w = [(-10,-10),(10,10)]

            # write to a waypoints file

        write_to_file = open('waypoint_new.txt', 'w')
        for i in w:
            write_to_file.write("%s" %i)

            #call external program

        call(["/home/reu_student_1/PycharmProjects/me599_homework_2/simulator-linux","-1"])

            #get output



