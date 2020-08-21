

function logica_modal_excluir_info_idioma(){
	
	$('.modal-exclusao-msg-erro-id').html('');

	var id = $('#modal-exclusao-int-id').val();

	if(id === null || id.trim() == ''){

		$(".modal-exclusao-msg-erro-id").html('<span style="color:red;">Por favor, preencha o campo de \'id\'.</span>');

		$('#modal-exclusao-int-id').focus();

		return false;

	}

	$.ajax({

		url: 'http://localhost:5000/excluir_info_idioma',
		type: 'GET',
		data: "id="+id,
		async: false,
		fail: function(){
			alert("Ocorreu um erro inesperado, tente novamente mais tarde.")
		},
		success: function(info_recebida){

			if(info_recebida["resultado"] == 'ok'){

				$('#modal-exclusao-txt-nome').val('');
				$('.modal-exclusao-msg-erro-id').html('');
				
				$('.modal-exclusao-msg-resultado').html('<span style="color:green;">Informações deletadas com sucesso!</p>');

			} else {

				$('.modal-exclusao-msg-resultado').html('<span style="color:red;">Não foi possível deletar as informações, tente novamente.</span>');

			}

		}

	});

}

function logica_modal_incluir_info_idioma(){

	// restaura as mensagens de erro para saber quais são os atuais.
	$('.modal-inclusao-msg-erro-nome').html('');
	$('.modal-inclusao-msg-erro-dificuldade').html('');
	$('.modal-inclusao-msg-erro-popularidade').html('');
	$('.modal-inclusao-msg-resultado').html('');
	
	var nome = $('#modal-inclusao-txt-nome').val();
	var dificuldade = $('#modal-inclusao-ddi-dificuldade').val();
	var popularidade = $('#modal-inclusao-ddi-popularidade').val();

	var falhou = false;

	if(nome === null || nome.trim() == ''){

		$(".modal-inclusao-msg-erro-nome").html('<span style="color:red;">Por favor, preencha o campo de \'nome\'.</span>');

		$('#modal-inclusao-txt-nome').focus();

		falhou = true;

	}

	if (dificuldade === null || dificuldade.trim() == 'Opções ...'){

		$(".modal-inclusao-msg-erro-dificuldade").html('<span style="color:red;">Por favor, escolha uma opção do campo \'dificuldade\'.</span>');

		$('#modal-inclusao-ddi-dificuldade').focus();
		
		falhou = true;

	}

	if (popularidade === null || popularidade.trim() == 'Opções ...'){

		$(".modal-inclusao-msg-erro-popularidade").html('<span style="color:red;">Por favor, escolha uma opção do campo \'popularidade\'.</span>');

		$('#modal-inclusao-ddi-popularidade').focus();

		falhou = true;

	}

	if (falhou){
		return false;
	}

	$.ajax({

		url: 'http://localhost:5000/incluir_info_idioma',
		type: 'POST',
		data: JSON.stringify({nome, dificuldade, popularidade}),
		contentType: 'application/json; charset=utf-8',
		dataType: 'json',
		async: false,
		fail: function(){
			alert("Ocorreu um erro inesperado, tente novamente mais tarde.")
		},
		success: function(info_recebida){

			if(info_recebida["resultado"] == 'ok'){

				$('#modal-inclusao-txt-nome').val('');
				$('#modal-inclusao-ddi-dificuldade').val('Opções ...');
				$('#modal-inclusao-ddi-popularidade').val('Opções ...');
				$('.modal-inclusao-msg-erro-nome').html('');
				$('.modal-inclusao-msg-erro-dificuldade').html('');
				$('.modal-inclusao-msg-erro-popularidade').html('');
				
				$('.modal-inclusao-msg-resultado').html('<span style="color:green;">Informações cadastradas com sucesso!</p>');

			} else {

				$('.modal-inclusao-msg-resultado').html('<span style="color:red;">Ocorreu um erro, tente novamente.</span>');

			}

		}

	});

}

function logica_modal_alterar_info_idioma(){

	// restaura as mensagens de erro para saber quais são os atuais.
	$('.modal-alteracao-msg-erro-id').html('');
	$('.modal-alteracao-msg-erro-nome').html('');
	$('.modal-alteracao-msg-erro-dificuldade').html('');
	$('.modal-alteracao-msg-erro-popularidade').html('');
	$('.modal-alteracao-msg-resultado').html('');
	
	var id = $('#modal-alteracao-int-id').val();
	var nome = $('#modal-alteracao-txt-nome').val();
	var dificuldade = $('#modal-alteracao-ddi-dificuldade').val();
	var popularidade = $('#modal-alteracao-ddi-popularidade').val();

	var falhou = false;

	if(id === null || id.trim() == ''){

		$(".modal-alteracao-msg-erro-id").html('<span style="color:red;">Por favor, preencha o campo de \'id\'.</span>');

		$('#modal-alteracao-int-id').focus();

		falhou = true;

	}

	if(nome === null || nome.trim() == ''){

		$(".modal-alteracao-msg-erro-nome").html('<span style="color:red;">Por favor, preencha o campo de \'nome\'.</span>');

		$('#modal-alteracao-txt-nome').focus();

		falhou = true;

	}

	if (dificuldade === null || dificuldade.trim() == 'Opções ...'){

		$(".modal-alteracao-msg-erro-dificuldade").html('<span style="color:red;">Por favor, escolha uma opção do campo \'dificuldade\'.</span>');

		$('#modal-alteracao-ddi-dificuldade').focus();
		
		falhou = true;

	}

	if (popularidade === null || popularidade.trim() == 'Opções ...'){

		$(".modal-alteracao-msg-erro-popularidade").html('<span style="color:red;">Por favor, escolha uma opção do campo \'popularidade\'.</span>');

		$('#modal-alteracao-ddi-popularidade').focus();

		falhou = true;

	}

	if (falhou){
		return false;
	}

	$.ajax({

		url: 'http://localhost:5000/alterar_info_idioma',
		type: 'GET',
		data: 'id='+id,
		async: false,
		fail: function(){
			alert("Ocorreu um erro inesperado, tente novamente mais tarde.")
		},
		success: function(info_recebida){

			// objeto existe, logo pode enviar as informações
			if(info_recebida["resultado"] == 'ok'){

				$.ajax({

					url: 'http://localhost:5000/alterar_info_idioma',
					type: 'POST',
					data: JSON.stringify({nome, dificuldade, popularidade, id}),
					contentType: 'application/json; charset=utf-8',
					dataType: 'json',
					async: false,
					fail: function(){
						alert("Ocorreu um erro inesperado, tente novamente mais tarde.")
					},
					success: function(info_recebida){

						if(info_recebida["resultado"] == 'ok'){

							$('#modal-alteracao-int-id').val('');
							$('#modal-alteracao-txt-nome').val('');
							$('#modal-alteracao-ddi-dificuldade').val('Opções ...');
							$('#modal-alteracao-ddi-popularidade').val('Opções ...');
							$('.modal-alteracao-msg-erro-nome').html('');
							$('.modal-alteracao-msg-erro-dificuldade').html('');
							$('.modal-alteracao-msg-erro-popularidade').html('');
							
							$('.modal-alteracao-msg-resultado').html('<span style="color:green;">Informações alteradas com sucesso!</p>');

						} else {

							$('.modal-alteracao-msg-resultado').html('<span style="color:red;">Não foi possível alterar as informações, tente novamente.</span>');

						}

					}

				});

			} else {

				$('.modal-alteracao-msg-resultado').html('<span style="color:red;">Não existe um objeto com esse identificador.</span>');

			}

		}

	});
	
}

function logica_tabela_listar_info_idioma(){

	$.ajax({

		url: 'http://localhost:5000/listar_info_idiomas',
		method: 'GET',
		dataType: 'json',
		async: false,
		error: function(){
			alert("Erro na leitura dos dados. Possível má formação de dados desde o back-end.");
		},
		success: function(info_recebida){

			linhas = "";

			for (var i in info_recebida) {

				linha = "<tr>" +
				"<th>" + info_recebida[i].id + "</th>" +
				"<td>" + info_recebida[i].nome + "</td>" +
				"<td>" + info_recebida[i].dificuldade + "</td>" +
				"<td>" + info_recebida[i].popularidade + "</td>" +
				"</tr>";

				linhas = linhas + linha;

			}

			$("#tabela-idiomas-corpo-um").html(linhas);

			$("#mensagem-entrada-home").addClass("invisible");

			$("#tabela-idiomas").removeClass("invisible");

		}

	});

}

$(document).ready(function(){

	// modal inclusão de informações
	$("#btn-enviar-form-inclusao-info-idioma").click(logica_modal_incluir_info_idioma);

	// modal alteração de informações
	$("#btn-enviar-form-alteracao-info-idioma").click(logica_modal_alterar_info_idioma);

	// modal exclusão de informações
	$("#btn-enviar-form-exclusao-info-idioma").click(logica_modal_excluir_info_idioma);

	$("#mensagem-entrada-home").removeClass("invisible");

	$("#link-listar-info-idioma").click(logica_tabela_listar_info_idioma);

});