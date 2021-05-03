#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
import re
import json
from collections import defaultdict, Counter
from datetime import datetime
import platform
import statistics
from typing import Pattern

from fmqlutils import VISTA_DATA_BASE_DIR
from fmqlutils.cacher.cacherUtils import FilteredResultIterator 
from fmqlutils.reporter.reportUtils import MarkdownTable, reportPercent, reportAbsAndPercent
from fmqlreports.webReportUtils import vistasOfVISN

from fileDirectory import CommonFileDirectory

"""
FINAL TODO P2: a web site - .md - of builds - with some "AI" of blurbs ie/ raw and then on to full. <----------- part of in VAEC web site and beyond .mds!

TODO P2: Focus on [1] Bulk up Build Meta and [2] Separate Report getting into [a] what's in builds and what's out of them, [b] redundancy, [c] core VistA build/bit of VistA ex/ VistA/Finance or ... In case of VistA/Finance, want to pull out as black box that needs data feeds in order to make its reports/do its calcs
- [ ] dependency between builds
- [ ] include ability to pull in missing pieces referenced like LINKs or APPs or PROTOCOLs as given in blurbs but not formally defined.
- [ ] for all components AND files -- add option to see what RPCs or options etc ARE NOT in any builds ie/ where 8994 is superset of RPCs known to builds (which reference 8994)
- [ ] do a "dateCut" to go with "dateAdded" and "stationNo" in opening list (true for all directories)
- [ ] EFFICIENCY: right now every entry keeps its own build meta copy -- change to normalize down to one master build meta and just reference => QA that same copy
- [ ] Build up by file/RPC report enable ie/ see report of addition in time and 
deletion and change ie/ system grows
  ... and want per package/subsystem too
- [ ] 8994 ala FileDirectory for RPCs ie/ compare all known to in builds
  - suppress rdv user setup
  - availability
- [ ] add in first install, # installs, last install per VistA of build (and can then graph installs vs ...) + simple cnt of any builds NOT installed => exclude from totals
- [ ] entries with missing or inconsistent dates ... report on it (see below warnings) [210 warnings from 13197]

TODO STRUCT/INSTALL: common base directory. Moving towards that with 'resource' and 'entry'. Just need to establish the base that WORKS FOR BUILDS AND FILES (as both 
unique in space)
REM: goal is that basic report drops out common.
REM: idea of set of resources with entries in each VistA (one per VistA or could have
> one in case of users?)
"""
class CommonBuildDirectory(): 

    ENTRY_IDX_SNO = 0

    ENTRY_IDX_ID = 1 # IEN
    ENTRY_IDX_NAME = 2 # assuming unique
    
    ENTRY_IDX_DATE_DISTRIBUTED = 3
    ENTRY_IDX_PACKAGE = 4
    ENTRY_IDX_TYPE = 5
    ENTRY_IDX_DESCRIPTION = 6
    ENTRY_IDX_ISNATIONAL = 7

    ENTRY_IDX_FILES = 8 # own array - not in Build Components
    
    ENTRY_IDX_RPCS = 9 # file 8994
    ENTRY_IDX_OPTIONS = 10 # file 19
    ENTRY_IDX_PROTOCOLS = 11 # file 101
    ENTRY_IDX_HL7LLS = 12 # file 870
    ENTRY_IDX_ROUTINES = 13 # file 9.8
    ENTRY_IDX_PARAMETER_DEFINITIONS = 14 # file 8989.51 ... TBD fully fill in 
    ENTRY_IDX_HL7APS = 15
    
    # Portable
    ENTRY_IDX_RESOURCE_ID = 2 # CommonBuildDirectory.ENTRY_IDX_NAME
    
    """
    # BUILD/INSTALL on file -- see if appropriate
    ENTRY_IDX_BUILD_FIRST_DT = 6
    ENTRY_IDX_BUILD_LAST_DT = 7
    ENTRY_IDX_BUILD_COUNT = 8
    ENTRY_IDX_INSTALL_FIRST_DT = 9
    ENTRY_IDX_INSTALL_LAST_DT = 10
    ENTRY_IDX_INSTALL_COUNT = 11
    """

    def __init__(self, vistaSNOs, dirPrefixLetter="B"):
        self.__vistaSNOs = vistaSNOs
        self.__dirFile = f'{VISTA_DATA_BASE_DIR}Common/Directory/{dirPrefixLetter}DIR.json'
        try:
            print("Attempting to load preexisting Directory")
            self.__dir = json.load(open(self.__dirFile))
        except:
            print("Starting Directory from Scratch")
            self.__dir = {"vistas": [], "entries": {}, "resources": []}
        else:
            print(f'Loaded preexisting directory with {len(self.__dir["resources"]):,} builds')
        self.__changeUpdate()
        
    def vistas(self):
        return self.__dir["vistas"]
        
    def resourceIds(self, stationNo): # to be portable
        return self.buildIds(stationNo)
        
    # To see, per station, add stationNo
    def total(self, stationNo=""):
        if stationNo == "":
            return len(self.__dir["resources"])
        return sum(1 for res in self.__dir["resources"] if sum(1 for gien in res if gien.split(":")[0] == stationNo))
        
    def entryTotal(self, stationNo=""):
        if stationNo == "":
            return len(self.__dir["entries"])
        return sum(1 for gien in self.__dir["entries"] if gien.split(":")[0] == stationNo)
                
    def lookupEntryByGIEN(self, gien):
        return self.__dir["entries"].get(gien, None)
        
    def commonCounts(self, stationNo="", excludeResources=set()):
        crossVistATypesPresenceCount = Counter()
        for res in self.__dir["resources"]:
            resName = self.__dir["entries"][res[0]][CommonBuildDirectory.ENTRY_IDX_RESOURCE_ID]
            crossVistATypesPresenceCount[resName] = len(res)
        ress = self.resourceIds(stationNo) # all if stationNo == ""
        commonCount = Counter()
        for resId in ress:
            if resId in excludeResources:
                continue
            commonCount[crossVistATypesPresenceCount[resId]] += 1                    
        return commonCount
                
    # Fan out the build - good for reports
    def lookupBuildEntriesByGIEN(self, gien):
        gienBuild = None
        for build in self.__dir["resources"]:
            if gien in build:
                gienBuild = build
                break
        if not gienBuild:
            return None
        entries = []
        for gien in gienBuild:
            entry = self.__dir["entries"][gien]
            entries.append(entry)
        return {"gien": gien, "entries": entries}
        
    # May be many copies across systems - just do [0] to get one
    def lookupBuildEntriesByName(self, buildName):
        entries = []
        for gien in self.__dir["entries"]:
            entry = self.__dir["entries"][gien]
            if entry[CommonBuildDirectory.ENTRY_IDX_NAME] == buildName:
                entries.append(entry)
        return entries      
               
    """
    Plan to support report with: top like file rep, time like user
    - hbar of total, excl, common, some
    - hbar of w/files (and can add w'routines later)
    - TODO: number of files covered by build system [could you rebuild a VistA]
    - common counts per vista, abs and perc ... excl, all, some
    """         
    def report(self, fileDirectory=None):        
        
        mu = "# Build Directory Synopsis\n\n"
        mu += f'VistAs: {len(self.__dir["vistas"]):,}' + "\n"
        
        # Graphics - top: topTotal - isHasBH
        ress = self.__dir["resources"]
        mu += f'Builds: {len(self.__dir["resources"]):,}' + "\n"
        cores = set(self.commonBuilds())
        mu += "Core (in all): {}\n".format(
            reportAbsAndPercent(len(cores), len(ress))
        )
        commonCount = self.commonCounts()
        mu += f'Common Builds: {"/".join([reportAbsAndPercent(commonCount[cnt], len(ress)) for cnt in sorted(commonCount) if cnt > 1])}' + "\n"
        exclBuilds = self.commonBuilds(count=1) # if they appear, are one
        mu += "Exclusive (in 1): {}\n".format(
            reportAbsAndPercent(len(exclBuilds), len(ress)),
        )
                
        # 1. First Bar up top breakdown [+ per VistA, will do in Graph]
        allBldsByGroup = {}
        for resId in exclBuilds:
            allBldsByGroup[resId] = "EXCLUSIVE"
        for resId in cores:
            allBldsByGroup[resId] = "ALL"
        for resId in self.buildIds():
            if resId in allBldsByGroup:
                continue
            allBldsByGroup[resId] = "SOME"
        if "SOME" in allBldsByGroup:
            mu += f"In Some (not just 1, not all): {reportAbsAndPercent(len(allBldsByGroup['SOME']), len(ress))}\n"
        
        # TODO: Can expand to have routines etc
        # ... 2. Second Bar up top
        mu += f'Have files: {reportAbsAndPercent(len(self.buildsWithFiles()), len(ress))}\n'
        entryDateByBuild = self.buildEntryDates()
        mu += f'Have Entry Dates: {reportAbsAndPercent(len(entryDateByBuild), len(ress))}\n'
        mu += f'Have packages: {reportAbsAndPercent(len(self.buildsWithPackage()), len(ress))}\n'        
        
        # Timing - will have builds by year (ala last bar in user or patient)
        countByYr = Counter()
        for resName in entryDateByBuild:
            yr = entryDateByBuild[resName].split("-")[0]
            countByYr[yr] += 1
        mu += "Builds by Year (of builds with entry date) ...\n"
        for yr in sorted(countByYr, key=lambda x: int(x)):
            mu += f"\t{yr}: {countByYr[yr]}\n"
        mu += "\n"
        
        # 3. TODO: 
        # expand out and see % of known files covered or addressed in builds
        mu += f'Files: {len(self.buildFiles())}\n'
        if fileDirectory:
            mu += f'\t% of all known: {reportAbsAndPercent(len(self.buildFiles()), len(fileDirectory.fileIds()))}\n'
        mu += f'RPCs: {len(self.buildRPCs())}\n' 
        mu += f'\tBuilds w/RPCs: {reportPercent(len(self.buildsWithRPCs()), len(self.__dir["resources"]))}\n'
        mu += f'Options: {len(self.buildOptions())}\n' 
        mu += f'\tBuilds w/Options: {reportPercent(len(self.buildsWithOptions()), len(self.__dir["resources"]))}\n'
        mu += f'Protocols: {len(self.buildProtocols())}\n' 
        mu += f'\tBuilds w/Protocols: {reportPercent(len(self.buildsWithProtocols()), len(self.__dir["resources"]))}\n'
        mu += f'HL7 LLs: {len(self.buildHL7LLs())}\n' 
        mu += f'\tBuilds w/HL7: {reportPercent(len(self.buildsWithHL7LLs()), len(self.__dir["resources"]))}\n'        
        mu += f'Routines: {len(self.buildRoutines())}\n' 
        mu += f'\tBuilds w/Routines: {reportPercent(len(self.buildsWithRoutines()), len(self.__dir["resources"]))}\n'               
        print(json.dumps(self.buildsWithHL7LLs()))
        # TODO: > one system etc?
        # TODO: could unify the 8994s and then do an "all known"?           
        mu += f'Packages: {len(self.buildPackages())}\n'
        for i, pkg in enumerate(self.buildPackages(), 1):
            mu += f"\t{i}. {pkg}\n"
        mu += "\n"
            
        mu += f'Definitions across VistAs: {len(self.__dir["entries"]):,}' + "\n"
        mu += "\n"
        for vistaInfo in self.__dir["vistas"]:
        
            stationNo = vistaInfo["stationNumber"]
            mu += f'## VistA {stationNo}\n' + "\n"
            
            ress = self.buildIds(stationNo)
            mu += f'Builds: {len(ress):,}' + "\n"
            commonCount = self.commonCounts(stationNo)
            mu += f'Common Builds: {"/".join([reportAbsAndPercent(commonCount[cnt], len(ress)) for cnt in sorted(commonCount) if cnt > 1])}' + "\n"
            exclBuilds = set(self.commonBuilds(stationNo, count=1))
            mu += "Exclusive (in 1): {}\n".format(
                reportAbsAndPercent(len(exclBuilds), len(ress)),
            )
            mu += "\n" 
                
        return mu
        
    # ----------------- Build Ids and Presence across VistAs -------------------
            
    def buildIds(self, stationNo=""):
        """
        All builds known or just per VistA - rem id is name
        
        For Plot: enables a isHasBH - total builds and then can give % with different 
        attributes using other methods below (emptyBuildIds)
        """
        resNames = []
        if stationNo:
            for entry in self.__entriesByVistA(stationNo):
                resNames.append(entry[CommonBuildDirectory.ENTRY_IDX_NAME])
        else:    
            for res in self.__dir["resources"]:
                # assuming all in res have same id == name
                entry = self.__dir["entries"][res[0]]
                resNames.append(entry[CommonBuildDirectory.ENTRY_IDX_NAME])
        return sorted(resNames)
        
    def commonBuilds(self, stationNo="", count=0, mustHaveFiles=False, mustHaveRPCs=False): 
        """
        # 0 == ALL
            ie/ commonBuilds(stationNo) <=> allBuilds([stationNo])
        # 1 == Exclusive (ie/ not common at all)
            ie/ commonBuilds(stationNo, 1) <=> exclusiveBuilds([stationNo])
        where stationNo being set limits the list to builds in a particular vista
        
        # > 1 BUT < len(vistas) => mix ie/ not exclusive and not all
        """
        inCount = []
        count = count or len(self.__dir["vistas"])
        for res in self.__dir["resources"]:
            if len(res) != count: # relies on builds only once in any vista
                continue
            if stationNo and sum(1 for b in res if b.split(":")[0] == stationNo) == 0:
                continue
            resEntry = self.__dir["entries"][res[0]]
            if mustHaveFiles and len(resEntry[CommonBuildDirectory.ENTRY_IDX_FILES]) == 0:
                continue
            if mustHaveRPCs and len(resEntry[CommonBuildDirectory.ENTRY_IDX_RPCS]) == 0:
                continue
            resName = resEntry[CommonBuildDirectory.ENTRY_IDX_NAME]
            inCount.append(resName)
        return inCount
        
    # Only one package
    def buildsWithPackage(self):
        wPackages = []
        for res in self.__dir["resources"]:
            bentry = self.__dir["entries"][res[0]]
            if bentry[CommonBuildDirectory.ENTRY_IDX_PACKAGE]:
                resName = bentry[CommonBuildDirectory.ENTRY_IDX_NAME]
                wPackages.append(resName)
        return wPackages
    
    def buildPackages(self):
        allPKGs = set()
        for gien in self.__dir["entries"]:
            bentry = self.__dir["entries"][gien]
            pkg = bentry[CommonBuildDirectory.ENTRY_IDX_PACKAGE]
            if pkg == "":
                continue
            allPKGs.add(pkg)
        return sorted(list(allPKGs))

    def buildsWithFile(self, fileId):
        return self.__buildsWithEntity(fileId, CommonBuildDirectory.ENTRY_IDX_FILES) 
        
    def buildFiles(self):
        return self.__buildEntities(CommonBuildDirectory.ENTRY_IDX_FILES)

    def buildsWithFiles(self):
        return self.__buildsWithEntities(CommonBuildDirectory.ENTRY_IDX_FILES)

    def buildsWithRPC(self, rpcName):
        return self.__buildsWithEntity(rpcName, CommonBuildDirectory.ENTRY_IDX_RPCS) 
        
    def buildRPCs(self):
        return self.__buildEntities(CommonBuildDirectory.ENTRY_IDX_RPCS)

    def buildsWithRPCs(self):
        return self.__buildsWithEntities(CommonBuildDirectory.ENTRY_IDX_RPCS)
    
    def buildsWithOption(self, optionName):
        return self.__buildsWithEntity(optionName, CommonBuildDirectory.ENTRY_IDX_OPTIONS) 
        
    def buildOptions(self):
        return self.__buildEntities(CommonBuildDirectory.ENTRY_IDX_OPTIONS)

    def buildsWithOptions(self):
        return self.__buildsWithEntities(CommonBuildDirectory.ENTRY_IDX_OPTIONS)
        
    def buildsWithProtocol(self, protocolName):
        return self.__buildsWithEntity(protocolName, CommonBuildDirectory.ENTRY_IDX_PROTOCOLS) 
        
    def vistasWithProtocolInBuild(self, protocolName):
        return self.__vistasWithEntity(protocolName, CommonBuildDirectory.ENTRY_IDX_PROTOCOLS)
        
    # TBD - ex/ Parameter GMRC IFC REGIONAL ROUTER file (#8989.5) to configure 
    # where post Cerner IFCs go
    def buildsWithParameterDefinition(self, parameterName):
        return self.__buildsWithEntity(protocolName, CommonBuildDirectory.ENTRY_IDX_PARAMETER_DEFINITIONS)        
        
    def buildProtocols(self):
        return self.__buildEntities(CommonBuildDirectory.ENTRY_IDX_PROTOCOLS)

    def buildsWithProtocols(self):
        return self.__buildsWithEntities(CommonBuildDirectory.ENTRY_IDX_PROTOCOLS)
        
    def buildsWithRoutine(self, routineName):
        return self.__buildsWithEntity(routineName, CommonBuildDirectory.ENTRY_IDX_ROUTINES) 
        
    def buildRoutines(self):
        return self.__buildEntities(CommonBuildDirectory.ENTRY_IDX_ROUTINES)

    def buildsWithRoutines(self):
        return self.__buildsWithEntities(CommonBuildDirectory.ENTRY_IDX_ROUTINES)

    def buildsWithHL7LL(self, hl7LLName):
        return self.__buildsWithEntity(hl7LLName, CommonBuildDirectory.ENTRY_IDX_HL7LLS) 
        
    def buildHL7LLs(self):
        return self.__buildEntities(CommonBuildDirectory.ENTRY_IDX_HL7LLS)

    def buildsWithHL7LLs(self):
        return self.__buildsWithEntities(CommonBuildDirectory.ENTRY_IDX_HL7LLS)
        
    def buildsWithHL7AP(self, hl7APName):
        return self.__buildsWithEntity(hl7APName, CommonBuildDirectory.ENTRY_IDX_HL7APS) 
        
    def buildHL7APs(self):
        return self.__buildEntities(CommonBuildDirectory.ENTRY_IDX_HL7APS)

    def buildsWithHL7APs(self):
        return self.__buildsWithEntities(CommonBuildDirectory.ENTRY_IDX_HL7APS)
        
    # A/Cs for older versions from some sys's not having all data. Tries
    # get a version with data
    def __buildsWithEntity(self, entityName, entityIndex):
        bldNames = []
        for res in self.__dir["resources"]:
            for resRef in res:
                bentry = self.__dir["entries"][resRef]
                if len(bentry) < entityIndex + 1:
                    bentry = None
                    continue
                break
            if bentry == None:
                continue
            if len(bentry[entityIndex]) == 0: # allow for older dirs with less info
                continue
            if isinstance(entityName, Pattern):
                if sum(1 for e in bentry[entityIndex] if entityName.search(e)) == 0:
                    continue
            else:
                if entityName not in bentry[entityIndex]:
                    continue
            resName = bentry[CommonBuildDirectory.ENTRY_IDX_NAME]
            bldNames.append(resName)
        return bldNames 
       
    # Ex/ all VistA's with a build with a particular protocol  
    def __vistasWithEntity(self, entityName, entityIndex):
        vistas = set()
        for gien in self.__dir["entries"]:
            sno = gien.split(":")[0]
            if sno in vistas:
                continue # got already
            bentry = self.__dir["entries"][gien]
            if len(bentry) < entityIndex + 1:
                continue
            entitys = bentry[entityIndex]
            if len(entitys) == 0:
                continue
            if entityName not in entitys:
                continue
            vistas.add(sno)
        return sorted(vistas)
        
    # Crude across all reprs of builds - if some reprs old and lack
    # certain data, shouldn't matter
    def __buildEntities(self, entityIndex):
        allEntities = set()
        for gien in self.__dir["entries"]:
            bentry = self.__dir["entries"][gien]
            if len(bentry) < entityIndex + 1:
                continue
            entitys = bentry[entityIndex]
            if len(entitys) == 0:
                continue
            allEntities |= set(entitys)
        return sorted(list(allEntities))

    def __buildsWithEntities(self, entityIndex):
        wEntities = []
        for res in self.__dir["resources"]:
            for resRef in res:
                bentry = self.__dir["entries"][resRef]
                if len(bentry) < entityIndex + 1:
                    bentry = None
                    continue
                break
            if bentry == None:
                continue
            if len(bentry[entityIndex]):
                resName = bentry[CommonBuildDirectory.ENTRY_IDX_NAME]
                wEntities.append(resName)
        return wEntities
        
    """
    Dates by Build Name
    
    Expecting consistency of entry dates - ie/ one per build
    
    Note: will go with build install per VistA dates
    """
    def buildEntryDates(self):
        entryDateOfBuild = {}
        warning = defaultdict(dict)
        for res in self.__dir["resources"]:
            resDT = ""
            for gien in res:
                entry = self.__dir["entries"][gien]
                resName = entry[CommonBuildDirectory.ENTRY_IDX_NAME]
                dt = entry[CommonBuildDirectory.ENTRY_IDX_DATE_DISTRIBUTED]
                if dt:
                    if resDT:
                        if resDT != dt:
                            warning["DATE_DISAGREE"][resName] = f'{resDT} vs {dt}'
                            if dt < resDT:
                                resDT = dt
                    else:
                        resDT = dt
                        entryDateOfBuild[resName] = dt    
                elif resDT:
                    warning["DATE_THERE_AND_NOT"][resName] = entry[CommonBuildDirectory.ENTRY_IDX_SNO]
        if len(warning):
            print(f'** Warning: for date extractions out of {len(self.__dir["resources"])}, {sum(len(warning[wt]) for wt in warning)} warnings happen')
        return entryDateOfBuild
    
    # -------------------------- Utilities etc --------------------------
        
    def __entriesByVistA(self, stationNo):
        return [self.__dir["entries"][gid] for gid in self.__dir["entries"] if re.match(stationNo, gid)]
        
    # TODO: timing stuff is ever get to 9_4, 9_6 - see old Archives
             
    # ########################## CHANGE / UPDATE ######################
                        
    def __changeUpdate(self):
        changed = self.__fillFromAvailable()
        if changed:
            print("Changed - so rebuilding builds")
            self.__rebuildBuilds()
            self.__flush()    
                             
    def __fillFromAvailable(self):
    
        def loadStationBuilds(stationNo):
    
            dataLocn = "{}{}/Data/".format(VISTA_DATA_BASE_DIR, stationNo)   
            resourceIter = FilteredResultIterator(dataLocn, "9_6")
            resourceEntry = []
            fileAssertionMismatchCounter = Counter()
            wFiles = 0
            wRPCs = 0
            for resource in resourceIter:
                """
                Add:
                - build components
                - multiple build
                - required build
                # DO: build_components - 
                """
                flIds = []
                if "file" in resource:
                    fls = sorted(list(set(mult["ien"] for mult in resource["file"])), key=lambda x: float(x))         
                    flIds = sorted(list(set(mult["file"]["id"].split("-")[1] for mult in resource["file"] if "file" in mult)), key=lambda x: float(x))
                    wFiles += 1
                    if len(set(flIds) - set(fls)):
                        raise Exception("If iens and fl pointers differ then expect iens to be the superset")
                    if flIds != fls:
                        fileAssertionMismatchCounter[len(fls) - len(flIds)] += 1
                rpcs = []
                options = []
                protocols = []
                hl7LLs = []
                routines = []
                if "build_components" in resource:
                    for bc in resource["build_components"]:
                        if "build_component" not in bc:
                            continue
                        if bc["build_component"]["id"] == "1-8994": # RPC
                            if "entries" not in bc:
                                continue
                            wRPCs += 1
                            for entry in bc["entries"]:
                                rpcName = entry["entries"]
                                # action = entry["action"] # SEND etc - ignore for now
                                rpcs.append(rpcName)
                            continue
                        if bc["build_component"]["id"] == "1-19": # OPTION
                            if "entries" not in bc:
                                continue
                            for entry in bc["entries"]:
                                optionName = entry["entries"]
                                # action = entry["action"] # SEND etc - ignore for now
                                options.append(optionName)
                            continue
                        if bc["build_component"]["id"] == "1-101": # PROTOCOL
                            if "entries" not in bc:
                                continue
                            for entry in bc["entries"]:
                                protocolName = entry["entries"]
                                # action = entry["action"] # SEND etc - ignore for now
                                protocols.append(protocolName)
                            continue
                        # TODO: consider the two other HL7 (779_2 == app registry and 771 application parameter)
                        if bc["build_component"]["id"] == "1-870": # HL7 LL
                            if "entries" not in bc:
                                continue
                            for entry in bc["entries"]:
                                hl7LLName = entry["entries"]
                                # action = entry["action"] # SEND etc - ignore for now
                                hl7LLs.append(hl7LLName)
                            continue
                        if bc["build_component"]["id"] == "1-9.8": # Routine
                            if "entries" not in bc:
                                continue
                            for entry in bc["entries"]:
                                routineName = entry["entries"]
                                # action = entry["action"] # SEND etc - ignore for now
                                routines.append(routineName)
                            continue
                rresource = [
                    stationNo,
                    resource["_id"].split("-")[1],
                    resource["name"],
                    resource["date_distributed"]["value"] if "date_distributed" in resource else "",
                    resource["package_file_link"]["label"] if "package_file_link" in resource else "",
                    resource["type_2"].split(":")[0] if "type_2" in resource else "",
                    resource.get("description_of_enhancements", ""),
                    resource.get("track_package_nationally", ""),
                    flIds, # taking subset of mults - these ones exist in 1/DD
                    rpcs,
                    options,
                    protocols,
                    hl7LLs,
                    routines
                ]
                self.__dir["entries"][f'{stationNo}:{rresource[1]}'] = rresource
            if wFiles and len(fileAssertionMismatchCounter):
                print(f"** Warning {stationNo}: 'file' pointer missing from {fileAssertionMismatchCounter} of the {wFiles} entries with files") 
            
        changed = False
        for stationNo in self.__vistaSNOs:
            if sum(1 for vistaInfo in self.__dir["vistas"] if vistaInfo["stationNumber"] == stationNo):
                print("\t{} already in Directory - skipping".format(stationNo))
                continue
            try:
                loadStationBuilds(stationNo)
            except Exception as e:
                print(e)
                print("{} can't be loaded as no 9_6 ...".format(stationNo))
                continue
            changed = True
            self.__dir["vistas"].append(
                {
                    "stationNumber": stationNo, 
                    "dateAdded": str(datetime.now()).split(" ")[0]
                }
            )
        return changed
                
    def __rebuildBuilds(self): # Just doing top builds for now
        del self.__dir["resources"]
        buildEntryGIDsByName = defaultdict(list)
        for gid in self.__dir["entries"]:
            entry = self.__dir["entries"][gid]
            buildEntryGIDsByName[entry[CommonBuildDirectory.ENTRY_IDX_NAME]].append(
                f'{entry[CommonBuildDirectory.ENTRY_IDX_SNO]}:{entry[CommonBuildDirectory.ENTRY_IDX_ID]}'
            )
        self.__dir["resources"] = [sorted(buildEntryGIDsByName[resName]) for resName in sorted(buildEntryGIDsByName)]
        buildsWGT1EntryInStation = sum(1 for res in self.__dir["resources"] if len(set(b.split(":")[0] for b in res)) != len(res))
        if buildsWGT1EntryInStation:
            raise Exception(f"Can't rebuild as {buildsWGT1EntryInStation} builds have > 1 entry in some VistA")
        print(f'From {len(self.__dir["entries"]):,}, isolated {len(self.__dir["resources"]):,} distinct builds')
        
    # => won't keep descr in all etc. BUT still not too big!
    # ... want descr, date etc same OR note if > 1 form
    def _makeNormalizedEntries(self):
        pass
        
    def __flush(self):
        print("Builds {:,}, Entries {:,} flushed".format(len(self.__dir["resources"]), len(self.__dir["entries"])))
        json.dump(
            self.__dir, 
            open(self.__dirFile, "w"), 
            indent=4
        )
        
"""
A quick dump utility to use as I expand the 9_6 info taken and QA

Gets into issues with builds for better dir:
- not all content noted in structured info
- allusions to missing structure in descriptions
- nonsense descriptions (see Forum etc -- reduce those pro-formas)
ie/ need to BULK up builds in Phase 2 of Directory
"""
def dumpRawBuild9_6s(stationNo, buildIds=[], keywords=[]):
    if len(keywords):
        keywordsRE = f'({"|".join(keywords)})'
    dataLocn = "{}{}/Data/".format(VISTA_DATA_BASE_DIR, stationNo)   
    resourceIter = FilteredResultIterator(dataLocn, "9_6")
    print(f"Dumping builds {buildIds}")
    for resource in resourceIter:
        if len(buildIds) and "name" in resource and resource["name"] in buildIds:
            print(f'# Build Id Match: {resource["name"]}\n\n')
            print(json.dumps(resource, indent=4))
            print()
            continue
        if len(keywords) and "description_of_enhancements" in resource and re.search(keywordsRE, resource["description_of_enhancements"], re.IGNORECASE):
            matchedKW = re.search(keywordsRE, resource["description_of_enhancements"], re.IGNORECASE).group(1)
            print(f'# Keyword in Description Match: {matchedKW}\n\n')
            print(json.dumps(resource, indent=4))
            print()            
                
# ############################## DRIVER ##########################
                
def main():

    assert sys.version_info >= (3, 6)
    
    visn20VistAs = vistasOfVISN("20")
    print(f'Building with {visn20VistAs}')
    fileDirectory = CommonFileDirectory(visn20VistAs)
    cbd = CommonBuildDirectory(visn20VistAs, dirPrefixLetter="B")
    print(cbd.report(fileDirectory=fileDirectory))
            
if __name__ == "__main__":
    main() 