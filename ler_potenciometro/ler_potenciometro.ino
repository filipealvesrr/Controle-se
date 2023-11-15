//const int potenciometro = A0;
const int Pin_rotacao = 2;
const int Pin_PWM = 9;
int i = 1023;
int cont=0;
int rpm;
//int valor_potenciometro = 0;
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
  attachInterrupt(0, contador, FALLING);
  pulsos = 0;
  rpm = 0;
  timeold = 0;
}

void loop() {
  
   if(cont == 9){
    if(i==0)
      i = 1023;
 
    else
      i = 0;

    cont = 0;
   }

  if (millis() - timeold >= 100)
  {
    detachInterrupt(0);
    rpm = (60 * 1000 / pulsos_por_volta ) / (millis() - timeold) * pulsos;
    timeold = millis();
    pulsos = 0;
    attachInterrupt(0, contador, FALLING);
  }

  //valor_potenciometro = analogRead(potenciometro);
  analogWrite(Pin_PWM, i);

  delay(100);
  print_serial();

  cont++;
}

void print_serial(){

  Serial.print(i);
  Serial.print(",");
  Serial.print(rpm);
  Serial.print(",");
  Serial.println(cont);
}
