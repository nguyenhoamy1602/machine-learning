#!/usr/bin/python

## @svm_json.py
#  This file contains methods to convert svm data to a JSON object.
import json, csv
from collections import defaultdict
from itertools import islice

## Class: JSON
class JSON:

  ## constructor
  def __init__(self, svm_file):
    self.svm_file = svm_file

  ## csv_to_json: convert csv file to JSON object
  #
  #  Note: we use the 'Universal Newline Support' with the 'U" parameter
  #        when opening 'self.svm_file'. This allows newlines to be
  #        understood regardless, if the newline character was created in
  #        osx, windows, or linux.
  def csv_to_json(self):
    list_dataset       = []
    list_dataset_label = []

    # open temporary 'csvfile'
    with open( self.svm_file, 'rU' ) as csvfile:
      stuff = csv.reader( csvfile, delimiter=' ', quotechar='|' )

      # iterate only first row of csvfile
      for row in islice( stuff, 0, 1 ):

        # row is a list with one comma-delimited string element
        row = row[0].split(',')
        for value in row:
          list_dataset_label.append( value )

      # iterate all other rows of csvfile (except first)
      for row in islice( stuff, 1, None ):

        # row is a list with one comma-delimited string element
        row = row[0].split(',')
        for index, value in enumerate( row ):
          list_dataset.append( {dict_dataset_label[index]: value} )

    #return json.dumps(columns)
    print list_dataset
  ## xml_to_json: convert xml to JSON object
  def xml_to_json(self):
    print 'dummy code'
