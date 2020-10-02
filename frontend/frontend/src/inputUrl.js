import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import MaterialTable from 'material-table'

const InputUrl = (props) => {
  const [Url, setUrl] = useState(null);
  const [relacionadas, setRelacionadas] = useState(null);

  // Pegar valor do input e colocar no state para posteriormente ser enviado ao backend
  const handleChange = (event) => {

    setUrl(event.target.value);
  }

  //Realizar o POST da informação para o backend
  const handlePost = () => {
    //Parte de validação, csrfToken removida para primeira versão
    let endpoint = 'http://localhost:8000/crawler/'
    let data = Url;
    let lookupOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: data,
    }
    fetch(endpoint, lookupOptions)
      .then(function (response) {
        return response.json()
      })
      .then(function (responseData) {
        if (responseData !== null) {
          setRelacionadas(responseData.resultado)
        }
      })
      .catch(function (error) {
        console.log('error', error)
        alert('Um erro aconteceu ao tentar gravar a url - ' + error)
      })
  }


  const InputRender = () => {
    return (
      <div>
        <TextField name='inputUrl' id='inputUrl' variant='outlined' label='Url' style={{ width: '100%' }} onChange={handleChange} defaultValue='' />

        <Button className='button' type='button' onClick={handlePost} variant='contained' color='primary'>Get!</Button>
        {relacionadas !== null && relacionadas.length > 0 ?
          <div className='table'>
            <MaterialTable
              columns={[
                { title: 'Links Relacionados', field: 'link' },
              ]}
              data={relacionadas}
              title="Tabela de Url's"
            />
          </div>
          :
          <div></div>
        }


      </div>
    );
  }

  return (
    InputRender()
  )

}

export default InputUrl;