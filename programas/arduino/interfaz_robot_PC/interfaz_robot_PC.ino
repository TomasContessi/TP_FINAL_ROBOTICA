#include <Servo.h>

Servo eje1;  // crea el objeto servo
Servo eje2;  // crea el objeto servo
Servo eje3;  // crea el objeto servo
Servo eje4;  // crea el objeto servo

int pwm1 = 2;        // uso la pata D2 para enviar el PWM al servo 1
int pwm2 = 3;        // uso la pata D3 para enviar el PWM al servo 2
int pwm3 = 4;        // uso la pata D4 para enviar el PWM al servo 3
int pwm4 = 5;        // uso la pata D5 para enviar el PWM al servo 4
int gripper_out = 6; // uso la pata D6 para el gripper

const int pinLED = 13;
int Q[] = {90,140,40,90};
int gripper = 0;
int motors = 0;
// home <90:140:40:0>
int QlimPos[] = {180,152,40,180,0};//Q3 tambien tiene de limite Q2-algo porque como estan invertidos es complicado sacar la relacion Q2=70->Q3=45
int QlimNeg[] = {0,54,150,0,0};

const byte buffSize = 40;
char inputBuffer[buffSize];
const char startMarker = '<';
const char endMarker = '>';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newDataFromPC = false;

float inicio =0;
float fin = 0;

void setup(){
  eje1.attach(pwm1);  // vinculo los servos
  eje2.attach(pwm2);
  eje3.attach(pwm3);
  eje4.attach(pwm4);

   
  Serial.begin(115200);
  Serial.write(".");
  pinMode(pinLED, OUTPUT);
  pinMode(gripper_out, OUTPUT);
  }


void loop(){
  inicio=millis();                              // establesco un Ts de 20ms
  fin= inicio+20;

  
  
  if (Serial.available()>0) 
  {
    digitalWrite(pinLED, HIGH);
    SerialEvent();
    digitalWrite(pinLED, LOW);
    Serial.write(".");
    // actualizo los servos 
    if (motors == 1)
    {
      eje1.write(Q[1]); 
      eje2.write(Q[2]); 
      eje3.write(Q[3]); 
      eje4.write(Q[4]);
    }
  }


  digitalWrite(gripper_out, gripper);
  while (fin > millis())  {}
}
