"""
Metadata storage for individual measurements, such as taxonomic metadata and
file paths.
"""

import os

##############################################################################

class Measurement:
	"""
	Metadata for a single measurement
	
	:param db_dir: Directory of the overall database, used as a base to
		construct measurement-specific filepaths which may depend on other 
		measurement attributes such as the sort_date.
	:type db_dir: A string or path-like object
	:param experiment: An identifier for a group of related measurements.
		Together with snum, must uniquely identify the measurement.
	:type experiment: str
	:param snum: The measurement serial number. Together with the experiment,
		must uniquely identify the measurement.
	:type snum: int
	:param sort_date: The date used for 'administration' tasks associated with
		this measurement, such as constructing a Labber-style filepath. May or
		may not reflect the actual date on which the measurement was taken.
	:type sort_date: class: datetime.date
	"""

	def __init__(self, db_dir, experiment, snum, sort_date, **kwargs):
		"""
		Initialize a Measurement object with the required attributes (db_dir, 
		experiment, snum, sort_date), as well as further optional attributes 
		specified through the remaining kwargs.
		"""
		## Assign data attributes
		self.db_dir = db_dir
		self.experiment = experiment
		self.snum = snum
		self.sort_date = sort_date
		## Additional attributes
		self.extra_attributes = kwargs


	## Magic attributes
	##########################################################################

	## Representation
	def __str__(self):
		return self.name
	def __repr__(self):
		return "<Measurement object {} at {:d}>".format(str(self), id(self))
	def __hash__(self):
		## Hashed from the data fields that are intended to uniquely identify
		## the measurement, ie experiment and serial number
		## This may change in the future!
		return hash((self.experiment, self.snum))
	def __format__(self, fmt_spec):
		## String formatting
		if (fmt_spec == "") or (fmt_spec == "s"):
			return format(str(self), fmt_spec)
		## Decimal formatting - snum
		elif fmt_spec == "d":
			return format(int(self), fmt_spec)
		else:
			raise ValueError("{} is not a valid format specifier for object of type Measurement".format(fmt_spec))
	
	## Implicit type conversion
	def __int__(self):
		return self.snum

	## Overloaded comparison operators
	def __lt__(self, other):
		return str(self) < str(other)
	def __le__(self, other):
		return (self < other) or (self == other) 
	def __eq__(self, other):
		return hash(self) == hash(other) 
	def __ne__(self, other):
		return not (self == other)
	def __gt__(self, other):
		return str(self) > str(other)
	def __ge__(self, other):
		return (self > other) or (self == other)


	## Compound attributes
	##########################################################################

	@property
	def serial(self):
		"""Text form of the serial number with zero-padding.
		"""
		return "{:04d}".format(self.snum)


	@property
	def name(self):
		"""
		<experiment>_<serial number>, uniquely identifying the measurement
		irrespectively of other data fields.
		"""
		return "{}_{}".format(self.experiment, self.serial)


	@property
	def directory(self):
		"""
		Labber-style directory based on db_dir and sort_date attributes.

		This may/will be changed when expanding beyond the Labber use case!
		Expect more flexibility in the future.
		"""
		sort_dir = "{:%Y/%m/Data_%m%d}".format(self.sort_date)
		return os.path.join(self.db_dir, sort_dir)


	@property
	def path(self):
		"""
		The full filepath to the data file corresponding to this measurement.

		Currently Labber-style but this will be more customizable in the 
		future.
		"""
		return os.path.normpath(os.path.join(self.directory, self.name+".hdf5"))

