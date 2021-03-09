# Copyright PORTALSURFER, No rights reserved.
# https: //www.blender.org/about/license/

import bpy
import mathutils
import math

bl_info = {
    "name": "SnapperSnap",
    "author": "PORTALSURFER",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic"
}


class vector3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


def quantize(val, to_values):
    """Quantize a value with regards to a set of allowed values.

    Examples:
        quantize(49.513, [0, 45, 90]) -> 45
        quantize(43, [0, 10, 20, 30]) -> 30

    Note: function doesn't assume to_values to be sorted and
    iterates over all values (i.e. is rather slow).

    Args:
        val        The value to quantize
        to_values  The allowed values
    Returns:
        Closest value among allowed values.
    """
    best_match = None
    best_match_diff = None
    for other_val in to_values:
        diff = abs(other_val - val)
        if best_match is None or diff < best_match_diff:
            best_match = other_val
            best_match_diff = diff
    return best_match


class TOOL_OT_snapper_snap(bpy.types.Operator):
    """
    Snaps rotation to the nearest rounded value
    """
    bl_idname = "object.snapper_snap"
    bl_label = "Snap rotation values to neares rounded value"

    def execute(self, context):
        active = context.active_object

        rotation = vector3()
        rotation.x = math.degrees(context.active_object.rotation_euler.x)
        rotation.y = math.degrees(context.active_object.rotation_euler.y)
        rotation.z = math.degrees(context.active_object.rotation_euler.z)

        step = 15
        step_list = []
        target = 0
        while target <= 360:
            step_list.append(target)
            target += 15

        print(step_list)

        active.rotation_euler.x = math.radians(quantize(
            rotation.x, step_list))
        active.rotation_euler.y = math.radians(quantize(
            rotation.y, step_list))
        active.rotation_euler.z = math.radians(quantize(
            rotation.z, step_list))
        return {'FINISHED'}


def register():
    bpy.utils.register_class(TOOL_OT_snapper_snap)


def unregister():
    bpy.utils.unregister_class(TOOL_OT_snapper_snap)
