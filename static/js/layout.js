const cabecera = document.querySelector('cabecera');
const detalles = document.querySelector('detalles');
const eliminar = document.getElementById('ej');


window.onload=function traer() {
    fetch("./password")
        .then(res => res.json())
        .then(datos => {
            if (Object.keys(datos).length === 0){
                cont.innerHTML+=
                ` 
                <h1> No hay DB! </h1>
                
                ` 
            }else{
                tabla(datos)
            }
            
        })
}

function tabla(datos) {



    for (let valor of datos) {

        var usuario = valor.usu
        var fecha = valor.fecha
        var password = valor.password
        var id = valor.id
        var pag = valor.pag

        contenido.innerHTML += `   

                <tr scope="row" >
                    
                    <td  id=${id} onclick="copiar('${id}')">${id}</td>
                    <td id=${pag} onclick="copiar('${pag}')">${pag}</td> 
                    <td id=${usuario} onclick="copiar('${usuario}')">${usuario}</td> 
                    <td id=${password} onclick="copiar('${password}')">${password}</td> 
                    <td id=${fecha} onclick="copiar('${fecha}')">${fecha}</td> 
                </tr>
                
                `

    }
    var btnAceptar = document.getElementById("cargar");
    var disableButton = function () { this.disabled = true; };
    btnAceptar.addEventListener('click', disableButton, true);


}

function copiar(lo_que_copias) {


    if (window.clipboardData && window.clipboardData.setData) {
        // IE: prevent textarea being shown while dialog is visible
        return window.clipboardData.setData("Text", lo_que_copias);

    } else if (document.queryCommandSupported &&
        document.queryCommandSupported("copy")) {
        var textarea = document.createElement("textarea");
        textarea.textContent = lo_que_copias;
        // Prevent scrolling to bottom of page in MS Edge
        textarea.style.position = "fixed";
        document.body.appendChild(textarea);
        textarea.select();
        try {
            // Security exception may be thrown by some browsers
            return document.execCommand("copy");
        } catch (ex) {
            console.warn("Copy to clipboard failed.", ex);
            return false;
        } finally {
            document.body.removeChild(textarea);
        }
    }
}

function formulario() {
    
    if(eliminar.childElementCount===1)
    {
        var elemen= document.getElementById('formu')
        elemen.parentNode.removeChild(elemen)
        
    }
    else{
    
        eliminar.innerHTML+=
        ` 
        <form  id="formu" action="#" method="POST">

        <h2 class="titulo">Delete page</h2>
        <br>
        <input type="text" name="borrar" id="borrar" placeholder="Page"/></br>
        <input type="text" name="borrar_usu" id="borrar_usu" placeholder="User (Optinal)"/></br>
        <input type="submit" value="Delete" />
        <br>

        </form>
        ` 
    }



}



