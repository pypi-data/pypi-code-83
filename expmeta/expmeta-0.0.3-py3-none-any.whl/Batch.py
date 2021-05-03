"""
Metadata containers for storage of multiple measurements
"""

import pandas as pd
from . import Measurement

pd.options.mode.chained_assignment = None

##############################################################################

class pdBatch:
	"""
	Metadata for a batch of measurements, built on a pandas DataFrame

	:param db_dir: Directory of the overall database, used as a base to construct measurement-specific filepaths which may depend on other measurement attributes such as the sort_date.
	:type db_dir: A string or path-like object
	:param data_df: An existing pandas DataFrame with the appropriate structure. Either data_df or all of [experiment, sort_date, snums] must be provided, with the existing DataFrame taking precedence.
	:type data_df: pd.DataFrame, optional
	:param experiment: An identifier for a group of related measurements. Together with snum, must uniquely identify the measurement.
	:type experiment: str or Sequence of str
	:param snum: The measurement serial number. Together with the experiment must uniquely identify the measurement.
	:type snum: int or Sequence of int
	:param sort_date: The date used for 'administration' tasks associated with this measurement, such as constructing a Labber-style filepath. May or may not reflect the actual date on which the measurement was taken.
	:type sort_date: class: datetime.date or Sequence of datetime.date

	Additional kwargs to the constructor will be stored as additional parameters in the DataFrame. All parameters must either be scalars/strings, or have the same length as the longest Sequence passed in to any of the params.

	In general, the aim is to provide as many intuitive idioms, in particular some common and useful DataFrame operations, to get or iterate over either `pdBatch` objects containing (row-)subsets of the metadata, or in instances where a single row is desired, a `Measurement` object with all the appropriate parameters.

	The underlying pandas DataFrame can be directly accessed through the `df` attribute. 
	"""

	def __init__(self, db_dir, data_df=None, *,
				 experiment=None, sort_date=None, snums=None, 
				 **kwargs):
		"""
		Initialize a pdBatch object, either via an existing DataFrame of the appropriate format, or by specifying the individual parameters or Sequences of parameters directly.
		"""
		## Assign fixed attributes
		self.db_dir = db_dir
		## If creating from a DataFrame, just create directly
		if data_df is not None:
			self.df = data_df
		## Create DataFrame and populate it with passed-in params
		else:
			## Get length of first non-scalar item in attribs (incl extras)
			for item in [experiment, sort_date, snums]+list(kwargs.items()):
				## Exclude strings as they have a len
				if isinstance(item, str):
					continue
				else:
					## Try to check the length
					try:
						batch_len = len(item)
						break
					except TypeError:
						continue

			## Make a DataFrame that is that long, with the appropriate columns
			self.df = pd.DataFrame(index=range(batch_len),
								columns=["experiment", "snum", "sort_date"]+list(kwargs.keys()))
			## Fill DataFrame with values
			for label, value in {**{"experiment": experiment, "snum": snums, "sort_date": sort_date}, **kwargs}.items():
				self.df[label] = value
			## Set the experiment and snums as the index, to ensure consistency when we do things like merges etc.
			self.df.set_index(["experiment", "snum"], inplace=True)
		## Sort the index; it should go by experiment first, then serial
		self.df.sort_index(inplace=True)


	## Measurement object fetch conversion
	def meas_from_row(self, row_series):
		return Measurement(
					db_dir=self.db_dir, 
					experiment=row_series.name[0], 
					snum=row_series.name[1], 
					**row_series.to_dict())

	## New pdBatch object from subset of the DataFrame
	def batch_from_dfsub(self, dfsub):
		return pdBatch(db_dir=self.db_dir, data_df=dfsub)


	## Magic methods
	##########################################################################

	## Representations
	##################

	def __str__(self):
		## Get the (experiment, snum) pairs for the first and last items
		first = self.df.iloc[0].name
		last = self.df.iloc[-1].name
		## Check if the experiment is the same
		if first[0] == last[0]:
			return "{}_{:04d}-{:04d}".format(*first, last[1])
		else:
			return "{}_{:04d}-{}_{:04d}".format(*first, *last)

	def __repr__(self):
		return "<pdBatch object {} at {}>".format(str(self), id(self))


	## Overloaded comparison operators
	##################################

	## Equality - check if all DataFrame elements are equal
	## We may want to consider making this only check the index values
	def __eq__(self, other):
		return self.df.equals(other.df)
	def __ne__(self, other):
		return not(self == other)


	## Membership and indexing
	##########################

	## TODO __contains__ method

	def __iter__(self):
		## Get rows in DataFrame
		for row_tuple in self.df.itertuples():
			## Convert to dict
			row_dict = row_tuple._asdict()
			## Extract the index elements
			experiment = row_dict["Index"][0]
			snum = row_dict["Index"][1]
			del row_dict["Index"]
			## Construct the Measurement object
			meas_obj = Measurement(db_dir=self.db_dir, 
								   experiment=experiment,
								   snum=snum,
								   **row_dict)
			yield meas_obj


	def __len__(self):
		return len(self.df)


	def __getitem__(self, index):
		## If string, break up into <experiment>_<snum> and fetch item
		if isinstance(index, str):
			fetch_exp = "_".join(index.split("_")[:-1])
			fetch_snum = int(index.split("_")[-1])
			return self.meas_from_row(self.df.loc[(fetch_exp, fetch_snum)])
		## If Measurement object, match the experiment and snum
		elif isinstance(index, Measurement):
			return self.meas_from_row(self.df.loc[(index.experiment, index.snum)])
		## If it is a single integer, fetch the row by index
		elif isinstance(index, int):
			return self.meas_from_row(self.df.iloc[index])
		## Otherwise, pass it to the dataframe iloc and return a pdBatch object with the subset dataframe
		else:
			return self.batch_from_dfsub(self.df.iloc[index])


	## Arithmetic overloading
	#########################

	def __add__(self, other):
		## Concatenate the DataFrames
		cat_df = pd.concat([self.df, other.df], verify_integrity=True)
		## Create new pdBatch object from combined Dataframe
		out_batch = pdBatch(db_dir=self.db_dir, data_df=cat_df)
		return out_batch

	def __iadd__(self, other):
		## Concatenate the DataFrames
		cat_df = pd.concat([self.df, other.df], verify_integrity=True)
		## Reassign DataFrame
		self.df = cat_df
		## Sort indices
		self.df.sort_index(inplace=True)
		return self


	## Compound attributes
	######################

	@property
	def name(self):
		"""
		Name as a string, <first-experiment>_<first-snum>-<last-experiment>_<last-snum> if more than one experiment is present, otherwise <experiment>_<first-snum>-<last-snum>.
		"""
		return str(self)

	## DataFrame abstractions and wrappers
	######################################

	def groupby(self, columns, **kwargs):
		"""Iterator yielding pdBatch objects corresponding to groupbys of the underlying DataFrame along columns `columns`.
		"""
		## TODO this currently doesn't play nicely with tqdm!
		for values, group_df in self.df.groupby(columns, **kwargs):
			## Create new pdBatch object from Dataframe
			group_batch = self.batch_from_dfsub(group_df)
			## Return values conforming to pd groupby style
			yield values, group_batch
