#!/usr/bin/env python

import os, re
import sys


for file in os.listdir("/home/sckao/usercode/GMSB_SLHA"):

    if ( re.match('GMSB', file ) ) :
       newfile = re.sub('pythia', 'pythia6', file )   
       #print (file, ' -> ',  newfile )
       cmd = 'mv %s %s' %( file , newfile) 
       print cmd  
       os.system( cmd )

