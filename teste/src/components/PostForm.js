import React from 'react'
import call from '../call'

function PostForm () {  
    const [data, setData] = React.useState({
    
    });
    
    async function submit (e){
        e.preventDefault();
        const {sal,desc,dep} = e.target
        console.log(sal.value)
        const dados ={
            sal: sal.value,
            desc: desc.value,
            dep: dep.value
        }
        console.log("formulario",dados)

        try {
          const  res = await call.post('/calculo',dados)
        console.log("apiRes",res)
        setData(res.data)  
        } catch(error){
            console.log(error)
        }   
    }   
        
     return(
        <div>
            <h1 className="title">
                Calculadora de Impostos
            </h1>
            <div >
               <form className="input" onSubmit={submit} >
                <h2>Salário</h2>
                <input className="box"
                required                
                name="sal"
                type="number"
                step=".01"/>

                <h2>Dependentes</h2>
                <input className="box2"
                required                
                name="dep"
                type="number"
                step=".01"/>

                <h2>Descontos</h2>
                <input className="box3"
                required           
                name="desc"
                type="number"
                step=".01"/>

                <button className="button" type="submit">Calcular</button>
            </form> 
            </div>
            <div>
                <table className="table">
                    <tbody>
                        <tr>
                            <th>INSS</th>
                            <th>IRPF</th>
                        </tr>               
                    </tbody>
                </table>
                <table className="table2">
                    <tbody>
                        <tr>
                            <th>R${data.INSS}</th>
                            <th>R${data.IPR}</th>
                        </tr>
                    </tbody>
                </table>
                <table className="table3">
                    <tbody>
                        <tr>
                            <th>Total</th>
                            <th>Salário</th>
                        </tr>
                    </tbody>                   
                </table>
                <table className="table4">
                    <tbody>
                        <tr>
                            <th>R${data.Descontos}</th>
                            <th className="resultado">R${data.Total}</th>
                        </tr>
                    </tbody>
                </table>
            </div>
            <h4 className="texto">Calcule aqui o seu salário liquido! Demostra como obter um valor de salário líquido a partir do salário bruto e dos descontos do salário (INSS e IRRF)</h4>
            
        </div>
        

    )   
   
}

export default PostForm