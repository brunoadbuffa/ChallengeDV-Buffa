import numpy as np
np.seterr(all='raise')
from scipy.spatial.distance import cdist, euclidean

def k_meansMODIF(X, k, tol=1e-4, n_iter=50):
    n_samples, n_dim = X.shape    
    # D² weighting initialization
    centroids = D2weighting(X, k)
    prev_centroids = centroids.copy()
    distortion, prev_distortion = 0., 1e6
    for i in range(n_iter):
        assignments = np.argmin(cdist(X, centroids),1)
        centroids = np.array([np.mean(X[assignments == l], 0) for l in range(k)])
        
        #calculo del error y la distorsión
        error = sum([euclidean(centroids[j], prev_centroids[j]) for j in range(k) ])
        distortion = 0.
        for j in range(n_samples):
            distortion += euclidean(X[j], centroids[assignments[j]])
        distortion /= n_samples
        #Chequeamos si se cumplen alguno de los 2 criterios de parada (AQUÍ AGREGUÉ EL USO DE LA DISTORSION)
        if ((prev_distortion - distortion) / (prev_distortion + 2**-23)) < tol or error < tol:
            print('done')
            break
        prev_distortion , prev_centroids = distortion, centroids
    print('iterations ={}, error ={:.3e}'.format(i+1, distortion))
    return centroids, error, distortion

def D2weighting(X, k):
    centroids = X[np.random.choice(range(X.shape[0]), size=1)]
    for j in range(1, k):
        D = np.min(cdist(X, centroids, metric='sqeuclidean'),1) #D=[D(x1)² D(x2)²...D(xn)²] (dist² de c/x al centroide más cercano) 
        pvals = D / sum(D) #arreglo con las prob de cada x de convertirse en el próximo centroide
        centroids = np.vstack([centroids, X[np.where(np.random.multinomial(1,pvals))[0]]]) #agrego el nuevo centroide como fila de centroids
    return centroids
    
