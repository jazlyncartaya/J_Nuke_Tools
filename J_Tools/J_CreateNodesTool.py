# J_CreateNodes Tool 1.0
# Copyright (c) 2018 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke
# J_CreateNodes Menu
#nuke.menu('Nuke').addCommand('J_CreateNodes/Create Nodes',
                             #'create_nodes()',
                             #'ctrl+alt+c')

def create_nodes():
    """This tool lets the artist create as many nodes,
    of the same node, as they want,
    with one of the knobs adjusted in those nodes."""

    # Panel 1: Asks for node name and node amount.

    panel = nuke.Panel('J_CreateNodes')
    panel.addSingleLineInput('Amount of Nodes:', '')
    panel.addSingleLineInput('Node:', '')
    ret = panel.show()
    if not ret:
        pass

    node_amount = panel.value('Amount of Nodes:')
    print node_amount

    node_name = panel.value('Node:')
    print node_name

    # List to keep track of created nodes:
    created_nodes_list = []

    # Create Nodes
    try:
        for node in range(0, int(node_amount)):
            created_nodes = nuke.createNode(node_name)
            created_nodes_list.append(created_nodes)
    except ValueError:
        pass

    # Panel 2: Asks for knob name and input amount.

    selected_knob = None
    knobs = nuke.selectedNode().knobs().keys()
    knobs.sort(key=str.lower) # Sort knobs into alphabetical order.

    panel = nuke.Panel('Knob Input')
    panel.addEnumerationPulldown('Knob (optional):', ' '.join(knobs))
    panel.addSingleLineInput('Input (optional):', 0)
    ret = panel.show()

    selected_knob = panel.value('Knob (optional):')
    print selected_knob

    input_amount = panel.value('Input (optional):')
    print input_amount

    # Set x node(s), at y value.
    try:
        for node in created_nodes_list:
            node.knob(selected_knob).setValue(int(input_amount))

    except TypeError:
        nuke.message(
            ' The knob you selected does not take a number value.'
            ' Please select a knob that takes a number value.'
            )

    except ValueError:
        nuke.message(
            ' You must type a number value'
            ' into the Input section.'
            )
