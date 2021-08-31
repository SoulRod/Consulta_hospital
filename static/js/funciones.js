// Funcion para validar las edades correspondientes de cada pacientes / activar y desactivar inputs

function validarEdad(valor){
    if(valor > 40){
        input2 = document.getElementById('caja2')
        input2.type = "text";
        input2.disabled = false
        input4 = document.getElementById('caja4')
        input4.type = "hidden";
        input4.disabled = true
        input5 = document.getElementById('caja5')
        input5.type = "hidden";
        input5.disabled = true
    }
    if(valor <= 40 && valor > 15){
        input2 = document.getElementById('caja2')
        input2.type = "hidden";
        input2.disabled = true
        input3 = document.getElementById('caja3')
        input3.type = "text";
        input3.disabled = false
        input4 = document.getElementById('caja4')
        input4.type = "hidden";
        input4.disabled = true
        input5 = document.getElementById('caja5')
        input5.type = "hidden";
        input5.disabled = true
    }
    if(valor >= 0 && valor <= 15 ){
        input2 = document.getElementById('caja2')
        input2.type = "hidden";
        input2.disabled = true
        input3 = document.getElementById('caja3')
        input3.type = "hidden";
        input3.disabled = true
        input4 = document.getElementById('caja4')
        input4.type = "text";
        input4.disabled = false
        input5 = document.getElementById('caja5')
        input5.type = "text";
        input5.disabled = false
    }
    if(valor == ""){
        input2 = document.getElementById('caja2')
        input2.type = "hidden";
        input2.disabled = true
        input3 = document.getElementById('caja3')
        input3.type = "hidden";
        input3.disabled = true
        input4 = document.getElementById('caja4')
        input4.type = "hidden";
        input4.disabled = true
        input5 = document.getElementById('caja5')
        input5.type = "hidden";
        input5.disabled = true
    }
}