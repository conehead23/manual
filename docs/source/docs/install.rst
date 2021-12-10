=======
Install
=======

Things you’ll need
==================

•	Your laptop
•	Poco Program
•	Clearscada program
•	Point orange unit, pulse cable, aerial, programing cable, mount, wire joiners

Point Orange Setup
==================

1.	Check cell reception and install sim card with best reception (note IP address)
2.	Configure point orange in Poco
3.	Upload a template that suits application (e.g. Spark,Vodafone,double meter)
4.	Assign point orange an outstation from (coms reporter) excel spreadsheet
5.	Upgrade firmware in the device tab and choose latest file
6.	Add device ID (ATH) and device location (site name e.g. smith dairy farm)
7.	Download configuration to point orange and wait for it to call in using the call progress tab (wifi logo)
8.	Once its called in to the cloud logo go to file and save as the device ID and device location into the metasphere folder
9.	Install point orange to flow meter and take photos (meter serial number, point orange serial number)
10.	Go to monitor points tab (chart logo) and scroll down to CIO, if water is pumping you should see some pluses coming through if not pumping put meter into simulation mode and test the pulse output, some meters won’t have a simulation mode, in this case you will have to monitor from clearscada at a later stage and see if its received a pulse.
11.	Point orange is all setup and should be good to go.

CLEARSCADA
==========

We need to set up a site in ClearSCADA for the point orange to put all its data.

- Remote into ClearSCADA server. Logon with your standard logon. Open ViewX

    - Download the :download:`ClearSCADA.rdp </files/ClearSCADA.rdp>`.
    - Computer: pnt-ap37.horizons.govt.nz
      Username: servers

.. image:: /images/clearSCADA_rdp.PNG
   :target: ../_images/clearSCADA_rdp.PNG

- Select :guilabel:`Server (PNT-AP37)` > :guilabel:`Sites` > :guilabel:`Water Metering`
- Right click on :guilabel:`Water Metering` and select :guilabel:`Create Instance`

.. image:: /images/clearSCADA_instance.PNG
   :target: ../_images/clearSCADA_instance.PNG

- Select :guilabel:`Point Orange Water Meter FM1`. If you have more than one flow meter connected to the point orange select :guilabel:`FM2` or :guilabel:`FM3`

.. image:: /images/clearSCADA_template.PNG
   :target: ../_images/clearSCADA_template.PNG

- Right click :guilabel:`New Group Instance` and rename to the site with ATH number

.. image:: /images/clearSCADA_new.PNG
   :target: ../_images/clearSCADA_new.PNG

- Select :guilabel:`+` and double click :guilabel:`Outstation`
- In the address box in the DNP3 tab, write the Device ID

.. image:: /images/clearSCADA_deviceID.PNG
   :target: ../_images/clearSCADA_deviceID.PNG

- Right click your site and select :guilabel:`Edit properties`
- Select :guilabel:`Location` tab. Select the :guilabel:`...` and enter the Lat and Long. This can be gotten from BaseMaps or IRIS

+--------------------------------------------------+------------------------------------------------+
| .. image:: /images/clearSCADA_properties.PNG     | .. image::/images/clearSCADA_location.PNG      |
|    :target: ../_images/clearSCADA_properties.PNG |    :target: ../_images/clearSCADA_location.PNG |
+--------------------------------------------------+------------------------------------------------+

- Right click your site and select :guilabel:`Notes`
- Write down the IP address of the SIM card installed in the point orange

.. image:: /images/clearSCADA_notes.PNG
   :target: ../_images/clearSCADA_notes.PNG

- Go to the top left and click save (above the file tab)

.. image:: /images/clearSCADA_save.PNG
   :target: ../_images/clearSCADA_save.PNG

HAZZAH you have setup ClearSCADA, have a free 10 points

OTHER THINGS TO DO
==================

1.	Update outstation spread sheet with site details and IP address
2.	Move point orange in assets to the site (if you’ve replaced an old logger write it off)
