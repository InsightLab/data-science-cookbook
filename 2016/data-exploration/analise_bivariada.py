# -*- coding: utf-8 -*-
from analises import *


temperature = [83, 64, 72, 81, 70, 68, 65, 75, 71, 85, 80, 72, 69, 75]
humidity = [86, 65, 90, 75, 96, 80, 70, 80, 91, 85, 90, 95, 70, 70]

print 'Covariance: ', correlacao_linear.covariance(temperature, humidity)
print 'Correlation: ', correlacao_linear.correlation(temperature, humidity)