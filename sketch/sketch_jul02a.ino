void setup() {
  // Seeding the Random Number Generator
  randomSeed( analogRead(A0) );
  // Setting Baudrate
  Serial.begin(9600);
}

void loop() {

  Serial.print("Arduino Output = ");
  Serial.print(random(1, 101));
  Serial.println("");
  delay(1000);
  
}
