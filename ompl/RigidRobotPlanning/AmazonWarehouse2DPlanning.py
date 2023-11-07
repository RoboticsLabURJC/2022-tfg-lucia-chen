#!/usr/bin/env python

# Author: Mark Moll

import sys
from os.path import abspath, dirname, join

ompl_app_root = dirname(dirname(dirname(abspath(__file__))))

from ompl import base as ob
from ompl import control as oc
from ompl import app as oa
from ompl import geometric as og


def amazonWarehouse():
    setup = oa.SE2RigidBodyPlanning()
    # comment out next two lines if you want to ignore obstacles
    setup.setRobotMesh('2D/car1_planar_robot.dae')
    setup.setEnvironmentMesh('2D/BugTrap_planar_env.dae')

    # plan for dynamic car in SE(2)
    stateSpace = setup.getStateSpace()

    # define start state
    start = ob.State(stateSpace)
    start().setX(7.02)
    start().setY(-12.0)
    start().setYaw(0.0)

    # define goal state
    goal = ob.State(stateSpace)
    goal().setX(-36.98)
    goal().setY(-10.0)
    goal().setYaw(2.25147473507)

    # set the start & goal states
    setup.setStartAndGoalStates(start, goal, 3.)

    # set the planner
    planner = og.RRTstar(setup.getSpaceInformation())
    setup.setPlanner(planner)

    # try to solve the problem
    # print("\n\n***** Planning for a %s *****\n" % setup.getName())
    # print(setup)
    if setup.solve(40):
        # print the (approximate) solution path: print states along the path
        # and controls required to get from one state to the next
        path = setup.getSolutionPath()
        # path.interpolate(); # uncomment if you want to plot the path
        print(path.printAsMatrix())
        # print(path)
        if not setup.haveExactSolutionPath():
            print("Solution is approximate. Distance to actual goal is %g" %
                    setup.getProblemDefinition().getSolutionDifference())

if __name__ == '__main__':
    amazonWarehouse()
