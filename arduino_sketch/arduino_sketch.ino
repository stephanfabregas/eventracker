int ledPins[] = {8, 9, 10, 11};
int inputPins[] = {2, 3, 4, 5};
int numPins = 4;
unsigned long time;
int state = 4;
int val[] = {0, 0, 0, 0};
unsigned long currentTime = 0;

void setup() {
  for (int thisPin = 0; thisPin < numPins; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
    pinMode(inputPins[thisPin], INPUT);
  }
  Serial.begin(9600);
}

void loop(){

  if (Serial.available() == 2) {
    int byteOne = Serial.read();
    int byteTwo = Serial.read();
    if (byteOne == 82 && byteTwo != 87) { // Read is R (ASCII 82)
      Serial.print(state);
    } else if (byteOne == 87) { // Write is W (ASCII 87)
      if (byteTwo < 48 || byteTwo > 52) {
        Serial.print('E');
      } else {
        state = byteTwo - 48;
        lightState(state);
      }
    } else {
      Serial.print('E');
    }
  } else {
  
    for (int thisPin = 0; thisPin < numPins; thisPin++) {
      val[thisPin] = digitalRead(inputPins[thisPin]);
    }

    state = readState();
    lightState(state);
  }

}

int readState() {
  if (val[state]!=HIGH) {
    for (int thisPin = 0; thisPin < numPins; thisPin++) {
      if (val[thisPin]==HIGH) {
        Serial.print(thisPin);
        return(thisPin);
      }
    }
  }
  return(state);
}

void lightState(int state) {
    for (int thisPin = 0; thisPin < numPins; thisPin++) {
      if (ledPins[thisPin]!=state) {
        digitalWrite(ledPins[thisPin], LOW);
      }
    }
    digitalWrite(ledPins[state], HIGH);
}

