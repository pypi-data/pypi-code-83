from bx.command import Command
from bx import download as dl


class FreeSurfer6Command(Command):
    """FreeSurfer v6.0

    Available subcommands:
     files:\t\tdownload all `recon-all` outputs (segmentation maps, files, everything...)
     aseg:\t\tcreate an Excel table with all `aseg` measurements
     aparc:\t\tcreate an Excel table with all `aparc` measurements
     hippoSfVolumes:\tsave an Excel table with hippocampal subfield volumes (if available)
     snapshot:\t\tdownload a snapshot from the `recon-all` pipeline
     report:\t\tdownload the validation report issued by `FreeSurferValidator`
     tests:\t\tcreate an Excel table with all automatic tests outcomes from `FreeSurferValidator`

    Usage:
     bx freesurfer6 <subcommand> <resource_id>
    """
    nargs = 2
    resource_name = 'FREESURFER6'
    subcommands = ['aparc', 'aseg', 'hippoSfVolumes', 'snapshot', 'tests',
                   'report', 'files']
    validator = 'FreeSurferValidator'

    def __init__(self, *args, **kwargs):
        super(FreeSurfer6Command, self).__init__(*args, **kwargs)

    def parse(self):
        subcommand = self.args[0]
        id = self.args[1]  # should be a project or an experiment_id

        if subcommand in ['aparc', 'aseg', 'hippoSfVolumes']:
            import logging as log
            msg = 'FreeSurfer6 has a bug in the computation of some of the'\
                  ' global metrics on high resolution data analyzed at high '\
                  'resolution. Thus, reported values are in voxels not mm3. '\
                  'For consistency those have been excluded from bx results. '\
                  'Source: https://surfer.nmr.mgh.harvard.edu/fswiki/BrainVolStatsFixed'
            if 'HIRES' in self.resource_name:
                log.warning(msg)
            df = self.run_id(id, dl.measurements,
                             resource_name=self.resource_name,
                             subfunc=subcommand, max_rows=10)
            self.to_excel(id, df)

        elif subcommand in ['files', 'report', 'snapshot']:
            self.subcommand_download()

        elif subcommand == 'tests':

            version = ['##0390c55f', '4e37c9d0']
            from bx import validation as val
            df = self.run_id(id, val.validation_scores,
                             validator=self.validator,
                             version=version, max_rows=25)
            self.to_excel(id, df)

    def subcommand_download(self):
        subcommand = self.args[0]
        id = self.args[1]

        resource_name = self.resource_name
        validator = self.validator
        if 'hires' in self.command:
            resource_name = 'FREESURFER6_HIRES'
            validator = 'FreeSurferHiresValidator'

        if subcommand == 'report':
            resource_name = None

        from bx import download as dl
        self.run_id(id, dl.download, resource_name=resource_name,
                    validator=validator, destdir=self.destdir,
                    subcommand=subcommand)


class FreeSurfer6HiresCommand(FreeSurfer6Command):
    """FreeSurfer v6.0 (-hires option)

    Available subcommands:
     files:\t\tdownload all `recon-all` outputs (segmentation maps, files, everything...)
     aseg:\t\tcreates an Excel table with all `aseg` measurements
     aparc:\t\tcreates an Excel table with all `aparc` measurements
     hippoSfVolumes:\tsaves an Excel table with hippocampal subfield volumes (if available)
     snapshot:\t\tdownload a snapshot from the `recon-all` pipeline
     report:\t\tdownload the validation report issued by `FreeSurferHiresValidator`
     tests:\t\tcreates an Excel table with all automatic tests outcomes from `FreeSurferValidator`

    Usage:
     bx freesurfer6hires <subcommand> <resource_id>
    """
    nargs = 2
    resource_name = 'FREESURFER6_HIRES'

    def __init__(self, *args, **kwargs):
        super(FreeSurfer6HiresCommand, self).__init__(*args, **kwargs)
