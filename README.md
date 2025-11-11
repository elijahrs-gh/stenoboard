# Stenoboard V1
A 28 key stenography keyboard.

**Finished PCB 3d render:**
<img width="974" height="435" alt="Screenshot 2025-11-11 at 11 15 09 AM" src="https://github.com/user-attachments/assets/87a21844-ff7e-48c0-bc97-01d535f907f5" />

## Pictures

**PCB:**
<img width="1623" height="667" alt="Screenshot 2025-11-11 at 11 15 22 AM" src="https://github.com/user-attachments/assets/c6a8a9e6-fdbc-43f6-bfd4-a643b1ad8611" />

**Schematic:**
<img width="1488" height="747" alt="Screenshot 2025-11-11 at 11 15 42 AM" src="https://github.com/user-attachments/assets/e3471ec3-81b8-4d48-9f0a-fb7bf0db68f3" />

**Case:**
<img width="1347" height="589" alt="Screenshot 2025-11-11 at 11 15 57 AM" src="https://github.com/user-attachments/assets/c04d9cff-5af6-4c98-8118-d8d19e896f24" />

## BOM
| Reference                                                                 | Qty | Value    | DNP | Exclude from BOM | Exclude from Board | Footprint                                                         | Datasheet                                                                                  |
|---------------------------------------------------------------------------|-----|----------|-----|------------------|-------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| A1                                                                        | 1   | RaspberryPi_Pico |     |                  |                   | Module:RaspberryPi_Pico_Common_Unspecified                        | https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf                                 |
| D1, D2                                                                    | 2   | SK6812MINI |     |                  |                   | LED_SMD:LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm                    | https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf                 |
| D3–D30 (28 parts)                                                         | 28  | 1N4148   |     |                  |                   | Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal                        | https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf                         |
| SW1–SW28 (28 switches)                                                    | 28  | SW_Push  |     |                  |                   | Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB                     | ~                                                                                            |
