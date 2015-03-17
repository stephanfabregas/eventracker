const int ledPin1 = 8;
const int ledPin2 = 9;
const int ledPin3 = 10;
const int ledPin4 = 11;
const int inputPin1 = 2;
const int inputPin2 = 3;
const int inputPin3 = 4;
const int inputPin4 = 5;

void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
  pinMode(inputPin1, INPUT);
  pinMode(inputPin2, INPUT);
  pinMode(inputPin3, INPUT);
  pinMode(inputPin4, INPUT);
}

void loop(){
  int val1 = digitalRead(inputPin1);
  int val2 = digitalRead(inputPin2);
  int val3 = digitalRead(inputPin3);
  int val4 = digitalRead(inputPin4);
  
  checkPin(val1, ledPin1);
  checkPin(val2, ledPin2);
  checkPin(val3, ledPin3);
  checkPin(val4, ledPin4);
}

void checkPin(int val, int pin) {
  if (val==HIGH) {
   digitalWrite(pin, HIGH);
  } else {
   digitalWrite(pin, LOW);
  }
}
