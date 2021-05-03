#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
import re
import io
import json
from collections import defaultdict, Counter
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from fmqlutils.cacher.cacherUtils import FMQLReplyStore, FilteredResultIterator, metaOfVistA
from fmqlutils.reporter.reportUtils import MarkdownTable, reportPercent, reportAbsAndPercent

def dateRangeOfClones(snos):
    """
    Returns: 
    - first and last cut date
    - last full month of oldest clone
    """
    cutDateBySNO = {}
    for sno in sorted(snos):
        try:
            meta = metaOfVistA(sno)
        except:
            raise Exception(f"No meta for {sno}")
        else:
            cutDateBySNO[sno] = meta["cutDate"]
    oldestToLatest = sorted([cutDateBySNO[sno] for sno in cutDateBySNO])
    info = {
        "oldest": datetime.strptime(oldestToLatest[0], "%Y-%m-%d"),
        "youngest": datetime.strptime(oldestToLatest[-1], "%Y-%m-%d")
    }
    # Unless oldest date is end of month then go back a month so full month
    oldestLastOfMonth = datetime(info["oldest"].year, (info["oldest"] + relativedelta(months=1)).month, 1) - timedelta(days=1)
    if info["oldest"] != oldestLastOfMonth:
        # or just do relativedelta(31) as stops at month end
        oldestFirstOfMonth = datetime(info["oldest"].year, info["oldest"].month, 1) 
        oldestLastOfPreviousMonth = oldestFirstOfMonth - relativedelta(days=1) 
        info["oldestLastFullMonth"] = oldestLastOfPreviousMonth
    else:
        info["oldestLastFullMonth"] = info["oldest"]
    print(f"Date information for range of VistAs: {info}")
    return info
    
def vistaStationNosToNames(snos):
    snosToNames = {}
    for sno in sorted(snos):
        try:
            meta = metaOfVistA(sno)
        except:
            raise Exception(f"No meta for {sno}")
        else:
            snosToNames[sno] = meta["name"]    
    return snosToNames
    
def webReportSourceVistAs(snos):

    mu = "## VistA Clone Details\n\n"

    mu += f"Data from <span style='yellowIt'>{len(snos):,} VistAs was parsed. The VistAs are copies of production VistAs cut on the dates given below  ...\n\n"
    tbl = MarkdownTable([":VistA", ":Station \#", "Clone Cut Date"])
    for sno in sorted(snos):
        try:
            meta = metaOfVistA(sno)
        except:
            vistaName = ""
            cutDate = ""
            print(f"No meta of vista for {sno} - work locally by copying _/TmpWorking/metaOfVistA.json_ over. If too old then refresh?")
        else:
            vistaName = meta["name"]
            cutDate = meta["cutDate"]
        tbl.addRow([
            f'__{vistaName}__' if vistaName else "&nbsp;",
            sno,
            cutDate if cutDate else "&nbsp;"
        ])
    mu += tbl.md() + "\n\n"
    return mu
    
# ############################## TEST ################################
            
def main():

    print(dateRangeOfClones(["463", "687"]))
        
if __name__ == "__main__":
    main()