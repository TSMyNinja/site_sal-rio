from flask import *
from API import app, db
from .models import INSS, IPR

@app.route('/calculo', methods=['POST'])
def calculo():
    if(request.method =='POST'):
        sal = float(request.json["sal"])
        dep = int(request.json["dep"])
        desc = float(request.json["desc"])
        
        
        inss = INSS.query.filter(INSS.sal_min <= sal) or (INSS.sal_max >= sal)   
        for ins in inss:
            aliqinss = ins.aliquota/100
            deducao = ins.deducao       
        reajuste_inss = (sal*aliqinss)-float(deducao)  
        
        if (sal >= 1903.98):  
            salariobase = sal - reajuste_inss - (dep*189.59)
            irrf = IPR.query.filter(IPR.sal_min <= float(salariobase)) or (IPR.sal_max >= float(salariobase))
            for inf in irrf:
                aliqirrf = inf.aliquota/100
                deduirrf = inf.deducao 
            
            reajuste_ipr = round(abs(salariobase*aliqirrf)- float(deduirrf),2)
        else:
            reajuste_ipr = 0
        
        valor_final = round(abs(sal - (reajuste_inss + reajuste_ipr) - desc),2)

        descc = round(abs(reajuste_inss + reajuste_ipr + desc),2)
    
    
    return {"INSS": reajuste_inss , "IPR": reajuste_ipr, "Total": valor_final, "Descontos": descc}
    