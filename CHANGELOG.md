# v0.58 - 2014-08
   * gristle_dir_merger
     - initial addition to toolkit.  Merges directories of files using a variety
       of matching criteria and matching actions.   

# v0.57 - 2014-07
   * gristle_processor
     - initial addition to toolkit.  Provides ability to scan through directory
       structure recursively, and delete files that match config criteria.

# v0.56 - 2014-03

   * gristle_determinator
     - added hasnoheader arg
     - fixed problem printing top_values on empty file with header
   * gristle_validator
     - added hasnoheader arg
   * gristle_freaker
     - added hasnoheader arg

# v0.55 - 2014-02

   * gristle_determinator - fixed a few problems:
     - the 'Top Values not shown - all unique' message being truncated
     - floats not handled correctly for stddev & variance
     - quoted ints & floats not handled

# v0.54 - 2014-02

   * gristle_validator - major updates to allow validation of csv files based on
     the json schema standard, with help from the Validictory module.

# v0.53 - 2014-01

   * gristle_freaker - major updates to enable distributes on all columns to be
     automatically gathered through either (all or each) args.   'All' combines
     all columns into a single tuple prior to producing distribution.  'Each'
     creates a separate distribution for every column within the csv file.
   * travisci - added support and started using this testing service.
