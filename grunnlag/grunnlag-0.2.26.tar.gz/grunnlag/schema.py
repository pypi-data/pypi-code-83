from grunnlag.graphql.queries.representation import GET_REPRESENTATION, FILTER_REPRESENTATION
from grunnlag.graphql.mutations.representation import CREATE_REPRESENTATION, UPDATE_REPRESENTATION
from grunnlag.graphql.queries.sample import GET_SAMPLE, FILTER_SAMPLE
from grunnlag.graphql.mutations.sample import CREATE_SAMPLE
from grunnlag.managers import AsyncRepresentationManager, RepresentationManager
from typing import List, Optional
from bergen.types.model import ArnheimModel
from bergen.schema import User
from enum import Enum
from grunnlag.extenders import Array
try:
	# python 3.8
	from typing import ForwardRef
except ImportError:
	# ForwardRef is private in python 3.6 and 3.7
	from typing import _ForwardRef as ForwardRef


Representation = ForwardRef("Representation")
Sample = ForwardRef("Sample")
Experiment = ForwardRef("Experiment")


class RepresentationVariety(str, Enum):
    VOXEL = "VOXEL"
    MASK = "MASK"
    UNKNOWN = "UNKNOWN"



class Representation(Array, ArnheimModel):
    id: Optional[int]
    name: Optional[str]
    package: Optional[str]
    store: Optional[str]
    shape: Optional[List[int]]
    image: Optional[str]
    unique: Optional[str]
    variety: Optional[RepresentationVariety]
    sample: Optional[Sample]
    tags: Optional[List[str]]

    objects = RepresentationManager()
    asyncs = AsyncRepresentationManager()

    class Meta:
        identifier = "representation"
        get = GET_REPRESENTATION
        create = CREATE_REPRESENTATION
        update = UPDATE_REPRESENTATION
        filter = FILTER_REPRESENTATION


class Sample(ArnheimModel):
    id: Optional[int]
    representations: Optional[List[Representation]]
    creator: Optional[User]
    experiments: Optional[List[Experiment]]
    name: Optional[str]

    class Meta:
        identifier = "sample"
        get = GET_SAMPLE
        filter = FILTER_SAMPLE
        create = CREATE_SAMPLE


class Experiment(ArnheimModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    descriptionLong: Optional[str]
    creator: Optional[User]
    samples: Optional[List[Sample]]

    class Meta:
        identifier = "experiment"
        


Representation.update_forward_refs()
Sample.update_forward_refs()
Experiment.update_forward_refs()

