import bpy
import math

# Get all selected objects
selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    # Rotate by 180 degrees around the local Z axis
    # Using the object's rotation_mode and applying rotation to local space
    obj.rotation_euler.rotate_axis('Z', math.radians(180))
    print(f"Rotated {obj.name} by 180 degrees around local Z axis")
    
    # Find Simple Deform modifier and negate its angle
    for modifier in obj.modifiers:
        if modifier.type == 'SIMPLE_DEFORM':
            # Multiply angle by -1
            modifier.angle *= -1
            print(f"Found Simple Deform modifier '{modifier.name}' on {obj.name}")
            print(f"  New angle value: {modifier.angle}")
            break  # Remove this if you want to process multiple Simple Deform modifiers
    else:
        print(f"No Simple Deform modifier found on {obj.name}")

print("Done!")
