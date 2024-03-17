/*How to make a Bluetooth control car
 * https://srituhobby.com
 */
 
#include <AFMotor.h>
#include <Servo.h>
#define Speed 250

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

Servo servo1;
Servo servo2;

void setup() {
  Serial.begin(9600);
  motor1.setSpeed(Speed);
  motor2.setSpeed(Speed);
  motor3.setSpeed(Speed);
  motor4.setSpeed(Speed);

  servo1.attach(9);
  servo2.attach(10);
  servo1.write(70);
  servo2.write(180 - 70);
}

void loop() {
  if (Serial.available() > 0) {
    char value = Serial.read();
    Serial.println(value);

    if (value == '1') {
      servo1.write(70);
      servo2.write(180 - 70);
    } else if (value == '2') {
      servo1.write(80);
      servo2.write(180 - 80);
    } else if (value == '3') {
      servo1.write(90);
      servo2.write(180 - 90);
    } else if (value == '4') {
      servo1.write(100);
      servo2.write(180 - 100);
    } else if (value == '5') {
      servo1.write(120);
      servo2.write(180 - 120);
    } else if (value == '6') {
      servo1.write(140);
      servo2.write(180 - 140);
    } else if (value == '7') {
      servo1.write(150);
      servo2.write(180 - 150);
    } else if (value == '8') {
      servo1.write(160);
      servo2.write(180 - 160);
    } else if (value == '9') {
      servo1.write(170);
      servo2.write(180 - 170);
    } else if (value == 'F') {
      forward();
    } else if (value == 'B') {
      backward();
    } else if (value == 'L') {
      left();
    } else if (value == 'R') {
      right();
    } else {
      Stop();
    }
  }
}

void forward() {
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(FORWARD);
}
void backward() {
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
}
void left() {
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}
void right() {
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}
void Stop() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}