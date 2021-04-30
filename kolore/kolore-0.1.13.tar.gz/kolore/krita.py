import kolore.palette as palette
import os
import shutil
import tempfile
import xml.dom.minidom as dom
import xml.etree.ElementTree as xml
import zipfile as zipf


def load_krita(path: str) -> [str]:
    with tempfile.TemporaryDirectory() as tmp_dir:
        with zipf.ZipFile(path, 'r') as zipObj:
            zipObj.extractall(tmp_dir)

            tree = xml.parse(f'{tmp_dir}/colorset.xml')
            root = tree.getroot()
            colors = []
            for child in root:
                rgb = child[0].attrib
                colors.append(palette.rgb_dict_to_rgb_tuple(rgb))

    return colors

def save_krita(width, height, colors: [str], path: str):
    root = xml.Element('ColorSet')
    root.set('readonly', 'false')
    root.set('version', '1.0')
    root.set('columns', f'{len(colors)}')
    root.set('rows', '1')
    root.set('name', f'{path}')
    for i, color in enumerate(colors):
        color_entry = xml.SubElement(root, 'ColorSetEntry')
        color_entry.set('spot', 'false')
        color_entry.set('bitdepth', 'U8')
        color_entry.set('name', f'Colour {i + 1}')
        color_entry.set('id', f'{i + 1}')

        rgb = xml.SubElement(color_entry, 'RGB')
        rgb.set('space', 'sRGB-elle-V2-srgbtrc.icc')
        rgb.set('g', f'{float(color.g):.15f}')
        rgb.set('r', f'{float(color.r):.15f}')
        rgb.set('b', f'{float(color.b):.15f}')

        pos = xml.SubElement(color_entry, 'Position')
        pos.set('column', f'{i}')
        pos.set('row', '0')
    
    with open(f'./kolore/resources/krita/colorset.xml', 'w') as f:
        f.write(prettify(root))
    
    shutil.make_archive(path, 'zip', './kolore/resources/krita/')
    os.rename(f"{path}.zip", path)

palette.loaders['krita'] = load_krita
palette.savers['krita'] = save_krita
palette.extension_checkers['krita'] = lambda f: f.endswith('.kpl')

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = xml.tostring(elem, 'utf-8')
    reparsed = dom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
