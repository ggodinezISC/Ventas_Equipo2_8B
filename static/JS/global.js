function eliminarAlumno(nocontrol){
    if(confirm('¿ Estas seguro de eliminar al edificio:'+nocontrol+'?'))
        location.href='/alumnos/delete/'+nocontrol;
}
function eliminarUsuario(id){
    if(confirm('¿ Estas seguro de eliminar el usuario: '+id))
        location.href='/usuarios/delete/'+id;
}
function eliminarPractica(id){
    if(confirm('¿ Estas seguro de eliminar la practica: '+id))
        location.href='/practicas/delete/'+id;
}
function eliminarLaboratorio(id){
    if(confirm('¿ Estas seguro de eliminar el laboratorio: '+id))
        location.href='/laboratorios/delete/'+id;
}
function eliminarBotiquin(id){
    if(confirm('¿ Estas seguro de eliminar el item del botiquin: '+id))
        location.href='/botiquines/delete/'+id;
}
function eliminarInventario(id){
    if(confirm('¿ Estas seguro de eliminar el equipo de inventario: '+id))
        location.href='/inventario/delete/'+id;
}
function eliminarLiquido(id){
    if(confirm('¿ Estas seguro de eliminar el liquido: '+id))
        location.href='/liquidos/delete/'+id;
}
function eliminarMaestro(id){
    if(confirm('¿ Estas seguro de eliminar el maestro: '+id))
        location.href='/maestros/delete/'+id;
}
function eliminarReactivo(id){
    if(confirm('¿ Estas seguro de eliminar el Reactivo: '+id))
        location.href='/reactivos/delete/'+id;
}
function eliminarPractica(id){
    if(confirm('¿ Estas seguro de eliminar la practica: '+id))
        location.href='/practicas/delete/'+id;
}
function eliminarMaterial(id){
    if(confirm('¿ Estas seguro de eliminar la instrumentacion: '+id+'?'))
        location.href='/materiales/delete/'+id;
}
