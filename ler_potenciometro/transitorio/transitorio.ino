const int Pin_rotacao = 2;
const int Pin_PWM = 9;

double Setpoint = 950;  
double Input, Output;
volatile byte pulsos;
unsigned int pulsos_por_volta = 2;
unsigned long timeold;

void contador() {
  pulsos++;
}

void setup() {
  Serial.begin(9600);
  pinMode(Pin_PWM, OUTPUT);
  pinMode(Pin_rotacao, INPUT);
  attachInterrupt(digitalPinToInterrupt(Pin_rotacao), contador, FALLING);
  pulsos = 0;
  timeold = millis();
}

void loop() {

  if (millis() - timeold >= 1000) {
    detachInterrupt(digitalPinToInterrupt(Pin_rotacao));

    Input = (60 * 1000 / pulsos_por_volta) / (millis() - timeold) * pulsos;
    pulsos = 0;

    Output = Setpoint - Input;

    analogWrite(Pin_PWM, Output);

    timeold = millis();
    attachInterrupt(digitalPinToInterrupt(Pin_rotacao), contador, FALLING);
  }

  print_serial(Input);
  delay(1000);
}

void print_serial(double valor){
  Serial.println(valor);
}
