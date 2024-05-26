# --------------------------------------------------------------
# kmeans.py
# k-means-Clustering
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 1
# Michael Weigend 18.9.2023
# --------------------------------------------------------------
körpergrößen = [123, 107, 178, 100, 99,
                156, 178, 172, 112, 145, 133, 171, 118]
c1 = körpergrößen[0]
c2 = körpergrößen[1]
cluster1 = []
fertig = False

while not fertig:
    altesCluster1 = cluster1
    cluster1 = []
    cluster2 = []
    for g in körpergrößen:
        if (g-c1)**2 < (g-c2)**2:
            cluster1 += [g]
        else:
            cluster2 += [g]
    c1 = sum(cluster1)/len(cluster1)
    c2 = sum(cluster2)/len(cluster2)
    print('Cluster 1:', cluster1)
    print('Cluster 2:', cluster2)
    fertig = cluster1 == altesCluster1

print('Größe 1:', round(c1),'cm,',
      'Größe 2:', round(c2),'cm')
input()        
    
