#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT6, False)
right_drive_smart = Motor(Ports.PORT10, True)
drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 259.34, 320, 40, MM, 1)


# Wait for sensor(s) to fully initialize
wait(100, MSEC)

# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 

# Initialize random seed 
initializeRandomSeed()

vexcode_initial_drivetrain_calibration_completed = False
def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    global vexcode_initial_drivetrain_calibration_completed
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    brain_inertial.calibrate()
    while brain_inertial.is_calibrating():
        sleep(25, MSEC)
    vexcode_initial_drivetrain_calibration_completed = True
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


# Calibrate the Drivetrain
calibrate_drivetrain()

#endregion VEXcode Generated Robot Configuration
myVariable = 0

def when_started1():
    global myVariable
    drivetrain.drive_for(FORWARD, 5.5, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 2, INCHES)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 1.5, INCHES)
    drivetrain.turn_for(LEFT, 45, DEGREES)
    drivetrain.set_drive_velocity(300, PERCENT)
    drivetrain.drive_for(FORWARD, 17, MM)
    drivetrain.stop()
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.turn_for(LEFT, 46, DEGREES)
    drivetrain.drive_for(FORWARD, 1.5, INCHES)
    drivetrain.set_drive_velocity(500, PERCENT)
    drivetrain.drive_for(FORWARD, 9.5, INCHES)
    drivetrain.stop()
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.turn_for(LEFT, 98, DEGREES)
    drivetrain.drive_for(FORWARD, 1, INCHES)
    drivetrain.turn_for(LEFT, 15, DEGREES)
    drivetrain.drive_for(FORWARD, 37, MM)
    drivetrain.turn_for(RIGHT, 15, DEGREES)
    drivetrain.drive_for(FORWARD, 27, INCHES)
    drivetrain.turn_for(RIGHT, 78, DEGREES)
    drivetrain.drive_for(FORWARD, 12, INCHES)
    drivetrain.drive_for(REVERSE, 7.5, INCHES)
    drivetrain.turn_for(RIGHT, 53, DEGREES)
    drivetrain.drive_for(FORWARD, 6, INCHES)
    drivetrain.turn_for(RIGHT, 37, DEGREES)
    drivetrain.drive_for(FORWARD, 30, INCHES)

when_started1()
