$(function(){
   //sacar los mensajes de error
    $("errorEmail").hide();
    $("errorRunUsuario").hide();
    $("errorNombreUsuario").hide();
    $("errorFecnac").hide();
    $("errorTelefonoUs").hide();
    $("errorVivienda").hide();
    
    //variables que indican valor de estado validacion
    var error_email = false;
    var error_run = false;
	var error_nombrecompleto = false;
	var error_tefcontac = false;
	var error_fecden = false;
	var error_vivienda = false;
	
    
    $("#errorEmail").focusout(function() {

		check_email();
		
	});

	$("#errorRunUsuario").focusout(function() {

		check_run();
		
	});

	$("#errorNombreUsuario").focusout(function() {

		check_nombrecompleto();
		
	});

	$("#errorFecnac").focusout(function() {

		check_fecden();
	});

	$("#errorTelefonoUs").focusout(function() {

		check_tefcontac();

	});	

	$("#errorVivienda").focusout(function() {

		check_vivienda();

	});

		function check_email() {

		var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
	
		if(pattern.test($("#Email").val())) {
			$("#errorEmail").hide();
		} else {
			$("#errorEmail").html("Direccion inválida ");
			$("#errorEmail").show();
			error_email = true;
		}
	
	}
    
    function check_run() {
	
		var run_length = $("#RunUsuario").val().length;
		
		if(run_length < 8 || run_length > 10) {
			$("#errorRunUsuario").html("Run no tiene los digitos correspondientes");
			$("#errorRunUsuario").show();
			error_run = true;
		} else {
			$("#errorRunUsuario").hide();
		}
	
	}

	function check_nombrecompleto() {
	
		var nombrecompleto_length = $("#NombreUsuario").val().length;
		
		if(nombrecompleto_length < 10 || nombrecompleto_length > 40) {
			$("#errorNombreUsuario").html("Tiene que tener entre 10 y 40 letras");
			$("#errorNombreUsuario").show();
			error_nombrecompleto = true;
		} else {
			$("#errorNombreUsuario").hide();
		}
	
	}

	function check_fecden() {
	
      var RegExPattern = /^\d{1,2}\/\d{1,2}\/\d{2,4}$/; /* Solo funciona si el formato es dd/mm/aaaaa */
      var fecha = "01/01/2001";

      if ((RegExPattern.test($("#Fecnac").val())) && ($("#Fecnac").val() > fecha)) {
            $("#errorFecnac").hide();
      } else {
      	 	$("#errorFecnac").html("Debe tener el formato y ser mayor a 2001");
            $("#errorFecnac").show();
            error_fecden = true;
      }
}

	function check_tefcontac() {
	
		var tefcontac_length = $("#TelefonoUs").val().length;
		
		if(tefcontac_length < 9 || tefcontac_length > 9) {
			$("#errorTelefonoUs").html("Debe tener 9 numeros");
			$("#errorTelefonoUs").show();
			error_tefcontac = true;
		} else {
			$("#errorTelefonoUs").hide();
		}
	
	}

	function check_vivienda() {

		if($("#vivienda option:selected").val() == 0) {
    		$("#errorVivienda").html("Seleccione una categoria");
			$("#errorVivienda").show();
			error_vivienda = true;
		} else {
			$("#errorVivienda").hide();
		}
	}

	// Funcion para que solo hayan letras en el nombre //
	function soloLetras(e){
       key = e.keyCode || e.which;
       tecla = String.fromCharCode(key).toLowerCase();
       letras = " áéíóúabcdefghijklmnñopqrstuvwxyz"; /* Se especifican las letras que solo aceptan */
       especiales = "8-37-39-46";

       tecla_especial = false
       for(var i in especiales){
            if(key == especiales[i]){
                tecla_especial = true;
                break;
            }
        }

        if(letras.indexOf(tecla)==-1 && !tecla_especial){
            return false;
        }
    }
	
	$("#registration_form").submit(function() {
											
		  error_email = false;
          error_run = false;
	      error_nombrecompleto = false;
	      error_fecden = false;
	      error_tefcontac = false;
	      error_vivienda = false;
	    
											
		check_email();
		check_run();
		check_nombrecompleto();
		check_fecden();
		check_tefcontac();
		check_vivienda();

		
		if(error_email == false && error_run == false && error_nombrecompleto == false && error_fecden == false  && error_tefcontac == false && error_vivienda == false) {
			return true;
		} else {
			return false;	
		}

	});



});