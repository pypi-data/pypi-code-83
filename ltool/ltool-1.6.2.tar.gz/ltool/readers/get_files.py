#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:03:44 2020

@author: nick
"""
import mysql.connector
import numpy as np
import os, glob, re

def database(meas_id, cfg):
    
    mydb = mysql.connector.connect(
      host=cfg.dtb['host'],
      user=cfg.dtb['user'],
      passwd=cfg.dtb['password'],
      port=cfg.dtb['port'],
      db=cfg.dtb['scc-db-name']
    )
    
    cur = mydb.cursor()
    
    # cur.execute("SELECT measurements.ID, products.ID, " +\
    #             "ltool_product_options._input_product_ID, " +\
    #             "ltool_product_options.dilation, " +\
    #             "ltool_product_options.snr_factor, " +\
    #             "ltool_product_options.wct_peak_margin, " +\
    #             "elda_products.filename FROM measurements INNER JOIN " +\
    #             "system_product INNER JOIN products INNER JOIN product_options " +\
    #             "INNER JOIN ltool_product_options INNER JOIN elda_products ON " +\
    #             "system_product._system_ID=measurements._hoi_system_ID AND " +\
    #             "system_product._Product_ID=products.ID AND " +\
    #             "product_options._product_ID=elda_products._product_ID AND " +\
    #             "products._ltool_product_option_ID=ltool_product_options.ID AND " +\
    #             "ltool_product_options._input_product_ID=elda_products._product_ID AND " +\
    #             "elda_products.__measurements__ID=measurements.ID WHERE " +\
    #             "products._prod_type_ID="+prod_type_id+" AND measurements.ID='" +\
    #             meas_id+"'")

    cur.execute("SELECT dilation, snr_factor, wct_peak_margin, " +\
                "ltool_product_options._product_ID, filename " +\
                "FROM ltool_product_options " +\
                "JOIN elda_products " +\
                "ON elda_products._product_ID=ltool_product_options._input_product_ID " +\
                "WHERE __measurements__ID='"+meas_id+"'")
    print("SELECT dilation, snr_factor, wct_peak_margin, " +\
                "ltool_product_options._product_ID, filename " +\
                "FROM ltool_product_options " +\
                "JOIN elda_products " +\
                "ON elda_products._product_ID=ltool_product_options._input_product_ID " +\
                "WHERE __measurements__ID='"+meas_id+"'")
    query = cur.fetchall()
    
    files = np.array([os.path.join(cfg.scc['input-dir'], x[4]) for x in query])
    
    rpath = np.array([os.path.split(x[4])[0] for x in query])

    alphas = np.array([x[0]/1000. for x in query])

    alphas[alphas == None] = 0.4

    snr_factor = np.array([x[1] for x in query])
    
    snr_factor[snr_factor == None] = 1.
        
    wct_peak_margin = np.array([x[2] for x in query])

    wct_peak_margin[wct_peak_margin == None] = 0.63
    
    ids = np.array([x[3] for x in query])
    
    cur.execute("SELECT products.ID, products._prod_type_ID  " +\
                "FROM measurements JOIN " +\
                "system_product JOIN products " +\
                "ON measurements._hoi_system_ID=system_product._system_ID " +\
                "AND system_product._Product_ID=products.ID " +\
                "WHERE products._prod_type_ID IN (10,11) " +\
                "AND  measurements.ID='"+meas_id+"'")
        
    print("SELECT products.ID, products._prod_type_ID  " +\
                "FROM measurements JOIN " +\
                "system_product JOIN products " +\
                "ON measurements._hoi_system_ID=system_product._system_ID " +\
                "AND system_product._Product_ID=products.ID " +\
                "WHERE products._prod_type_ID IN (10,11) " +\
                "AND  measurements.ID='"+meas_id+"'")

    query = cur.fetchall()
    
    ids_list = np.array([x[0] for x in query])
    prd_type = np.array([x[1] for x in query])

    typ = []    
    for i_d in ids:
        ind = np.where(ids_list == i_d)[0][0]
        typ.append(prd_type[ind])
    typ = np.array(typ)

    mydb.close()
    print(alphas,snr_factor,wct_peak_margin,typ,ids,rpath)
        
    return(files, rpath, alphas,snr_factor, wct_peak_margin, typ, ids)