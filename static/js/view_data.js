'Use strict';

async function viewTable(idTable){
    let tbls = ['tbl-medical','tbl-car', 'tbl-house','tbl-life']
    let container = document.getElementById('container-data');
    let text = document.getElementById('text-tbl-no-data');
    let table = document.getElementById(idTable);
    
    for(let i =0; i < tbls.length; i++){
        if (idTable != tbls[i]){
            let tableNot = document.getElementById(tbls[i]);
            tableNot.style.display = 'none';
            tableNot.style.display = 'hidden';
            tableNot.style.transition = 'all 0.5s ease-in-out';
        }
        
    }
    

    container.style.flexDirection = 'inherit';
    text.style.display = 'none';
    text.style.visibility = 'hidden';
    table.style.display = "block";
    table.style.visibility = "visible";
    table.style.transition = 'all 0.5s ease-in-out';

}
function openViewFinder(id_form) {

    let visor = document.getElementById('conte-view-form');
    let btn = document.getElementById('btn-cerrar')
    let form = document.getElementById(id_form);
    
    form.style.display = "block";
    form.style.visibility = "visible";
    form.style.width = '80%';
    form.style.margin = '0px auto';
    form.style.height = '100%';
    visor.style.display = "block";
    visor.style.visibility = "visible";
    visor.style.width = '50%';
    visor.style.height = '80%';
    visor.style.transition = 'all 0.5s ease-in-out';
    btn.style.display = 'flex';
}

async function cerrarVisor(id_form) {
    let conteVisor = document.getElementById('conte-view-form');
    let form = document.getElementById(id_form);
    
    form.style.display = "none";
    form.style.visibility = "hidden";
    conteVisor.style.width = '0px';
    conteVisor.style.height = '0px';
    conteVisor.style.display = "none";
    conteVisor.style.visibility = "hidden";
    conteVisor.style.transition = 'all 0.5s ease-in-out';
    habilitar('header');
    habilitar('section-home');
    habilitar('section-contact-about-me');
    habilitar('footer');
}





async function ViewForm(id_form) {
    let visor = document.getElementById('container-forms-add')
    let btn = document.getElementById('btn-cerrar')
    let form = document.getElementById(id_form);

    form.style.display = "flex";
    form.style.visibility = "visible";
    form.style.width = '100%';
    form.style.height = '100%';
    visor.style.display = "flex";
    visor.style.visibility = "visible";
    visor.style.width = '30%';
    visor.style.height = '80%';
    visor.style.transition = 'all 0.5s ease-in-out';
    btn.style.display = 'flex';
    
}

async function cerrarFormHome(id_form) {
    let conteVisor = document.getElementById('container-forms-add');
    let form = document.getElementById(id_form);
    
    form.style.display = "none";
    form.style.visibility = "hidden";
    conteVisor.style.width = '0px';
    conteVisor.style.height = '0px';
    conteVisor.style.display = "none";
    conteVisor.style.visibility = "hidden";
    conteVisor.style.transition = 'all 0.5s ease-in-out';
    habilitar('header');
    habilitar('section-home');
    habilitar('section-contact-about-me');
    habilitar('footer');
}

function deshabilitar(elemento) {
    let elementoPadre = document.getElementById(elemento);
    //elementoPadre.setAttribute("class", );
    elementoPadre.classList.add("deshabilitado");
    let backBlock = document.createElement("div");
    backBlock.setAttribute("id", "backloader");
    backBlock.style.position = "fixed";
    backBlock.style.display = "inline-block";
    backBlock.style.width = "100%";
    backBlock.style.height = "100%";
    backBlock.style.top = "0";
    backBlock.style.bottom = "0";
    backBlock.style.left = "0";
    backBlock.style.right = "0";
    backBlock.style.opacity = "15%";
    backBlock.style.background = "grey";
    elementoPadre.appendChild(backBlock);
}


function habilitar(elemento) {
    let elementoPadre = document.getElementById(elemento);
    let backloader = document.getElementById("backloader");
    elementoPadre.classList.remove("deshabilitado");
    elementoPadre.removeChild(backloader);
    



}


function viewOptionLogout(){
    let container =  document.getElementById("container-option-main-user");
    container.style.display = "block";
    container.style.visibility = "visible";


    
}