=============
Common Issues
=============

First Layer
===========

+---------------------------+--------------------------------+-------------------------+
| Issue                     | Cause                          | Solution                |
+===========================+================================+=========================+
| Print not sticking to bed | Bed not clean                  | Clean bead              |
|                           +--------------------------------+-------------------------+
|                           | Nozzle not clean               | Clean nozzle            |
|                           +--------------------------------+-------------------------+
|                           | Printing environment too cold  | Use enclosure           |
|                           |                                |                         |
|                           | (>15°C)                        | Turn on heater          |
|                           +--------------------------------+-------------------------+
|                           | Low bed temperature            | Check bed temperature   |
|                           |                                |                         |
|                           |                                | Increase bed by 5°C     |
|                           +--------------------------------+-------------------------+
|                           | PINDA probe knocked            | Adjust PINDA probe      |
|                           +--------------------------------+-------------------------+
|                           | Z height too high              | First layer calibration |
|                           |                                |                         |
|                           |                                | Live Z adjust           |
+---------------------------+--------------------------------+-------------------------+
| Skirting on first layers  | Z height low                   | Clean nozzle            |
|                           |                                |                         |
| Low extrusion             |                                | First layer calibration |
|                           |                                |                         |
| Bubbling on first layer   |                                | Live Z adjust           |
|                           |                                |                         |
| Nozzle gathering filament |                                |                         |
+---------------------------+--------------------------------+-------------------------+

Mid Print
=========

+------------------------+----------------------------+------------------------------------+
| Issue                  | Possible Cause             | Solution                           |
+========================+============================+====================================+
|                        |                            | Check bed temperature              |
| Excessive Stringing    | High extruder temp         |                                    |
|                        |                            | Reduce extruder temp   by 5°C      |
+------------------------+----------------------------+------------------------------------+
| Large prints lifting   | Bed not clean              | Clean print bed                    |
|                        +----------------------------+------------------------------------+
|                        |                            | Check bed temperature              |
|                        | Low bed temperature        |                                    |
|                        |                            | Increase temperature by 5°C        |
+------------------------+----------------------------+------------------------------------+
| Layer shift            | Print lifting   off bed    | Follow ‘Large prints lifting’      |
+------------------------+----------------------------+------------------------------------+
| Not extruding          | Incorrect filament type    | Reslice model for correct filament |
|                        |                            |                                    |
|                        |                            | Remove and reinsert filament       |
|                        +----------------------------+------------------------------------+
|                        | Incorrect extruder tension | Check extruder tension             |
|                        |                            |                                    |
|                        |                            | Remove and reinsert filament       |
|                        +----------------------------+------------------------------------+
|                        | Nozzle blocked             | Clean Nozzle                       |
|                        |                            |                                    |
|                        |                            | Remove and reinsert filament       |
+------------------------+----------------------------+------------------------------------+
|                        |                            | Check extruder   temp              |
| PETG not shiny         | Low extruder   temp        |                                    |
|                        |                            | Increase temp   by 5°C             |
|                        +----------------------------+------------------------------------+
|                        | Old filament               | Put in food dehydrator for 15min   |
+------------------------+----------------------------+------------------------------------+
|                        |                            | Check printbed temp                |
| Poor layer adhesion    | Low extruder temp          |                                    |
|                        |                            | Increase temp by 5°C               |
+------------------------+----------------------------+------------------------------------+

Minimum Temperature Error
=========================

+-----------------------------------------+-------------------------------------------+
| .. figure:: /images/min_temp_screen.jpg | .. figure:: /images/heatgun.jpg           |
|                                         |                                           |
|    Minimum temperature error screen     |    Use curved attachment to heat extruder |
+-----------------------------------------+-------------------------------------------+

The Prusa has a quality check which disables printing if the ambient temperature is >10°C.
Low environment temperature results in faster cooling, in turn, causing layer separation or lifting.
This can be fixed by moving the printer to a warmer environment or utilizing a printing enclosure.
The printbed will produce enough heat to keep the enclosure at a reasonable temperature.

If this is not possible, one can trick the printer into turing on.

- Aim a heatgun at the printbed. Monitor the screen and remove the heat once the temperature has exceed 15°C
- Heat up the extruder. This is best done with the curved attachement. There are parts of the extruder that are made of PETG which will soften/melt with excessive heat so be careful.
- Once both extruder and heatbed are <15°C press the reset button
- Immediately start your print. If not ready to print, preheat the printer
- Consider raising the environment temperature by turning on a heater


https://3dprinterly.com/how-to-dry-filament-like-a-pro-pla-abs-petg-nylon-tpu/
