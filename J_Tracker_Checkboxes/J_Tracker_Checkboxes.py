# J_Tracker_Checkboxes v.2.0.0
# Jazlyn Cartaya, 2026


import nuke


def tracker_checkboxes_tab():
    """This function creates a tab in the Tracker node that lets users
    choose which Tracker checkboxes, T (translate), R (rotate), and S (scale),
    to enable for all tracks or only the selected tracks."""

    # Define variables
    node = nuke.thisNode()

    # Check if UI has already been added
    if node.knob('check_tracker_boxes'):
        return

    # Create knobs
    tab = nuke.Tab_Knob('Check Boxes')
    
    scope_knob = nuke.Enumeration_Knob('scope',
                                       'apply to',
                                       ['all tracks', 'selected tracks'])
    scope_knob.setFlag(nuke.STARTLINE)

    
    t_boolean_knob = nuke.Boolean_Knob(
        'translate_box',
        'translate',
        True
        )
    t_boolean_knob.setFlag(nuke.STARTLINE)

    r_boolean_knob = nuke.Boolean_Knob(
        'rotate_box',
        'rotate',
        True
        )

    s_boolean_knob = nuke.Boolean_Knob(
        'scale_box',
        'scale',
        True
        )
    
    pyknob = nuke.PyScript_Knob(
        'check_tracker_boxes',
        'execute',
        'import nuke\nnuke.tracker_checkboxes()'
        )
    pyknob.setFlag(nuke.STARTLINE)

    # Add knobs
    node.addKnob(tab)
    node.addKnob(scope_knob)
    node.addKnob(t_boolean_knob)
    node.addKnob(r_boolean_knob)
    node.addKnob(s_boolean_knob)
    node.addKnob(pyknob)


nuke.addOnCreate(tracker_checkboxes_tab, nodeClass='Tracker4')


def tracker_checkboxes():
    """This function checks the T (translate), R (rotate), and S (scale)
    checkboxes in the Tracker node for all tracks or the selected tracks."""

    # Define variables
    node = nuke.thisNode()
    knob = node['tracks']
    num_columns = 31
    col_translate = 6
    col_rotate = 7
    col_scale = 8
    scope = node.knob('scope').value()
    selected_only = (scope == 'selected tracks')
    translate_knobvalue = bool(node.knob('translate_box').value())
    rotate_knobvalue = bool(node.knob('rotate_box').value())
    scale_knobvalue = bool(node.knob('scale_box').value())

    # Get number of tracks from toScript
    script = node['tracks'].toScript()
    total_tracks = script.count('\"track ')
    if total_tracks <= 0:
        nuke.message('No tracks found on this Tracker node.')
        return

    # Set T, R, and S for a specific track index
    def set_trs(track_index):
        if translate_knobvalue is True:
            knob.setValue(1, num_columns * track_index + col_translate)
        else:
            knob.setValue(0, num_columns * track_index + col_translate)

        if rotate_knobvalue is True:
            knob.setValue(1, num_columns * track_index + col_rotate)
        else:
            knob.setValue(0, num_columns * track_index + col_rotate)

        if scale_knobvalue is True:
            knob.setValue(1, num_columns * track_index + col_scale)
        else:
            knob.setValue(0, num_columns * track_index + col_scale)
            
    # Math = (True (1) or False (0), 31 columns * track number (0 to infinity)
    # + Translate (6), Rotate (7), or Scale (8))

    # One-step undo
    u = nuke.Undo()
    u.begin('Tracker4: Set T, R, and S checkboxes')
    try:
        
        # Selected tracks
        if selected_only:

            # Guard: selected_tracks API not available in this node/Nuke version 
            if not node.knob('selected_tracks'):
                nuke.message('This node does not have a knob called "selected_tracks".')
                return

            # Guard: no tracks selected in the Tracker UI
            sel = (node['selected_tracks'].value() or '').strip()
            if not sel:
                nuke.message('No tracks selected.')
                return

            # Guard: selected_tracks string couldn't be parsed into integers
            try:
                idxs = [int(x) for x in sel.split(',') if x.strip() != '']
            except ValueError:
                nuke.message('Could not parse selected track indices.')
                return

            # Guard: clamp to valid range of integers, avoid duplicates
            idxs = sorted(set(i for i in idxs if 0 <= i < total_tracks))
            if not idxs:
                nuke.message('No valid selected tracks found.')
                return

            # Apply checkbox settings to each selected track
            for i in idxs:
                set_trs(i)

            return

        # All tracks
        for i in range(total_tracks):
            set_trs(i)

    finally:
        u.end()


# Add function to nuke module so PyScript_Knob can call it
nuke.tracker_checkboxes = tracker_checkboxes
