# Script to calculate epistemic uncertainty (model uncertainty)

import numpy as np

def uq_ec(x,model,b_size,itr=10):
    pr = []
    
    for i in range(itr):
        p = model.predict(x,batch_size=b_size,verbose=0)
        pr.append(p.T)
        
    pr = np.array(pr)
    
    ep_uc = pr.std(axis=0)
    
    return ep_uc