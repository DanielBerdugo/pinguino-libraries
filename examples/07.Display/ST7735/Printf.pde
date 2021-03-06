/**
        Author: 	Régis Blanchot (Mar. 2014)
        Tested on:	Pinguino 47J53 & Pinguino 32MX250
        Output:	262K-color graphic TFT-LCD with ST7735 controller

        2 modes available :
        - Hardware SPI
            . default mode
            . SPI operations are handled by the CPU
            . pins have to be the CPU SPI pins
            . PINGUINO 32 have up to 4 SPI module (SPI1 to SPI4)
            . PINGUINO 8  have only one SPI module (SPI1)
        - Software SPI
            . SPISW
            . SPI operations are handled by the SPI library
            . pins can be any digital pin
        
        Wiring :
        
        ST7735    PINGUINO
        ---------------------------------------
        LED       VSS (backlight on)
        SCK       SCK
        SDA       SDO
        A0 (DC)   can be connected to any digital pin
        RESET     VSS
        CS        can be connected to any digital pin
        GND       GND
        VSS       VSS (+5V or +3.3V)
**/

// Load one or more fonts and active them with ST7735.setFont()
#include <fonts/font6x8.h>

#define SPIMODULE SPI2

float f;

void setup()
{
    pinMode(USERLED, OUTPUT);
    ST7735.init(SPIMODULE, 0, 4, 0, 0);
    ST7735.setFont(SPIMODULE, font6x8);
    ST7735.setBackgroundColor(SPIMODULE, ST7735_BLACK);
    ST7735.setColor(SPIMODULE, ST7735_WHITE);
    ST7735.setOrientation(SPIMODULE, 180);
    ST7735.clearScreen(SPIMODULE);
}

void loop()
{
    ST7735.printf(SPIMODULE, "f=%.3f\r\n",f);
    f = f + 0.001f;
    toggle(USERLED);
    delay(100);
}
