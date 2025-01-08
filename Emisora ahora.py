#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Definir la dirección de la pantalla LCD
LiquidCrystal_I2C lcd(0x27, 16, 2); // Dirección 0x27, 16 columnas, 2 filas

void setup() {
  // Iniciar la comunicación con la pantalla LCD
  lcd.begin();
  lcd.backlight();  // Activar la retroiluminación

  // Enviar un mensaje al LCD
  lcd.setCursor(0, 0);  // Colocar el cursor en la primera línea, primera columna
  lcd.print("Hola Mundo!");

  lcd.setCursor(0, 1);  // Colocar el cursor en la segunda línea, primera columna
  lcd.print("Emisor LCD");
}

void loop() {
  // No es necesario hacer nada en el loop para este ejemplo
}
