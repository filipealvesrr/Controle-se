// UNIVASF - UNIVERSIDADE FEDERAL DO VALE DE SÃO FRANCISCO
// CAMPUS JUAZEIRO
// DISCIPLINA: SISTEMAS DE CONTROLE II
// UTILIZANDO PID PARA CONTROLAR ROTAÇÕES DO MOTOR
// NECESSÁRIO FAZER O DOWNLOAD DA LIB PID_v1.h EM: https://github.com/br3ttb/Arduino-PID-Library

#include <PID_v1.h>

const int Pin_rotacao = 2;
const int Pin_PWM = 9;

double Setpoint = 950;  
double Input, Output;
double Kp =  0.1, Ki = 0.01, Kd = 0.001;  
PID myPID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);

volatile byte pulsos;
unsigned int pulsos_por_volta = 2;
unsigned long timeold;

void contador(){
  pulsos++;
}

void setup() {
  Serial.begin(9600);
  pinMode(Pin_PWM, OUTPUT);
  pinMode(Pin_rotacao, INPUT);
  attachInterrupt(digitalPinToInterrupt(Pin_rotacao), contador, FALLING);
  pulsos = 0;
  timeold = millis();

  
  myPID.SetMode(AUTOMATIC);
  myPID.SetSampleTime(1000);  
}

void loop() {
  if (Setpoint < 1000) {
    Setpoint += 5;  
  }
  
  if (millis() - timeold >= 1000) {
    detachInterrupt(digitalPinToInterrupt(Pin_rotacao));

    // Cálculo da RPM
    Input = (60 * 1000 / pulsos_por_volta) / (millis() - timeold) * pulsos;
    pulsos = 0;

    myPID.Compute();

    
    Output = constrain(Output, 0, 255);

    
    analogWrite(Pin_PWM, Output);

    
    timeold = millis();
    attachInterrupt(digitalPinToInterrupt(Pin_rotacao), contador, FALLING);
  }

  print_serial(Input);
  delay(1000); 
}

void print_serial(double valor){
  Serial.println(Input);  
}
