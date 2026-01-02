# J_Nuke_Tools

This is a small collection of Nuke tools I built as a compositor to speed up repetitive tasks and make node graph work more consistent. Most tools are lightweight "workflow helpers" (UI tabs, buttons, quick setups), written in Python and meant to live in a tools folder (such as `~/.nuke/python/`).

## Highlights
- **J_Tracker_Checkboxes** — Bulk-toggle Tracker4 Translate / Rotate / Scale checkboxes for `all tracks` or `selected tracks`
- **J_Transform_SetRemove_Keys** — Add "Set/Remove Keys" controls to Transform nodes
- **J_CornerPin_SetRemove_Keys** — Set/remove keys for CornerPin2D `to`/`from` knobs
- **J_Track_to_RotoPaint** — Create a RotoPaint node parented to a Tracker
- **Quick Setups** — One-click node graph templates (e.g., Roto→Grade, TransformMasked setups)
- **Channel Helpers** — Shuffle/ShuffleCopy utilities for organizing multi-layer EXRs

> Each tool is documented in its own folder README (when available).

## Install
1. Copy this repo (or the tool files you want) into your Nuke directory, e.g. `~/.nuke/J_Nuke_Tools/`.
2. In `~/.nuke/init.py`, add the repo to Nuke's plugin path: `nuke.pluginAddPath('J_Nuke_Tools')`.
3. In `~/.nuke/menu.py`, import the tools you want. For example, `import J_Tracker_Checkboxes`.
4. Restart Nuke.

## Tools
- [J_Tracker_Checkboxes](https://github.com/jazlyncartaya/J_Nuke_Tools/blob/master/J_Tracker_Checkboxes.py)
- [J_Transform_SetRemove_Keys](https://github.com/jazlyncartaya/J_Nuke_Tools/blob/master/J_SetRemoveAllTransformKeys.py)
- [J_CornerPin_SetRemove_Keys](https://github.com/jazlyncartaya/J_Nuke_Tools/blob/master/J_SetRemoveAllCornerPin2DKeys.py)
- [J_Track_to_RotoPaint](https://github.com/jazlyncartaya/J_Nuke_Tools/blob/master/J_TrackToRotoPaint.py)
- [J_Roto_Grade_Setup](https://github.com/jazlyncartaya/J_Nuke_Tools/blob/master/J_Tools/J_QuickSetups.py)
- [J_TransformMasked_Setup](https://github.com/jazlyncartaya/J_Nuke_Tools/blob/master/J_Tools/J_QuickSetups.py)
- [J_ShuffleCopy_Tool](https://github.com/jazlyncartaya/J_Nuke_Tools/blob/master/J_ShuffleCopyTool.py)
- [J_Shuffle_Node_Tool](https://github.com/jazlyncartaya/J_Nuke_Tools/blob/master/J_ShuffleNodeTool.py)

## Notes
- These tools were built for real shot work: speed, consistency, and fewer clicks.
- Code aims to be readable and easy to modify for different pipelines.

## License
MIT License
