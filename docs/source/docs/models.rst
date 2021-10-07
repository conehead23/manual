3D Modelling
============


CAD Software
------------
`Onshape <https://cad.onshape.com/signin>`_
    It a browser based parametric CAD modelling software. Cloud based CAD has many benefits.
    I now do most of my CAD in Onshape. It is better and cheaper

    - Rendering done server-side. Thus, no powerful computer needed
    - Editable from more locations. Don’t need to ‘install’ it on every device you use
    - Phone app to edit on the go or to show clients your models


SOLIDWORKS
    Many schools and universities (including Massey) teach 3D CAD design in SOLIDWORKS. SOLIDWORKS is a ‘jack of all trades” package with many features such as FEA analysis, sheet metal design, model rendering, circuit board design, and CAM. All my older work is in SOLIDWORKS Educational 2019-2020. Models made will only work in versions that are new than 2019.

    I would not recommend using SOLIDWORKS. Onshape has a much efficient/cleaner working environment and more powerful engine. SOLIDWORKS tends to crash computers, even high spec ones resulting in loss of data. The movement in assembly is poor when compared to Onshape. SOLIDWORKS cost money for a 1-year educational licence whereas Onshape have a free account.

    SolidWorks have created a cloud-based CAD program called `3D Creator <https://www.solidworks.com/product/3d-creator>`_. Cost is USD$1680 not including tax, it doesn’t have a free version.

`OpenSCAD <https://openscad.org/downloads.html>`_
    OpenSCAD is a 3D modelling software based on writing code.
    This is good for developing parametric models where options can be changed such as a `universal bolt maker <https://www.thingiverse.com/thing:193647>`_ or formula based mathematical models like `globoid worm gear drive <https://www.thingiverse.com/thing:2776688>`_.
	
    There are a few models on Thingiverse that have an OpenSCAD model so you can make custom designs. OpenSCAD is suited for advanced users.

`Meshmixer <https://www.meshmixer.com/download.html>`_
    Meshmixer is a free mesh editor used to edit files such as STL and OBJ. This program is useful for editing STL that are ‘broken’ or need simple edits such as increasing the thickness of a surface. It is good for editing ‘natural’ models like people or animals with lots of curves and has a sculpting mode. 


Modelling for 3D Printing
-------------------------
3D printers work by adding layer successive layers on top of each other. When modelling keep in mind the orientation of your print and how the print will be supported as it prints. A decent rule of thumb is the printer will be able to print up to 45° overhangs. This can increase to 70° for short runs. The printer can print short ‘bridges’ without issue.

Sometimes large overhangs are unavoidable. Removable supports can be added in the slicing software to support the overhangs. When designing ensure there is enough space to remove a support from the model as it will make clean-up much easier.

The minimum thickness of a part on a model needs to be 0.5mm otherwise it will not print. This is due to the nozzle which has a 0.45mm extrusion width.

Models can be split apart and reassembled after printing. This is good for large objects or round/spherical objects


Design Libraries
----------------
Before going through the effort of designing from scratch, check out a few of these websites.

`Thingiverse <https://www.thingiverse.com/>`_
    Most popular library for all your 3D designs.

`Prusa Printers <https://www.prusaprinters.org/>`_
    Optimized for Prusa printers. Library is not as extensive as Thingiverse.

`GrabCAD <https://grabcad.com/library>`_
    Designed for CAD software thus the files are mostly editable formats such as STEP.
    These can be converted to STL/OBJ using Onshape

