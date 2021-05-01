import pandas as pd
from selenium import webdriver
import time
import re


def find_disulphide_bonds(input_file, output_file):
    """
	Find the probable Di-Sulphide Bonds in the given Domain sequences.
    
	:param input_file: Name of the input file which contains list of Domains (IRDs).
	:type input_file: string

	:param output_file: Name of the output file in which Domains along with Di-Sulphide Bonds found in them are saved.
	:type output_file: string

    """
    input_file = 'pinpy/data/'+input_file
    output_file = 'pinpy/data/output/'+output_file
    # print(input_file,output_file)

    domainsDF = pd.read_csv(input_file)
    outputFields = ['DomainID', 'Domain', 'DSBonds', 'BondsCount', 'ConfidenceInterval']
    dsBondsDF = pd.DataFrame(columns=outputFields)  # Creating the output Data Frame for storing Disulphide Bonds details
    # print(domainsDF)
    # print(dsBondsDF)

    # Iterating through the Domains
    for index, row in domainsDF.iterrows():
        '''
        Here using the Chrome browser driver we will open the webpage:[http://disulfind.disi.unitn.it/];set the 
        Amino Sequence control of the web page with Domain sequence and automatically submit it; and once the results i.e. 
        disulphide bonds in the sequence are displayed, we will retrieve it and save it in dsBondsDF Data Frame.
        '''
        # Reading Chrome Driver
        driver = webdriver.Chrome('C:\chromedriver.exe')
        print(driver)
        # Opening the Webpage
        driver.get('http://disulfind.disi.unitn.it/')
        # Reading the page element Query Name
        pageElement = driver.find_element_by_name('idseq')
        # Setting the Page Element Query Name with Domain ID
        pageElement.send_keys(row['domainID'])
        # Reading Page Element Amino Acid Sequence
        pageElement = driver.find_element_by_name('aaseq')
        # Setting the Page Element Amino Acid Sequence with actual sequence
        pageElement.send_keys(row['domain'].strip())
        # Reading Page Element Submit Button
        pageElement = driver.find_element_by_name('submit')
        # Clicking the submit button
        pageElement.click()
        # Sleeping to allow processing of webpage
        time.sleep(25)
        # Reading the Tag 'pre' of the webpage and saving its text in temp
        tag = driver.find_element_by_tag_name('pre')
        tagText = tag.text
        # print(tagText)
        dsBondList = []
        dsBondCount = 0
        confInterval = 0.0
        # Using Regular Expression to find 'DB_bond' labels in tag 'pre' data saved in tagText
        for label in re.finditer('DB_bond', tagText):
            # print(label)
            dsBondCount = dsBondCount + 1
            sPos = label.end() + 3
            ePos = label.end() + 14
            dsBondList.append(tagText[sPos:ePos].rstrip())
            # ';'.join(dsBondList)
            # print(dsBondList)
            # print(dsBondCount)
        # Using Regular Expression to find 'Conn_conf' labels in tag 'pre' data saved in tagText
        for label2 in re.finditer('Conn_conf', tagText):
            # print(m.start(),m.end())
            sPos = label2.end() + 1
            ePos = label2.end() + 9
            confInterval = tagText[sPos:ePos]
            # print(confInterval)
        # Building the final Record list to be saved in Output File
        record = [row['domainID'], row['domain'].strip(), dsBondList, dsBondCount, confInterval]
        # print(record)
        # Updating the output dsBonds data frame
        dsBondsDF = dsBondsDF.append({'DomainID': row['domainID'], 'Domain': row['domain'], 'DSBonds': dsBondList,
                                    'BondsCount': dsBondCount, 'ConfidenceInterval': confInterval}, ignore_index=True)
        driver.close()
    print(dsBondsDF)
    # Finally saving the dsBonds data Frame in the Output file
    dsBondsDF.to_csv(outputFile, index=False)