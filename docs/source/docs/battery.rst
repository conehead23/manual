===============
Battery Testing
===============

We are doing a full discharge test on the batteries to see how much capacity it will have in the field.
This is compared to the supposed capacity which gives us the battery health.

Discharge Current
=================

First step is to find the discharge current of the battery.
The best way is to find the battery datasheet online and find the 20h capacity.
The tester is limited to 100W discharge so ensure the discharge rate is less than 7.5A.
Sometimes this can be calculated from the battery for example:

+------------------------------------------+----------------------------------------------+
| .. image:: /images/battery_specs.jpg     | .. image:: /images/battery_datasheet.PNG     |
|    :target: ../_images/battery_specs.jpg |    :target: ../_images/battery_datasheet.PNG |
+------------------------------------------+----------------------------------------------+

- 5AH Capacity over 20 Hr = 5/20 = 0.25A discharge rate

Ensure you have the correct rate or else one cannot compare capacity to get the battery health

.. csv-table:: Battery List
    :file: /files/batteries.csv
    :header-rows: 1
    :stub-columns: 2

EBC-A20 Battery Analyser
========================

- Ensure battery is charged before putting on analyser.
  The analyser has a timeout after 60H, which can stop the test midway if analysing a large discharged battery
- Turn on the computer and EBC-A20
- Connect the leads to the battery
- Open :guilabel:`EB Tester software`. Ensure correct COM port is selected and press :guilabel:`connect`

    - The battery voltage should show up on the software and there should be a flashing rd light by the connect button. -PC- will show up on the EBC-A20

.. image:: /images/battery_connect.PNG
   :target: ../_images/battery_connect.PNG

- Select :guilabel:`cycle tab`. Select :guilabel:`Open` and open :download:`template_cycle.stp </files/template_cycle.stp>`

.. image:: /images/battery_template.PNG
   :target: ../_images/battery_template.PNG

- Select :guilabel:`Setting`. Select :guilabel:`Step 5` and change the current to `Discharge Current`_. Select :guilabel:`Ok`

    - If you have a small battery (>30AH) you will need to change the charge current.
      The max charge current is usually written on the battery or in the datasheet.
      Set :guilabel:`Step 1` and :guilabel:`Step 7`

.. image:: /images/battery_setting.PNG
   :target: ../_images/battery_setting.PNG

- Press :guilabel:`Start`

- Once finished note the capacity of the battery. Divide the tested capacity by the supposed capacity to get health.

    - Battery must be < 70% health to pass
    - Large batteries (<80Ah) with low health (50-70%) may be useful for testing electronics
    - Any thing less than 70% health has failed and can be scraped

- Use the appropriate label and note down the capacity, health, date, and name

Extras for experts
==================

- The cycle first bulk charges the battery to 14.1V then does a float charge to 13.8V.
  This ensures the battery is fully charged before the discharge test.
  After the discharge it starts to recharge the battery.
- The test can be stopped during the final charge stage if more batteries need to be charged.