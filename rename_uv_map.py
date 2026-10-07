import bpy

# Specify the new UV map name here
new_uv_name = "UVMap"

# Get all selected objects
selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    # Only process mesh objects
    if obj.type != 'MESH':
        print(f"Skipping {obj.name} (not a mesh)")
        continue
    
    # Get the UV layers
    uv_layers = obj.data.uv_layers
    
    if len(uv_layers) == 0:
        print(f"No UV maps found on {obj.name}")
        continue
    
    # Rename the first UV map to the specified name
    old_name = uv_layers[0].name
    uv_layers[0].name = new_uv_name
    print(f"Renamed UV map on {obj.name}: '{old_name}' -> '{new_uv_name}'")

print("Done!")
