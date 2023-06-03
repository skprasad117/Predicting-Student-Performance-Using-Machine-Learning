# ******************************************************************
# * Data Transformation : Main purpose is to do                    *
# *                       -> Data Cleaning                         *
# *                       -> convert cat to num, etc.              *
# ******************************************************************
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer  # create pipeline for ohc or standardscaling, if want to use in form of pipeline
from sklearn.impute import SimpleImputer # for missing data
from sklearn.pipeline import pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor