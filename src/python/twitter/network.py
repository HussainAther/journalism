import numpy as np
import os
import pandas as pd
import psycopg2
import re
import seaborn as sns
import tqdm
from wordcloud import WordCloud

from sqlalchemy import create_engine
frmo postgres_credentials import *

"""
Visualizing Twitter followers.
"""

