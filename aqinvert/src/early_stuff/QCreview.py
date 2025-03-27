

# QC for aqinvert - followup from QC review

import pandas as pd
import matplotlib.pyplot as plt





df = pd.read_csv("aqinvert_counts_thru_2023.csv")


cols = ['RepCount']
df2 = df[df[cols] > 1000]
df2.hist(column='RepCount')

what were the > 1000 records



df = pd.read_csv("location_details.csv")

df['StretchNumber'].unique() 
array([ 24.,  55.,  59.,  69.,  73.,  87., 279., 481., 640., 441., 462.,
       403., 646., 229., 420., 638., 317., 242., 244., 367., 383., 225.,
       304., 232., 378., 472., 241., 300., 574., 649., 238., 694., 476.,
       484., 366., 603., 623., 275., 390.,  nan,  14.,  35.,  46.,  67.,
        71.,  97., 819., 850., 576., 920., 473., 917., 494., 657., 695.,
       711., 930., 950., 685., 463., 734., 856., 104., 114., 123., 907.,
       542., 699.])
	   
convert to integer


df = pd.read_csv("reach_coordinates.csv")

precision of lat/long


df = pd.read_csv("riffle_sample_details.csv")


ParkName         object
ParkCode         object
LocationID       object
PeriodID         object
EventID          object
RiffleNo          int64
Replicate        object
Width           float64
Depth           float64
Velocity        float64

Substrate       float64
Embeddedness    float64
Vegetation      float64  <<<<<<<<<<<<< categorical 0 integer values
Algae           float64
Periphyton      float64
Deposition      float64
Organics        float64

Notes            object
dtype: object


df = pd.read_csv("riffle_water_quality.csv")


cols = ['DO']
df2 = df[df[cols] > 0]
df2.hist(column='DO')

what parks are 14 -> 17





