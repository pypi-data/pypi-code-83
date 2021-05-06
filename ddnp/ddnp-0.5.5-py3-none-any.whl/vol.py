'''
COPYRIGHT:
Copyright (c) 2015-2019, California Institute of Technology ("Caltech").
U.S. Government sponsorship acknowledged.
All rights reserved.

LICENSE:
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
- Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
- Neither the name of Caltech nor its operating division, the Jet
Propulsion Laboratory, nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior
written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

NTR:
'''

import flask
import os
import tarfile
import tempfile

CONTEXT = set()
def add (path:str)->None:
    '''store another path'''
    CONTEXT.add (path)
    return

def get (request:{})->str:
    '''get file(s) from the current volumes'''
    if len(request) != 1: raise KeyError('One file at a time.')

    request_name = request.to_dict().popitem()[0]
    result = None
    for path in CONTEXT:
        filename = os.path.abspath (os.path.join (path, request_name))

        if not os.path.isfile (filename): continue
        if not filename.startswith (path):
            raise KeyError('Filename is not legal')

        result = flask.send_file (filename, as_attachment=True)
        pass

    if result is None: raise FileNotFoundError()
    return result

def put (request:{})->str:
    '''put a single file into the current volumes'''
    return 'not implemented'

def tar (request:{})->str:
    '''tar up a file(s) or path(s) and deliver it as single item'''
    fid,filename = tempfile.mkstemp()
    os.close(fid)
    with tarfile.open (filename, 'w:gz') as tgz:
        for item in request:
            for path in CONTEXT:
                candidate = os.path.abspath (os.path.join (path, item))

                if (not (candidate.startswith(path) and
                         os.path.exists (candidate))):
                    raise KeyError('not a leagal path')

                os.chdir (path)
                tgz.add (item)
                pass
            pass
        pass
    return flask.send_file (filename, as_attachment=True)

def untar (request:{})->str:
    '''untar into the current volumes'''
    return 'not implemented'
