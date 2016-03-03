test_internal = [3366,1485,3351,1482,1767,1767,1814,1479,1767,1767]
test_external = [1479,1479,1479,1477,1483]

internal_count = 0
external_count = 0
with open('COG0001.aligned.jplace') as jplace_file:
    jplace_handle = json.load(jplace_file)
    placements = jplace_handle['placements']
    for placement in placements: #it works, but I am guessing there is a more efficient way to dig deep into a dictionary
        placement_values = placement.values()
        placement_fields = placement_values[0]
        placement_field_values = placement_fields[0]
        placement_edge = placement_field_values[2]
        if placement_edge in test_internal:
            internal_count += 1
        elif placement_edge in test_external:
            external_count += 1
    print(internal_count)
    print(external_count)
