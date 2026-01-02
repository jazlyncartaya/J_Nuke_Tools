# J_SetAllTransformKeys Button 1.0
# Copyright (c) 2018 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke

    # Creates button that sets keys in all knobs in "Transform":

def set_all_transform_keys():
    """This function sets all of the keys in all of the knobs
    in the Transform node."""

    this_node = nuke.thisNode()
    frame_number = nuke.frame()

    # "Transform" Knob: Translate

    translate_knob = this_node['translate']
    translate_knob.splitView('right')

    input_amount_translate = this_node.knob('translate').value()
    # --> this is returns a list [valX, valY]
    print input_amount_translate

    translate_knob.setAnimated(view='right')
    translate_knob.setValue(input_amount_translate)

    # "Transform" Knob: Rotate

    rotate_knob = this_node['rotate']

    input_amount_rotate = this_node.knob('rotate').value()
    print input_amount_rotate

    rotate_knob.setAnimated(0)
    rotate_knob_an = this_node['rotate'].animations()[0]
    rotate_knob_an.setKey(int(frame_number), float(input_amount_rotate))

    # "Transform" Knob: Scale

    scale_knob = this_node['scale']
    scale_knob.splitView('right')

    input_amount_scale = this_node.knob('scale').value()
    print input_amount_scale

    scale_knob.setAnimated(view='right')
    scale_knob.setValue(input_amount_scale)

    # "Transform" Knob: Skew X

    skew_x_knob = this_node['skewX']

    input_amount_skew_x = this_node.knob('skewX').value()
    print input_amount_skew_x

    skew_x_knob.setAnimated(0)
    skew_x_knob_an = this_node['skewX'].animations()[0]
    skew_x_knob_an.setKey(int(frame_number), float(input_amount_skew_x))

    # "Transform" Knob: Skew Y

    skew_y_knob = this_node['skewY']

    input_amount_skew_y = this_node.knob('skewY').value()
    print input_amount_skew_y

    skew_y_knob.setAnimated(0)
    skew_y_knob_an = this_node['skewY'].animations()[0]
    skew_y_knob_an.setKey(int(frame_number), float(input_amount_skew_y))

    # "Transform" Knob: Center

    center_knob = this_node['center']
    center_knob.splitView('right')

    input_amount_center = this_node.knob('center').value()
    print input_amount_center

    center_knob.setAnimated(view='right')
    center_knob.setValue(input_amount_center)

def set_keys_in_knobs():
    """This function creates a button in Transform node
    which executes the set_all_transform_keys() function."""

    pyknob = nuke.PyScript_Knob('set_all_transform_keys',
                                'set all keys',
                                'set_all_transform_keys()')
    node = nuke.thisNode()
    node.addKnob(pyknob)

nuke.addOnCreate(lambda: set_keys_in_knobs(), nodeClass='Transform')
