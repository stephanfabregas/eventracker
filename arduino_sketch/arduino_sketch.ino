int ledPins[] = {8, 9, 10, 11};
int inputPins[] = {2, 3, 4, 5};
int numPins = 4;
unsigned long time;
const int TIMER = 100;
int state = -1;
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
  currentTime = millis();
  
  for (int thisPin = 0; thisPin < numPins; thisPin++) {
    val[thisPin] = digitalRead(inputPins[thisPin]);
  }
  
  state = setState();
  lightState(int(state));
    
  if (abs(currentTime - time) > TIMER) {
    serialWrite();
    time = currentTime;
  }

}

int setState() {
  if (val[state]!=HIGH) {
    for (int thisPin = 0; thisPin < numPins; thisPin++) {
      if (val[thisPin]==HIGH) {
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

void serialWrite() {
   Serial.print("Current state is: ");
   Serial.println(state+1);
}
