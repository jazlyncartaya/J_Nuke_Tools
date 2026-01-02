# J_AttachNodes Tool 1.0
# Copyright (c) 2018 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke
# J_AttachNodes Menu
#nuke.menu('Nuke').addCommand('J_AttachNodes/Attach Nodes',
                             #'attach_nodes()',
                             #'ctrl+alt+a')

def attach_nodes():
    """This tool lets the artist select any node in their node graph,
    and attach any node, of the same node, with one of the knobs adjusted,
    to the selected nodes."""

    # Panel (1): Asks for name of the node you would like to attach.

    panel = nuke.Panel('J_AttachNodes')
    panel.addSingleLineInput('Node to attach:', '')
    ret = panel.show()
    if not ret:
        pass

    node_name = panel.value('Node to attach:')
    print node_name

    # List to keep track of nodes:
    desired_nodes = []

        # Attach Node(s):

    try:
        selected = nuke.selectedNodes()
        # Clear user's selection:
        [node.setSelected(False) for node in selected] # Why is this say
	                                               # it is assigned
						       # to nothing?
        for node in selected:
            # Select node so createNode correctly inserts it:
            node.setSelected(True)
            desired_node = nuke.createNode(node_name)
            desired_nodes.append(desired_node)

            """Now deselect selected node,
                        and corresponding desired node.
                        This will ensure the next nodes
                        are properly connected."""
            node.setSelected(False)
            desired_node.setSelected(False)
    except RuntimeError:
        pass

    # Panel (2): Asks the knob name of node,
               # and number value you would like to set.

    try:
        selected_knob = None
        knobs = desired_node.knobs().keys()
        knobs.sort(key=str.lower) # Sort knobs into alphabetical order.

        panel = nuke.Panel('Knob')
        panel.addEnumerationPulldown('Knob (optional):', ' '.join(knobs))
        panel.addSingleLineInput('Number Value (optional):', 0)
        ret = panel.show()
        if not ret:
            pass
        selected_knob = panel.value('Knob (optional):')
        print selected_knob

        input_amount = panel.value('Number Value (optional):')
        print input_amount
    except UnboundLocalError:
        pass

    # Change the knob(s) of x attached node(s) to y input value:
    # Loop through newly created nodes:
    for node in desired_nodes:
        try:
            #nuke.selectedNode().knob(selectedKnob).setValue(int(inputAmount))
            # Node refers to current node in the list.
            node.knob(selected_knob).setValue(int(input_amount))
        except ValueError:
            print nuke.message('The value you entered was not a number.'
                               ' Please enter a number value.')
        except TypeError:
            nuke.message('The knob you selected does not take a number value.'
                         ' Please select a knob that takes a number value.')
            break
