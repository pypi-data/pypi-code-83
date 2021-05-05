#    This script is part of pyroglancer (https://github.com/SridharJagannathan/pyroglancer).
#    Copyright (C) 2020 Sridhar Jagannathan
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

"""Test file for debugging purposes."""

# from pyroglancer.layers import handle_emdata, handle_segmentdata, handle_synapticdata
# from pyroglancer.layers import handle_synapticclefts, handle_meshes
# from pyroglancer.ngspaces import create_ngspace
# from pyroglancer.localserver import startdataserver, closedataserver
# from pyroglancer.ngviewer import openviewer, closeviewer, setviewerstate
# import neuroglancer as ng
# import pandas as pd
# from pyroglancer.layers import create_nglayer, add_precomputed
# from pyroglancer.flywire import flywireurl2dict, add_flywirelayer, set_flywireviewerstate
# import os
# import numpy as np
# import trimesh
# import glob
# import navis
# import flybrains
# import fafbseg
# import pymaid
# import struct
# import json
# import fafbseg

# from cloudvolume import CloudVolume, chunks, Storage, Skeleton
# from cloudvolume.storage import SimpleStorage
# from cloudvolume.lib import mkdir, Bbox, Vec, jsonify

# from pyroglancer.meshgenerator import decompose_meshes
# import navis.interfaces.neuprint as neu
# import flybrains
# from neuroglancer import credentials_provider, google_credentials
# from PIL import Image


# from cloudvolume.datasource.precomputed.sharding import ShardingSpecification

# ngviewer = openviewer(ngviewer = None)

# layer_kws = {}
# layer_kws['ngspace'] = "FAFB"
# layer_kws['name'] = "fafb_v14_orig"
# handle_emdata(ngviewer, layer_kws)

# layer_kws = {}
# layer_kws['ngspace'] = "FAFB"
# layer_kws['name'] = "seg_20200412"
# handle_segmentdata(ngviewer, layer_kws)

# layer_kws = {}
# layer_kws['ngspace'] = "FAFB"
# layer_kws['name'] = "synapses_buhmann2019"
# handle_synapticdata(ngviewer, layer_kws)

# layer_kws = {}
# layer_kws['ngspace'] = "FAFB"
# layer_kws['name'] = "clefts_Heinrich_etal"
# handle_synapticclefts(ngviewer, layer_kws)

# layer_kws = {}
# layer_kws['ngspace'] = "FAFB"
# layer_kws['name'] = "FAFB.surf"
# handle_meshes(ngviewer, layer_kws)

# create_ngspace(ngspace='FAFB')
# create_ngspace(ngspace='FANC')
# create_ngspace(ngspace='MANC')
# create_ngspace(ngspace='hemibrain')

# startdataserver()
# create_ngspace(ngspace='FAFB')
# temp_pts = pd.DataFrame([[123072, 47001, 3375], [120000, 17001, 3000]], columns=['x', 'y', 'z'])
# temp_pts['description'] = 'temp_pts'
# tmpviewer = create_nglayer(layer_kws={'type': 'points', 'name': 'landmarks',
#                                       'source': temp_pts, 'color': 'magenta'})

# temp_pts = []

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # shorturl = 'https://ngl.flywire.ai/?json_url=https://globalv1.flywire-daf.com/nglstate/5692426366746624'
# # ngdict = flywireurl2dict(shorturl)

# swc_path = os.path.join(BASE_DIR, 'pyroglancer/data/swc')
# swc_files = glob.glob(os.path.join(swc_path, '*.swc'))

# neuronlist = []
# neuronlist += [navis.read_swc(f, units='8 nm', connector_labels={'presynapse': 7, 'postsynapse': 8},
#                               id=int(os.path.splitext(os.path.basename(f))[0])) for f in swc_files]

# neuronlist = navis.core.NeuronList(neuronlist)
# publicurl = 'https://fafb.catmaid.virtualflybrain.org/'
# working_rm = pymaid.CatmaidInstance(publicurl, api_token=None, project_id=1)
# sample_skids = ['40637', '27295', '57311', '2863104', '57#323']
# catmiad_neuronlist = pymaid.get_neurons(sample_skids, remote_instance=working_rm)

# vols = pymaid.get_volume(['AL_L', 'AL_R'], color=(255, 0, 0, .2))
# vols['AL_R'].id = 200
# vols['AL_L'].id = 300

# client = neu.Client('https://neuprint.janelia.org/', dataset='hemibrain:v1.2')

# bodyids = [988852391, 988632865, 988909130, 989228019]
# neuronmeshes_df = neu.fetch_mesh_neuron(bodyids, lod=2, with_synapses=False)
# flywireneuronmeshes_df = navis.xform_brain(neuronmeshes_df, source='JRCFIB2018Fraw', target='FAFB', verbose=True)

# startdataserver()

# create_ngspace('FAFB')

# tmpviewer = create_nglayer(layer_kws={'type': 'volumes', 'name': 'flywiremesh',
#                                       'source': flywireneuronmeshes_df, 'color': 'blue'})

# tmpviewer = create_nglayer(layer_kws={'type': 'volumes', 'source': [vols['AL_R']],  # ,vols['AL_L']],
#                                       'name': 'neuropils', 'color': ['magenta', 'blue'], 'alpha': 0.3,
#                                       'multires': True,
#                                       'sharding': True,
#                                       'progress': True})

# layer_kws = {'type': 'skeletons', 'source': catmiad_neuronlist, 'sharding': True}
# add_flywirelayer(ngdict, layer_kws)
# create_nglayer(layer_kws=layer_kws)

# closedataserver()

# neuronlist = []
# neuronlist += [navis.read_swc(f, units='8 nm', connector_labels={'presynapse': 7, 'postsynapse': 8},
#                               id=int(os.path.splitext(os.path.basename(f))[0])) for f in swc_files]
# neuronlist = navis.core.NeuronList(neuronlist)

# flybrains.download_jefferislab_transforms()
# flybrains.download_saalfeldlab_transforms()
# flybrains.register_transforms()

# startdataserver()

# pre_syn_df2 = pd.read_hdf('/Users/sri/Downloads/test_data.h5', 'presyn').head(5)
# flywire_neuron = navis.xform_brain(neuronlist, source='FAFB14', target='FLYWIRE')
# flywire_neuron = navis.resample_neuron(flywire_neuron, resample_to=1000*8, inplace=False)
# layer_kws = {'type': 'synapses', 'source': flywire_neuron, 'annotationstatetype': 'in-json',
#              'color': ['red', 'blue'],
#               "scale": [4,4,40]}
# flywireurl = add_flywirelayer(ngdict, layer_kws)

# tempval = []

# scale = layer_kws.get("scale", 0)

# skel = Skeleton(
#     [
#         (0, 0, 0), (1, 0, 0), (2, 0, 0),
#         (0, 1, 0), (0, 2, 0), (0, 3, 0),
#     ],
#     edges=[
#         (0, 1), (1, 2),
#         (3, 4), (4, 5), (3, 5)
#     ],
#     segid=1,
#     extra_attributes=[
#         {
#             "id": "radius",
#             "data_type": "float32",
#             "num_components": 1,
#         }
#     ]
# ).physical_space()

# skels = {}
# for i in range(10):
#     sk = skel.clone()
#     sk.id = i
#     skels[i] = sk.to_precomputed()

# info = CloudVolume.create_new_info(
#     num_channels=1,  # Increase this number when we add more tests for RGB
#     layer_type='segmentation',
#     data_type='uint16',
#     encoding='raw',
#     resolution=[1, 1, 1],
#     voxel_offset=(0, 0, 0),
#     skeletons=True,
#     volume_size=(100, 100, 100),
#     chunk_size=(64, 64, 64),
# )

# mkdir('/tmp/removeme/skeletons/sharded/skeletons')
# with open('/tmp/removeme/skeletons/sharded/info', 'wt') as f:
#     f.write(jsonify(info))

# skel_info = {
#     "@type": "neuroglancer_skeletons",
#     "transform": [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
#     "vertex_attributes": [
#         {"id": "radius", "data_type": "float32", "num_components": 1}
#     ],
#     "mip": 3,
# }

# for idxenc in ('raw', 'gzip'):
#     for dataenc in ('raw', 'gzip'):

#       spec = ShardingSpecification(
#         'neuroglancer_uint64_sharded_v1',
#         preshift_bits=1,
#         hash='murmurhash3_x86_128',
#         minishard_bits=2,
#         shard_bits=1,
#         minishard_index_encoding=idxenc,
#         data_encoding=dataenc,
#       )
#       skel_info['sharding'] = spec.to_dict()

#       with open('/tmp/removeme/skeletons/sharded/skeletons/info', 'wt') as f:
#         f.write(jsonify(skel_info))

#       files = spec.synthesize_shards(skels)
#       for fname in files.keys():
#         with open('/tmp/removeme/skeletons/sharded/skeletons/' + fname, 'wb') as f:
#           f.write(files[fname])

#       cv = CloudVolume('file:///tmp/removeme/skeletons/sharded/')
#       assert cv.skeleton.meta.mip == 3

#       for i in range(10):
#         sk = cv.skeleton.get(i).physical_space()
#         sk.id = 1
#         assert sk == skel

#       labels = []
#       for fname in files.keys():
#         lbls = cv.skeleton.reader.list_labels(fname, path='skeletons')
#         labels += list(lbls)

#       labels.sort()
#       assert labels == list(range(10))

#       for filename, shard in files.items():
#         decoded_skels = cv.skeleton.reader.disassemble_shard(shard)
#         for label, binary in decoded_skels.items():
#           Skeleton.from_precomputed(binary)

#       exists = cv.skeleton.reader.exists(list(range(11)), path='skeletons')
#       assert exists == {
#         0: 'skeletons/0.shard',
#         1: 'skeletons/0.shard',
#         2: 'skeletons/0.shard',
#         3: 'skeletons/0.shard',
#         4: 'skeletons/0.shard',
#         5: 'skeletons/0.shard',
#         6: 'skeletons/0.shard',
#         7: 'skeletons/0.shard',
#         8: 'skeletons/1.shard',
#         9: 'skeletons/1.shard',
#         10: None,
#       }

# shutil.rmtree('/tmp/removeme/skeletons')


# hemibrain_vol = CloudVolume('gs://neuroglancer-janelia-flyem-hemibrain/v1.0/segmentation',
#                              mip=0, cache=False, use_https=True)

# meshes = hemibrain_vol.mesh.get([511271574], lod=2)

# tempval = []
# fileloc = 'file:///private/var/folders/_l/lrfvj_8j3ps0c37ncbr3c8dh0000gn/T/tmpvqvxdj4e/precomputed/neuropils/mesh/'
# fileloc = 'http://localhost:8000/precomputed/neuropils/'
# info = CloudVolume.create_new_info(
#     num_channels=1,
#     layer_type='segmentation',
#     data_type='uint64',  # Channel images might be 'uint8'
#     encoding='raw',  # raw, jpeg, compressed_segmentation, fpzip, kempressed
#     resolution=[4, 4, 40],  # Voxel scaling, units are in nanometers
#     voxel_offset=[0, 0, 0],  # x,y,z offset in voxels from the origin
#     mesh='mesh',
#     # Pick a convenient size for your underlying chunk representation
#     # Powers of two are recommended, doesn't need to cover image exactly
#     chunk_size=[34422, 37820, 41362],  # units are voxels
#     volume_size=[250000, 250000, 25000],  # e.g. a cubic millimeter dataset
# )
# neuropil = CloudVolume(fileloc, info=info, mip=0, cache=False, use_https=False)


# meshes = neuropil.mesh.get([200], lod=2)

# example sphere..

# meshes = trimesh.creation.uv_sphere()

# verts = meshes.vertices
# faces = meshes.faces

# quantization_bits = 16
# lods = np.array([0, 1, 2])
# chunk_shape = (verts.max(axis=0) - verts.min(axis=0))/2**lods.max()
# grid_origin = verts.min(axis=0)
# lod_scales = np.array([2**lod for lod in lods])
# num_lods = len(lod_scales)
# vertex_offsets = np.array([[0., 0., 0.] for _ in range(num_lods)])

# fragment_offsets = []
# fragment_positions = []
# #mkdir('/tmp/removeme/precompute/multi_res/mesh')
# with open('/tmp/removeme/precompute/multi_res/mesh/1', 'wb') as f:
#     for scale in lod_scales[::-1]:
#         lod_offsets = []
#         nodes, submeshes = decompose_meshes(verts.copy(), faces.copy(), scale, quantization_bits)

#         for mesh in submeshes:
#             draco = trimesh.exchange.ply.export_draco(mesh, bits=16)
#             f.write(draco)
#             lod_offsets.append(len(draco))

#         fragment_positions.append(np.array(nodes))
#         fragment_offsets.append(np.array(lod_offsets))

# num_fragments_per_lod = np.array([len(nodes) for nodes in fragment_positions])


# with open('/tmp/removeme/precompute/multi_res/mesh/1.index', 'wb') as f:
#     f.write(chunk_shape.astype('<f').tobytes())
#     f.write(grid_origin.astype('<f').tobytes())
#     f.write(struct.pack('<I', num_lods))
#     f.write(lod_scales.astype('<f').tobytes())
#     f.write(vertex_offsets.astype('<f').tobytes(order='C'))
#     f.write(num_fragments_per_lod.astype('<I').tobytes())
#     for frag_pos, frag_offset in zip(fragment_positions, fragment_offsets):
#         f.write(frag_pos.T.astype('<I').tobytes(order='C'))
#         f.write(frag_offset.astype('<I').tobytes(order='C'))

# with open('/tmp/removeme/precompute/multi_res/mesh/info', 'w') as f:
#     info = {
#         '@type': 'neuroglancer_multilod_draco',
#         'vertex_quantization_bits': 16,
#         'transform': [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
#         'lod_scale_multiplier': 1
#     }

#     json.dump(info, f)


# ngviewer = openviewer(ngviewer = None)
# startdataserver(directory='/tmp/removeme/precompute/multi_res/mesh/')

# create_ngspace(ngspace='FAFB')

# shorturl = 'https://ngl.flywire.ai/?json_url=https://globalv1.flywire-daf.com/nglstate/4832227095478272'
# ngdict = flywireurl2dict(shorturl)

# layer_kws = {'type': 'segments',
#              'segmentid': 720575940620589336,
#              'color': 'cyan',
#              'alpha': 0.8
#              }

# flywireurl = add_flywirelayer(layer_kws=layer_kws)

# import google.auth
# credentials, project = google.auth.default()


# import urllib.request as urllib2
# import requests

# # req = urllib2.Request("https://emdata5-private.janelia.org/api/server/token")
# r = requests.get('https://emdata5-private.janelia.org/api/server/token')
# #response = urllib2.urlopen(req)
# html = response.read()
# json_obj = json.loads(html)
# token_string = json_obj["token"].encode("ascii", "ignore")

# default_credentials_manager = credentials_provider.CredentialsManager()
# default_credentials_manager.register(
#     u'google-brainmaps',
#     lambda _parameters: google_credentials.GoogleOAuth2FlowCredentialsProvider(
#         client_id=u'639403125587-ue3c18dalqidqehs1n1p5rjvgni5f7qu.apps.googleusercontent.com',
#         client_secret=u'kuaqECaVXOKEJ2L6ifZu4Aqt',
#         scopes=[u'https://www.googleapis.com/auth/brainmaps'],
#     ))
# tempval = default_credentials_manager.register(u'DVID',
#                                      lambda _parameters: google_credentials.get_google_application_default_credentials_provider())

# token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiai5zcmlkaGFycmFqYW5AZ21haWwuY29tIn0.qe9tvB7zYfUeoOpdgR3Rf-52QohTRVFfLIVfZprW5VI'
# tempval = default_credentials_manager.register(u'DVID', token)

# layer_kws = {'ngspace': 'MANC'}
# create_ngspace(layer_kws)

# layer_kws = {'ngspace': 'FAFB'}
# create_ngspace(layer_kws)
# tmpviewer2 = setviewerstate(axis_lines=False, bounding_box=False)
# screenshot2 = tmpviewer2.screenshot(size=[800, 500])


# publicurl = 'https://fafb.catmaid.virtualflybrain.org/'
# working_rm = pymaid.CatmaidInstance(publicurl, api_token=None, project_id=1)
# catmiad_neuronlist = pymaid.get_neuron('/DA1 lPN', remote_instance=working_rm)  # get some DA1 PNs..
# flywire_neuron = navis.xform_brain(catmiad_neuronlist, source='FAFB14', target='FLYWIRE')

# startdataserver()

# shorturl = 'https://ngl.flywire.ai/?json_url=https://globalv1.flywire-daf.com/nglstate/5644175227748352'

# tmpviewer = add_flywirelayer(flywireurl2dict(shorturl), layer_kws={'type': 'skeletons',
#                                                                    'source': flywire_neuron[7:9],
#                                                                    'color': 'red'})

# shorturl = tmpviewer
# layout = {'type': 'xy-3d', 'orthographicProjection': 'True'}
# tmpviewer, shorturl = set_flywireviewerstate(shorturl, axis_lines=False, bounding_box=False, layout=layout)

# # screenshot = tmpviewer.screenshot(size=[800, 500])
# tempval = tmpviewer.screenshot().screenshot.image
# screenshot_image = Image(value=tmpviewer.screenshot().screenshot.image)

# tempval = []
