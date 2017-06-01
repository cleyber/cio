$(document)
    .ready(function() {
      $('.ui.form')
        .form({
          fields: {
            name: {
              identifier  : 'name',
              rules: [
                {
                  type   : 'empty',
                  prompt : 'Por favor introduzca su nombre'
                }
              ]
            },
            password: {
              identifier  : 'password',
              rules: [
                {
                  type   : 'empty',
                  prompt : 'Por favor introduzca su contraseña'
                },
                {
                  type   : 'length[6]',
                  prompt : 'Su contraseña debe tener al menos 6 caracteres'
                }
              ]
            }
          }
        })
      ;
    })
  ;
