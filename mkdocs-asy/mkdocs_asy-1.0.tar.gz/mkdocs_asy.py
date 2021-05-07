"""
Asymptote extension for Markdown (e.g. for mkdocs) :
Renders the output inline, eliminating the need to configure an output
directory.

Supports outputs types of SVG and PNG. The output will be taken from the
filename specified in the tag, if given, or. Example:

in SVG:

```asy
import math;

size(6cm,0);

add(grid(6,5,lightgray));

pair pA=(1,1), pB=(5,1), pC=(4,4);
 
draw(pA--pB--pC--cycle);
dot("$A$",pA,dir(pC--pA,pB--pA));  
dot("$B$",pB,dir(pC--pB,pA--pB));  
dot("$C$",pC,dir(pA--pC,pB--pC));
```

```asy svg
import math;

size(6cm,0);

add(grid(6,5,lightgray));

pair pA=(1,1), pB=(5,1), pC=(4,4);
 
draw(pA--pB--pC--cycle);
dot("$A$",pA,dir(pC--pA,pB--pA));  
dot("$B$",pB,dir(pC--pB,pA--pB));  
dot("$C$",pC,dir(pA--pC,pB--pC));
```

in PNG:

```asy png
import math;

size(6cm,0);

add(grid(6,5,lightgray));

pair pA=(1,1), pB=(5,1), pC=(4,4);
 
draw(pA--pB--pC--cycle);
dot("$A$",pA,dir(pC--pA,pB--pA));  
dot("$B$",pB,dir(pC--pB,pA--pB));  
dot("$C$",pC,dir(pA--pC,pB--pC));
```

Requires the Asymptote library (https://asymptote.sourceforge.io/) and python 3

[Rodrigo SCHWENCKE > mkdocs-graphviz](https://gitlab.com/rodrigo.schwencke/mkdocs-graphviz)
"""

import os
import re
import markdown
import subprocess
import base64
import shlex

# Global vars
BLOCK_RE_GRAVE_ACCENT_ASY_FILENAME = re.compile(
        r'^[ 	]*```asy[\s]+(?P<filename>[^\s]+)\s*\n(?P<content>.*?)```\s*$',
    re.MULTILINE | re.DOTALL)

BLOCK_RE_GRAVE_ACCENT_ASY = re.compile(
        r'^[ 	]*```asy\n(?P<content>.*?)```\s*$',
    re.MULTILINE | re.DOTALL)

ASY_COMMAND_FILENAME = 0
ASY_COMMAND_ALONE = 1

class MkdocsAsyExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        """ Add MkdocsAsyPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.add('asy_block',
                             MkdocsAsyPreprocessor(md),
                             "_begin")


class MkdocsAsyPreprocessor(markdown.preprocessors.Preprocessor):

    def __init__(self, md):
        super(MkdocsAsyPreprocessor, self).__init__(md)

    def read_block(self, text:str)->(str, int) or (None, -1):
        """Returns a tuple:
        - the asy block, if exists, and
        - a code integer to caracterize the command : 
            0 for 'asy' command,
            1 for 'asy svg' command,
            2 for 'asy png' command)
        or (None, -1), if not a recognised asy command block"""
        blocks = [BLOCK_RE_GRAVE_ACCENT_ASY_FILENAME.search(text),
                  BLOCK_RE_GRAVE_ACCENT_ASY.search(text)]
        for i in range(len(blocks)):
            if blocks[i] is not None:
                return blocks[i], i
        return None, -1

    def get_decalage(self, command:str, text:str)->int:
        """Renvoie le décalage (nombre d'espaces) où commencent les ``` dans la ligne ```command ...
        Cela suppose que le 'text' réellement la commande, ce qui est censé être le cas lors de l'utilisation de cette fonction
        """
        # command = 'asy' or 'asy filename.svg' or 'filename.png'
        i_command = text.find("```"+command)
        i_previous_linefeed = text[:i_command].rfind("\n")
        decalage = i_command - i_previous_linefeed-1
        return decalage

    def to_file(self, content:str,filename:str):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    def run(self, lines):
        """ Match and generate asy code blocks."""

        text = "\n".join(lines)
        while 1:
            m, block_type = self.read_block(text)
            if not m:
                break
            else:
                if block_type == ASY_COMMAND_FILENAME: # General Asy command with filename
                    filename = m.group('filename')
                    command = f"asy {filename}"
                else: # ASY command alone
                    command = "asy"
                    path = ""
                    filename = "noname.svg"

                decalage=self.get_decalage(command, text)
                filetype = filename[filename.rfind('.')+1:]
                content = m.group('content')

                self.to_file(content, filename[:-4]+".asy")

                totalCommand = f"asy -f {filetype} {filename[:-4]}.asy >&0 | cat {filename[:-4]}.{filetype}"

                if "|" in totalCommand:
                    cmd_parts = totalCommand.split('|')
                else:
                    cmd_parts = []
                    cmd_parts.append(totalCommand)
                i = 0
                p = {}
                for cmd_part in cmd_parts:
                    try:
                        cmd_part = cmd_part.strip()
                        if i == 0:
                            p[i]=subprocess.Popen(shlex.split(cmd_part),stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        else:
                            p[i]=subprocess.Popen(shlex.split(cmd_part),stdin=p[i-1].stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        i += 1
                    except Exception as e:
                        err = str(e) + ' : ' + str(cmd_part)
                        return (
                            '<pre>Error : ' + err + '</pre>'
                            '<pre>' + content + '</pre>').split('\n')
                
                (output, err) = p[i-1].communicate()
                exit_code = p[0].wait()
               
                if filetype == 'svg':
                    # print("SVG DETECTED")
                    encoding = 'base64'
                    # output = output.encode('utf-8')
                    output = base64.b64encode(output).decode('utf-8')
                    data_url_filetype = 'svg+xml'
                    data_path = "data:image/%s;%s,%s" % (
                        data_url_filetype,
                        encoding,
                        output)
                    img = " "*decalage+"![" + filename + "](" + data_path + ")"

                if filetype == 'png':
                    # print("PNG DETECTED")
                    data_url_filetype = 'png'
                    encoding = 'base64'
                    output = base64.b64encode(output).decode('utf-8')
                    data_path = "data:image/%s;%s,%s" % (
                        data_url_filetype,
                        encoding,
                        output)
                    img = " "*decalage+"![" + filename + "](" + data_path + ")"

                text = '%s\n%s\n%s' % (
                    text[:m.start()], img, text[m.end():])
        return text.split("\n")

def makeExtension(*args, **kwargs):
    return MkdocsAsyExtension(*args, **kwargs)
