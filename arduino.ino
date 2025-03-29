x #include <Servo.h>

#define EMG_PIN A0
#define SERVO_PIN 3

Servo SERVO_1;
int servoPos = 10;  // Posição inicial do servo

void setup() {
  Serial.begin(115200);
  SERVO_1.attach(SERVO_PIN);
  SERVO_1.write(servoPos);  // Inicializa o servo na posição 10
}

void loop() {
  int value = analogRead(EMG_PIN);
  Serial.println(value);  // Envia o valor do EMG para o Python

  delay(100);  // Atraso entre as leituras
}
