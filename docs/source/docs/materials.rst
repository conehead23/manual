Materials
===============
There are many 3D printing filaments that can be used in 3D printing. 
At Horizons we mainly use PETG due to its water resistance properties. 
PLA is suitable for prototyping and indoor models due to its affordable price and ease of print. 
FLEX filament can make almost indestructible prints due to its mechanical properties. 
We also have a composite of 75% PETG and 25% Carbon fibre filament which is useful for models which require extra stiffness. 

.. csv-table:: Manny Tested Filaments
    :file: /files/filament table.csv
    :header-rows: 1
    :stub-columns: 2

:note: Ensure you are purchasing ø1.75mm filament.

PLA/PLA+
------------------
PLA is the most popular 3D printing filament. 
It is biodegradable, easy to print with, and has stiff mechanical properties. 
It has low thermal expansion thus prints do not warp on the heatbed making it ideal for large/long prints. 
It is the only material that is well suited for printing 0.05mm layers (Ultradetail resolution) thus is ideal for small, detailed models.

When post-processing PLA, use wet sanding. The friction from sanding heats the plastic causing it to melt thus making it hard to continue sanding. This is due to its low tempurature resistance.

When connecting multiple pieces, one should use superglue or plastic welding with a soldering iron.

Typical Use
    - Prototypes, used all through Massey
    - Toys
    - Figures
    - Jewellery
    - Models

.. list-table::
    :header-rows: 1

    *   - Advantages
        - Disadvantages
    *   - Easy to print
        - Brittle
    *   - Detailed prints of small models
        - Low-temperature resistance ≈ 60°C
    *   - Trouble-free printing of large objects
        - Can warp in direct sunlight
    *   - Stiff, low flexibility
        - Not suitable for outdoor use
    *   - Almost odourless
        - Difficult to post-process
    *   - Affordable, cheapest filament available
        -
    *   - Wide colour selection
        -
    *   - Low Stringing
        -
		
Reference
	- `Prusa PLA article <https://help.prusa3d.com/en/article/pla_2062>`_


PET/PETG
--------
It is a great choice for printing mechanical components. Compared to PLA, it has higher temperature resistance, is more ductile and therefore less brittle. Due to its low thermal expansion, it holds well on the heatbed and does not warp. Printing with it is almost as easy as with PLA. But unlike PLA, it can offer better mechanical properties. Parts for the printer are printed from PETG.

Unlike PLA or ABS, PETG tends to ooze a bit and may leave strings of plastic on your print. You can get rid of it by quickly blasting your finished prints with a heat gun. If stringing is bad, refer to SECTION. .

PETG is often referred to simply as PET. The G in PETG stands for glycol, this is added to improve the flow of the filament when in liquid form. Generally, they’re almost the same material (you can even get pure PET filament, but it’s difficult to print with)

Typical Use
    - Mechanical components
    - Holders and cases
    - Watertight prints

.. list-table::
    :header-rows: 1

    *   - Advantages
        - Disadvantages
    *   - High-temperature resistance
        - Not suitable for printing small models
    *   - Easy to print
        - Possible stringing
    *   - Low thermal expansion
        - Bridging is problematic
    *   - Ductility and strength
        - Supports can be difficult to remove
    *   - Strong adhesion to the printbed
        - Can strip PEI off printbed
    *   - Almost odourless
        -
    *   - Glossy surface
        -
    *   - Perfect layer adhesion
        -
    *   - Water and humidity resistant
        -
    *   - Recyclable
        -
    *   - Food Safe, used in bottles
        -

Reference
	- `Prusa PETG article <https://help.prusa3d.com/en/article/petg_2059>`_


Flex/TPU
----------
Flex is a very strong and elastic material. In many cases, classic hard plastics may not be suitable for printing a specific model. It has the strongest layer adhesion of any filament resulting in near indestructible prints. This property makes it hard to remove prints from the heatbed and remove supports. When designing for FLEX filament avoid large overhangs and supports. There can also be a high amount of stringing so avoid prints that have multiple retractions.

Before you print from Flex, clean the nozzle from any previous material. When inserting Flex, loosen the pressure on the idler as much as possible. Flex adheres very strongly to the smooth PEI sheet and require the use of a glue stick as a separator to avoid damaging the PEI surface. This is not necessary with the textured powder-coated PEI.

Typical Uses
    - Phone cover
    - RS5 barge fins
    - RC car wheel

.. list-table::
    :header-rows: 1

    *   - Advantages
        - Disadvantages
    *   - Flexibility and elasticity
        - Extra steps to load filament
    *   - Minimal warping
        - Must be printed slowly
    *   - Good layer adhesion
        - High price
    *   - High abrasion resistance
        - Needs to be stored in dry environment
    *   - Generally strong, can absorb lots of force
        - High stringing
    *   - From initial testing, waterproof
        - Supports hard to remove

Reference
	- `Prusa TPU article <https://help.prusa3d.com/en/article/flexible-materials_2057>`_


Composite Materials
---------------------------------------
Composite materials (corkfill, copperfill, bronzefill, carbon or aramid composites and many others) are based on the main plastic medium and second material in the form of dust. These materials are very abrasive, so if you plan to print them long term, we recommend using a hardened nozzle. When using wood composites, we recommend larger nozzles (0.5 mm and larger). The printing characteristics of each material may vary depending on the plastic base, so use the appropriate print settings in the PrusaSlicer.

The first step of polishing is sanding with sandpaper. It’s better to start with a coarse one (80) and use finer and finer sandpaper. You can then sand the model with a brass brush. If you are still not satisfied with the polish of the material, you can finally use the wet sanding method with very fine sandpaper (1500+).

Wood filaments can be post-processed like a piece of wood (sanded/stained). The PETG+Carbon composite is much stiffer compared to regular PETG. Glow in the dark PLA filament from Jaycar works well for special models. All these filaments absorb moisture quickly which can result in stringing and print failures. Ensure it is stored in a dry storage box. DEHYDRATING the filament before use will remove moisture in the filament resulting in better prints. Unless you have a particular project in mind, would recommend not using them.

.. list-table::
    :header-rows: 1

    *   - Advantages
        - Disadvantages
    *   - Unique aesthetics
        - Requires hardened nozzle
    *   - Best of both worlds
        - Expensive
    *   -
        - Usually harder to print
    *   -
        - Sensitive to moisture


ASA/ABS
-------
ASA/ABS is a strong and versatile material. 
It has excellent heat resistance, your prints will not show signs of deformation up to around 100°C. 

It has a very high thermal expansion compared to PLA, which complicates printing, especially for larger models. 
Even with a heated bed set to 100 °C, the print can begin to warp and peel off the bed. 
It produces and unpleasant odour during printing, it is not recommended to work in the same environment when printing.

To mitigate these issues one should print ASA/ABS inside an enclosure. 
The heated bed will quickly heat the enclosure and reduce the thermal shock on the extruded filament. 
As a result, both warping and layer separation is decreased significantly. 

ASA and ABS are very similar materials. 
ASA has better UV stability compared to ABS (less yellowing) and shrinks less when printed. 
ABS responds better to surface treatment with acetone.

Acetone is a solvent for ASA/ABS. 
It can be used to join prints, applyed in a similar manner to superglue. 
This creates a strong bond as the acetone melts the parts together.
A acetone VAPOUR CHAMBER can be used to improve the strength of the print and gives a glossy finish.   
When in the chamber, the acetone vapours permiate through and remelt the print. 
This improves the layer adhesion of the print and can completely remove the print layer lines resulting in a smooth print. 
Read more about chemical smoothing in this `Prusa article. <https://blog.prusaprinters.org/improve-your-3d-prints-with-chemical-smoothing_36268/>`_

My experience with ABS is that it is too difficult to print compared to PETG. 
PETG offers similar mechanical properties and is also suitable for outdoor environments. 
It could be revisited in the future if a print is exposed to full sun or hot temperatures. 
A printing enclosure would also need to be purchased to get good ASA/ABS prints

Typical use
    - Outdoor covers and protective cases
    - Replacement parts

.. list-table::
    :header-rows: 1

    *   - Advantages
        - Disadvantages
    *   - High impact and wear resistance
        - Needs printing enclosure
    *   - Very good temperature resistance
        - Tendency to warp during printing
    *   - Suitable for outdoor use - UV stable
        - Unpleasant odour during printing
    *   - Soluble in acetone - easy to glue together
        - Difficult to print
    *   - Can be smoothed with acetone vapours
        -
    *   - Cheap
        -

Reference
	- `Prusa ABS article <https://help.prusa3d.com/en/article/abs_2058>`_


Nylon
-----
Nylon is a very strong, ductile and versatile material making it suitable for mechanical components. 
It is flexible in thin layers but with very good layer adhesion. 
Nylon must be stored in a dry environment otherwise it quickly absorbs air humidity and bubbles form in the material. 
This results in failed prints.
To get perfect prints it is recommended the filament is dried in a DEHYDRATOR before printing
Dry nylon filament prints smooth objects with a glossy finish.

`Hartley Engines <https://www.facebook.com/HartleyEngines/>`_ can print in Nylon and Nylon+Carbon blends if Nylon is needed for a project. 
This is a pricey option so be sure of your print. 

Typical use
	- Mechanical parts
	- Screws, nuts
	- Gearboxes
	- Exhaust Manifolds

.. list-table::
    :header-rows: 1

    *   - Advantages
        - Disadvantages
    *   - Godd mechanical properties
        - Must be stored in dry environment
    *   - Good chemical resistance
        - Needs printing enclosure
    *   - Flexible, but strong
        - Difficult to print

Reference
	- `Prusa <https://help.prusa3d.com/en/article/nylon_167188>`_


Others
------
There are many other flavours of filament with many advantages and disadvantages. I would recommend sticking to the ones mentioned
If you would like more information on other filaments first read the filament the section in `Prusa3D Manual <https://help.prusa3d.com/en/materials>`_.
