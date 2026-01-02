# J_QuickSetups
# Copyright (c) 2018 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke

    # Create Roto Setup quickly:

def roto_grade_setup():
    """This function creates a Roto and Grade node setup quickly:
    A Grade node with the mask input connected to a Roto node."""

    # Create Nodes:
    selected = nuke.selectedNodes()
    [node.setSelected(False) for node in selected]
    for node in selected:

        node.setSelected(True)
        grade = nuke.createNode('Grade')

        node.setSelected(False)
        grade.setSelected(False)

    if not selected:
        grade = nuke.createNode('Grade')

    roto = nuke.createNode('Roto')

    # List to keep track of created nodes:
    try:
        created_nodes = [roto, grade]

        # Arrange Nodes:

        # Assign a variable to X and Y positions:
        grade_x_position = nuke.Node.xpos(grade)
        grade_y_position = nuke.Node.ypos(grade)
        print nuke.Node.xpos(grade)
        print nuke.Node.ypos(grade)

        # Offset X and Y positions of Roto node:
        roto.setXpos(grade_x_position + -110)
        roto.setYpos(grade_y_position + -6)

        # Select Nodes:
        for node in created_nodes:
            node.setSelected(True)

        # Detach Nodes:
        roto.setInput(0, None)

        # Connect Nodes:
        grade.setInput(1, roto)
    except UnboundLocalError:
        pass

    # Create TransformMasked Setup quickly:

def transformmasked_setup():
    """This function creates a TransformMasked setup quickly:
    A TransFormMasked node
    with the mask input connected to a Blur and Roto node."""

    # Create Nodes:
    selected = nuke.selectedNodes()
    [node.setSelected(False) for node in selected]
    for node in selected:

        node.setSelected(True)
        transformmasked = nuke.createNode('TransformMasked')

        node.setSelected(False)
        transformmasked.setSelected(False)

    if not selected:
        transformmasked = nuke.createNode('TransformMasked')

    blur = nuke.createNode('Blur')
    roto = nuke.createNode('Roto')

        # List to keep track of created nodes:
    try:
        created_nodes = [blur, roto, transformmasked]

        # Arrange Nodes:

        # Assign a variable to X and Y positions:
        transformmasked_x_position = nuke.Node.xpos(transformmasked)
        transformmasked_y_position = nuke.Node.ypos(transformmasked)
        print nuke.Node.xpos(transformmasked)
        print nuke.Node.ypos(transformmasked)

	# Offset X and Y positions of Blur and Roto nodes:
        blur.setXpos(transformmasked_x_position + -110)
        roto.setXpos(transformmasked_x_position + -110)
        blur.setYpos(transformmasked_y_position + 6)
        roto.setYpos(transformmasked_y_position + -32)

        # Select Nodes:
        for node in created_nodes:
            node.setSelected(True)

        # Detach Nodes:
        roto.setInput(0, None)

        # Connect Nodes:
        blur.setInput(0, roto)
        transformmasked.setInput(1, blur)
    except UnboundLocalError:
        pass
