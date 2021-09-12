
function Precaucion(mensaje) {
    texto = '<p class="alertas-msg" >' + mensaje + '</p>';
    titulo = '<p class="alertas-titulo" >' + 'AVISO' + '</p>';
    Swal.fire({ 
        title: titulo,
        html: texto,
        icon: 'warning',
        confirmButtonText: 'Ok',
        confirmButtonColor: 'var(--color-resalte)',
        background: 'var(--color-fondo)',
        backdrop: false,
        width: '18rem',
        heightAuto: false,
        
    })

}

function succesesMessageTop(mensaje) {
    texto = '<p class="alertas-msg" >' + mensaje + '</p>';
    titulo = '<p class="alertas-titulo" >' + 'Hecho' + '</p>';
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: titulo,
        showConfirmButton: false,
        timer: 1500
    })
}

/* function succesesMessage(mensaje) {
    texto = '<p class="alertas-msg" >' + mensaje + '</p>';
    titulo = '<p class="alertas-titulo" >' + 'Hecho' + '</p>';
    Swal.fire({
        position: 'top-end',
        title: titulo,
        html: texto,
        icon: 'success',
        iconColor:'#06B056',
        confirmButtonText: 'Ok',
        confirmButtonColor: 'var(--color-resalte)',
        background: 'var(--color-fondo)',
        backdrop: false,
        width: '18rem',
        heightAuto: false,
    })
} */

function error(mensaje) {
    texto = '<p class="alertas-msg" >' + mensaje + '</p>';
    titulo = '<p class="alertas-titulo" >' + 'ERROR' + '</p>';
    Swal.fire({
        title: titulo,
        html: texto,
        icon: 'error',
        iconColor: '#C52C03',
        confirmButtonText: 'OK',
        confirmButtonColor: 'var(--color-resalte)',
        background: 'var(--color-fondo)',
        backdrop: false,
        width: '18rem',
        heightAuto: false,
    })


}

function error(mensaje) {
    texto = '<p class="alertas-msg" >' + mensaje + '</p>';
    titulo = '<p class="alertas-titulo" >' + 'ERROR' + '</p>';
    Swal.fire({
        title: titulo,
        html: texto,
        icon: 'error',
        iconColor: '#C52C03',
        confirmButtonText: 'OK',
        confirmButtonColor: 'var(--color-resalte)',
        background: 'var(--color-fondo)',
        backdrop: false,
        width: '18rem',
        heightAuto: false,
    })


}



