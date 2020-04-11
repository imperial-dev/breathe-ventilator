 This program drives a unipolar or bipolar stepper motor.

 The motor should revolve one revolution in one direction, then
 one revolution in the other direction at varying speeds (controlled by potentiometer)

 The motor is attached to digital pins 8 - 11 of the Arduino.
Potentiometer is connected to analog input 0.

Credit to Tom Igoe (2007-2010)

 */

#include <Stepper.h>

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  Serial.begin(9600);
}

void loop() {
  // step one revolution  in one direction:
  Serial.println("clockwise");  % exhale
    // read the sensor value:
  int sensorReading = analogRead(A0);
  // map it to a range from 0 to 100:
  int motorSpeed = map(sensorReading, 0, 1023, 0, 100); % converts potentiometer output to integer value between 1-100 to ‘motorSpeed’
  // set the motor speed:
  if (motorSpeed > 0) { % if potentiometer is set to value above 0
    myStepper.setSpeed(motorSpeed/2); %Dividing by 2 so that exhale takes twice as long as inhale
    // step 1/100 of a revolution:
    myStepper.step(stepsPerRevolution / 100);
  }

delay(1000); % 1 sec pause between inhalation and exhalation

  // step one revolution in the other direction:
  Serial.println("counterclockwise"); % inhale

// read the sensor value:
  int sensorReading = analogRead(A0);
  // map it to a range from 0 to 100:
  int motorSpeed = map(sensorReading, 0, 1023, 0, 100);
  // set the motor speed:
  if (motorSpeed > 0) {
    myStepper.setSpeed(motorSpeed);
    // step 1/100 of a revolution:
    myStepper.step(-stepsPerRevolution / 100);
  }

  delay(1000); % 1 sec pause between inhalation and exhalation
}
