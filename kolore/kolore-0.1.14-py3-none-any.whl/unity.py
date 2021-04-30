import kolore.palette as palette
import sys
import yaml


def unity_yaml_loader(loader, node) -> [palette.RGBA]:
    stuff = loader.construct_mapping(node.value[0][1], deep=True)
    colors = []
    for color_entry in stuff['m_Presets']:
        rgba = color_entry['m_Color']
        colors.append(palette.rgb_dict_to_tuple(rgba))

    return colors

yaml.add_constructor('tag:unity3d.com,2011:114', unity_yaml_loader)

def load_unity(filepath: str) -> [palette.RGBA]:
    with open(filepath) as file:
        colors = yaml.load(file, Loader=yaml.FullLoader)

    return colors

palette.loaders['unity'] = load_unity

def unity_yaml_dumper(dumper, palette):
    color_entries = []
    for color in palette.colors:
        d = {}
        d['r'] = color.r
        d['g'] = color.g
        d['b'] = color.b
        d['a'] = color.a
        color_entries.append({'m_Name': '', 'm_Color': d})
    d = {
        'MonoBehaviour': {
            'm_ObjectHideFlags': 52,
            'm_CorrespondingSourceObject': {'fileID': 0},
            'm_PrefabInstance': {'fileID': 0},
            'm_PrefabAsset': {'fileID': 0},
            'm_GameObject': {'fileID': 0},
            'm_Enabled': 1,
            'm_EditorHideFlags': 0,
            'm_Script': {'fileID': 12323, 'guid': '0000000000000000e000000000000000', 'type': 0},
            'm_Name': 'Name',
            'm_EditorClassIdentifier': '',
            'm_Presets': color_entries
        }
    }
    return dumper.represent_mapping('tag:unity3d.com,2011:114', d)

yaml.add_representer(palette.Palette, unity_yaml_dumper)

def save_unity(width, height, data, filepath):
    with open(filepath, 'w') as file:
        file.write('%YAML 1.1\n')
        file.write('%TAG !u! tag:unity3d.com,2011:\n')
        file.write('--- !u!114 &1\n')
        yaml_str = yaml.dump(palette.Palette(data))
        file.write("\n".join(yaml_str.split("\n")[1:]))

palette.savers['unity'] = save_unity

palette.extension_checkers['unity'] = lambda f: f.endswith('.colors')
