Datagristle is a toolbox of tough and flexible data connectors and
analyzers.
It's kind of an interactive mix between ETL and data analysis optimized
for rapid analysis and manipulation of a wide variety of data.

It's neither an enterprise ETL tool, nor an enterprise analysis,
reporting, or data mining tool. It's intended to be an easily-adopted
tool for technical analysts that combines the most useful subset of data
transformation and analysis capabilities necessary to do 80% of the
work. Its open source python codebase allows it to be easily extended to
with custom code to handle that always challenging last 20%.

Current Status: Strong support for easy analysis, simple transformations
of csv files, and ability to create data dictionaries.

More info is on the DataGristle wiki here:
https://github.com/kenfar/DataGristle/wiki

Next Steps:
===========

-  attractive PDF output of gristle\_determinator.py
-  metadata database population

Its objectives include:
=======================

-  multi-platform (unix, linux, mac os, windows with effort)
-  multi-language (primarily python)
-  free - no cripple-licensing
-  primary audience is programming data analysts - not non-technical
   analysts
-  primary environment is command-line rather than windows, graphical
   desktop or eclipse
-  extensible
-  allow a bi-directional iteration between ETL & data analysis
-  can quickly perform initial data analysis prior to longer-duration,
   deeper analysis with heavier-weight tools.

Installation
============

-  Using `pip <http://www.pip-installer.org/en/latest/>`_ (preferred) or
   `easyinstall <http://peak.telecommunity.com/DevCenter/EasyInstall>`_:

   \ :sub:`~`\  $ pip install datagristle $ easy\_install datagristle
   \ :sub:`~`\ 

-  Or install manually from
   `pypi <https://pypi.python.org/pypi/datagristle>`_:

   \ :sub:`~`\  $ mkdir ~$ wget
   https://pypi.python.org/packages/source/d/datagristle/datagristle-0.51.tar.gz
   $ tar -xvf easy\_install datagristle $ cd ~-\* $ python setup.py
   install \ :sub:`~`\ 

Dependencies
============

-  Python 2.6 or Python 2.7

Mature Utilities Provided in This Release:
==========================================

-  gristle\_slicer

   -  Used to extract a subset of columns and rows out of an input file.

-  gristle\_freaker

   -  Produces a frequency distribution of multiple columns from input
      file.

-  gristle\_viewer

   -  Shows one record from a file at a time - formatted based on
      metadata.

-  gristle\_determinator

   -  Identifies file formats, generates metadata, prints file analysis
      report
   -  This is the most mature - and also used by the other utilities so
      that you generally do not need to enter file structure info.

gristle\_slicer
===============

::

    Extracts subsets of input files based on user-specified columns and rows.
    The input csv file can be piped into the program through stdin or identified
    via a command line option.  The output will default to stdout, or redirected
    to a filename via a command line option.

    The columns and rows are specified using python list slicing syntax -
    so individual columns or rows can be listed as can ranges.   Inclusion
    or exclusion logic can be used - and even combined.

    Examples:
       $ gristle_slicer sample.csv
                    Prints all rows and columns
       $ gristle_slicer sample.csv -c":5, 10:15" -C 13
                    Prints columns 0-4 and 10,11,12,14 for all records
       $ gristle_slicer sample.csv -C:-1
                    Prints all columns except for the last for all records
       $ gristle_slicer sample.csv -c:5 -r-100
                    Prints columns 0-4 for the last 100 records
       $ gristle_slicer sample.csv -c:5 -r-100 -d'|' --quoting=quote_all
                    Prints columns 0-4 for the last 100 records, csv
                    dialect info (delimiter, quoting) provided manually)
       $ cat sample.csv | gristle_slicer -c:5 -r-100 -d'|' --quoting=quote_all
                    Prints columns 0-4 for the last 100 records, csv
                    dialect info (delimiter, quoting) provided manually)

gristle\_freaker
================

::

    Creates a frequency distribution of values from columns of the input file
    and prints it out in columns - the first being the unique key and the last 
    being the count of occurances.


    Examples:
       $ gristle_freaker sample.csv -d '|'  -c 0
                    Creates two columns from the input - the first with
                    unique keys from column 0, the second with a count of
                    how many times each exists.
       $ gristle_freaker sample.csv -d '|'  -c 0 --sortcol 1 --sortorder forward --writelimit 25
                    In addition to what was described in the first example, 
                    this example adds sorting of the output by count ascending 
                    and just prints the first 25 entries.
       $ gristle_freaker sample.csv -d '|'  -c 0 --sampling_rate 3 --sampling_method interval
                    In addition to what was described in the first example,
                    this example adds a sampling in which it only references
                    every third record.
       $ gristle_freaker sample.csv -d '|'  -c 0,1
                    Creates three columns from the input - the first two
                    with unique key combinations from columns 0 & 1, the 
                    third with the number of times each combination exists.
       $ gristle_freaker sample.csv -d '|'  -c -1
                    Creates two columns from the input - the first with unique
                    keys from the last column of the file (negative numbers 
                    wrap), then a second with the number of times each exists.
       $ gristle_freaker sample.csv -d '|'  --columntype all
                    Creates two columns from the input - all columns combined
                    into a key, then a second with the number of times each
                    combination exists.
       $ gristle_freaker sample.csv -d '|'  --columntype each
                    Unlike the other examples, this one performs a separate
                    analysis for every single column of the file.  Each analysis
                    produces three columns from the input - the first is a 
                    column number, second is a unique value from the column, 
                    and the third is the number of times that value appeared.  
                    This output is repeated for each column.

gristle\_viewer
===============

::

    Displays a single record of a file, one field per line, with field names 
    displayed as labels to the left of the field values.  Also allows simple 
    navigation between records.

    Examples:
       $ gristle_viewer sample.csv -r 3 
                    Presents the third record in the file with one field per line
                    and field names from the header record as labels in the left
                    column.
       $ gristle_viewer sample.csv -r 3  -d '|' -q quote_none
                    In addition to what was described in the first example this
                    adds explicit csv dialect overrides.

gristle\_determinator
=====================

::

    Analyzes the structures and contents of csv files in the end producing a 
    report of its findings.  It is intended to speed analysis of csv files by
    automating the most common and frequently-performed analysis tasks.  It's
    useful in both understanding the format and data and quickly spotting issues.

    Examples:
       $ gristle_determinator japan_station_radiation.csv
                    This command will analyze a file with radiation measurements
                    from various Japanese radiation stations.

        File Structure:
        format type:       csv
        field cnt:         4
        record cnt:        100
        has header:        True
        delimiter:                   
        csv quoting:       False   
        skipinitialspace:  False    
        quoting:           QUOTE_NONE  
        doublequote:       False   
        quotechar:         "       
        lineterminator:    '\n'    
        escapechar:        None    

        Field Analysis Progress: 
        Analyzing field: 0
        Analyzing field: 1
        Analyzing field: 2
        Analyzing field: 3

        Fields Analysis Results: 

            ------------------------------------------------------
            Name:             station_id           
            Field Number:     0                    
            Wrong Field Cnt:  0                    
            Type:             timestamp            
            Min:              1010000001           
            Max:              1140000006           
            Unique Values:    99                   
            Known Values:     99                   
            Top Values not shown - all values are unique

            ------------------------------------------------------
            Name:             datetime_utc         
            Field Number:     1                    
            Wrong Field Cnt:  0                    
            Type:             timestamp            
            Min:              2011-02-28 15:00:00  
            Max:              2011-02-28 15:00:00  
            Unique Values:    1                    
            Known Values:     1                    
            Top Values: 
                2011-02-28 15:00:00                      x 99 occurrences

            ------------------------------------------------------
            Name:             sa                   
            Field Number:     2                    
            Wrong Field Cnt:  0                    
            Type:             integer              
            Min:              -999                 
            Max:              52                   
            Unique Values:    35                   
            Known Values:     35                   
            Mean:             2.45454545455        
            Median:           38.0                 
            Variance:         31470.2681359        
            Std Dev:          177.398613681        
            Top Values: 
                41                                       x 7 occurrences
                42                                       x 7 occurrences
                39                                       x 6 occurrences
                37                                       x 5 occurrences
                46                                       x 5 occurrences
                17                                       x 4 occurrences
                38                                       x 4 occurrences
                40                                       x 4 occurrences
                45                                       x 4 occurrences
                44                                       x 4 occurrences

            ------------------------------------------------------
            Name:             ra                   
            Field Number:     3                    
            Wrong Field Cnt:  0                    
            Type:             integer              
            Min:              -888                 
            Max:              0                    
            Unique Values:    2                    
            Known Values:     2                    
            Mean:             -556.121212121       
            Median:           -888.0               
            Variance:         184564.833792        
            Std Dev:          429.610095077        
            Top Values: 
                -888                                     x 62 occurrences
                0                                        x 37 occurrences

gristle\_metadata
=================

::

    Gristle_metadata provides a command-line interface to the metadata database.
    It's mostly useful for scripts, but also useful for occasional direct
    command-line access to the metadata.

    Examples:
       $ gristle_metadata --table schema --action list
                    Prints a list of all rows for the schema table.
       $ gristle_metadata --table element --action put --prompt
                    Allows the user to input a row into the element table and 
                    prompts the user for all fields necessary.

gristle\_md\_reporter
=====================

::

    Gristle_md_reporter allows the user to create data dictionary reports that
    combine information about the collection and fields along with field value
    descriptions and frequencies.

    Examples:
       $ gristle_md_reporter --report datadictionary --collection_id 2
                    Prints a data dictionary report of collection_id 2.
       $ gristle_md_reporter --report datadictionary --collection_name presidents
                    Prints a data dictionary report of the president collection.
       $ gristle_md_reporter --report datadictionary --collection_id 2 --field_id 3
                    Prints a data dictionary report of the president collection,
                    only shows field-level information for field_id 3.

Licensing
=========

-  Gristle uses the BSD license - see the separate LICENSE file for
   further information

Copyright
=========

-  Copyright 2011,2012,2013 Ken Farmer