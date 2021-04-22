function eliminarAlumno(nocontrol){
    if(confirm('¿ Estas seguro de eliminar al edificio:'+nocontrol+'?'))
        location.href='/alumnos/delete/'+nocontrol;
}

