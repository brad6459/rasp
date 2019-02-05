const int led = 13;
const int command = 10;
int pistate = 0;

void setup() 
{
  pinMode(led,OUTPUT);
  pinMode(command, INPUT);
}

void loop() 
{
  pistate = digitalRead(command);
  if (pistate == HIGH)   
    {
    digitalWrite(led,HIGH);
    } 
  else 
    {
     digitalWrite(led,LOW);
    }    
}
