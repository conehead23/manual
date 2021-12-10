===============
Battery Testing
===============

We are doing a full discharge test on the batteries to see how much capacity it will have in the field.
This is compared to the supposed capacity which gives us the battery health.

First step is to find the discharge current of the battery.
The best way is to find the battery datasheet online and find the 10h or 20h capacity.
Sometimes this can be calculated from the battery for example:

- 100AH Capacity over 20 Hr = 100/20 = 5A discharge rate

Ensure you have the correct rate or else one cannot compare capacity to get the battery health

EBC-A20 Battery Analyser
========================

- Turn on the computer and EBC-A20
- Connect the leads to the battery
- Open the software. Press connect. Select the Cycle Test tab
- Select open and select the template
- Select edit. Select Step 5 and change the discharge rate. Select ok
- Press start.

- Once finished note the capacity of the battery. Divide the tested capacity by the supposed capacity to get health.

    - Battery must be < 70% health to pass
    - Large batteries (<80Ah) with low health (50-70%) may be useful for testing electronics
    - Any thing less than 70% health has failed and can be scraped

- Use the appropriate label and note down the capacity, health, date, and name
