#import all the libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#dataframe
dataFrame = pd.read_csv('/home/zxc/newpp.xlsx')

#monthly data
location = dataFrame.iloc[:,:2]
jan = np.array(dataFrame['Jan'])
feb = np.array(dataFrame['Feb'])
mar = np.array(dataFrame['Mar'])
apr = np.array(dataFrame['Apr'])
may = np.array(dataFrame['May'])
jun = np.array(dataFrame['Jun'])
jul = np.array(dataFrame['Jul'])
aug = np.array(dataFrame['Aug'])
sep = np.array(dataFrame['Sep'])
Oct = np.array(dataFrame['Oct'])
nov = np.array(dataFrame['Nov'])
dec = np.array(dataFrame['Dec'])
ann = np.array(dataFrame['Ann'])

#definations
def rolling_avg(l, N):
    sum = 0
    result = list( 0 for x in l)

    for i in range( 0, N ):
        sum = sum + l[i]
        result[i] = sum / (i+1)

    for i in range( N, len(l) ):
        sum = sum - l[i-N] + l[i]
        result[i] = sum / N

    return result

#principal component analysis
def dimension_min(data, N):
    from sklearn.decomposition import PCA
    if(data.shape[1]>1):
        pca = PCA(n_components = N)
        return pca.fit_transform(data)
    else :
        return data

#spectral biclustuur for alpha and beta 
def SpectralBiCluster(data, n_clusters = (4,4)):
    from sklearn.datasets import make_checkerboard
    from matplotlib import pyplot as plt
    from sklearn.cluster.bicluster import SpectralBiclustering
    model = SpectralBiclustering(method='log', random_state=0)
    data = np.array(data)
    model.fit(data)
    fit_data = data[np.argsort(model.row_labels_)]
    fit_data = fit_data[:, np.argsort(model.column_labels_)]
    plt.matshow(fit_data, cmap=plt.cm.Blues)

#mixed type data model
def StatSum(data):
    from scipy import stats
    import statsmodels.api as sm
    import matplotlib.pyplot as plt
    from statsmodels.distributions.mixture_rvs import mixture_rvs
    kde = sm.nonparametric.KDEUnivariate(data)
    kde.fit()
    fig = plt.figure(figsize=(6,4))
    ax = fig.add_subplot(111)
    ax.hist(data, bins=50, normed=True, color='red')
    ax.plot(kde.support, kde.density, lw=2, color='black')

#
