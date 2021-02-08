async function get_file(){
	let path = await eel.pick_file('encrypt');
}

async function get_file_tl1e(){
	let path = await eel.pick_file('decrypt_tl1e');
}

async function get_file_tl2e(){
	let path = await eel.pick_file('decrypt_tl2e');
}

async function get_file_output(){
	let path = await eel.pick_file('output');
}

async function get_file_output_decrypt(){
	let path = await eel.pick_file('output_decrypt');
}

async function get_file_note(){
	let path = await eel.pick_file('note');
}

eel.expose(js_set_path);
function js_set_path(path){
	let file_div = document.getElementById('toPath');
	file_div.innerHTML = path;
	file_div.value = path;
}

function js_encrypt_now(){
	let fileE = document.getElementById('toPath').value;
	let keyE = document.getElementById('keyE').value;
	let filenameE = document.getElementById('filenameE').value;
	let emailE = document.getElementById('emailE').value;
	let fileEOutput = document.getElementById('toPathOutput').value;
	let sendEmail = document.getElementById("sendEmail");
	if (sendEmail.checked == true){
	    sendEmail = "yes";
	  } else {
	    sendEmail = "no";
	  }
	eel.encrypt_now(filenameE,fileE,keyE,emailE,sendEmail,fileEOutput)
}

eel.expose(js_set_path_tl1e);
function js_set_path_tl1e(path){
	let file_div = document.getElementById('toPathTL1E');
	file_div.innerHTML = path;
	file_div.value = path;
}

eel.expose(js_set_path_tl2e);
function js_set_path_tl2e(path){
	let file_div = document.getElementById('toPathTL2E');
	file_div.innerHTML = path;
	file_div.value = path;
}

eel.expose(js_set_path_output);
function js_set_path_output(path){
	let file_div = document.getElementById('toPathOutput');
	file_div.innerHTML = path;
	file_div.value = path;
}

eel.expose(js_set_path_output_decrypt);
function js_set_path_output_decrypt(path){
	let file_div = document.getElementById('toPathOutputDecrypt');
	file_div.innerHTML = path;
	file_div.value = path;
}

function js_decrypt_now(){
	let fileTL1E = document.getElementById('toPathTL1E').value;
	let fileTL2E = document.getElementById('toPathTL2E').value;
	let keyD = document.getElementById('keyD').value;
	let extensionD = document.getElementById('extensionD').value;
	let filenameD = document.getElementById('filenameD').value;
	let fileEOutputDecrypt = document.getElementById('toPathOutputDecrypt').value;
	eel.decrypt_now(filenameD,extensionD,fileTL1E,fileTL2E,keyD,fileEOutputDecrypt)
}

eel.expose(js_set_result_decrypt)
function js_set_result_decrypt(message){
	let elementLayer1 = document.getElementById('layer2');
	elementLayer1.value = message;
}

eel.expose(js_set_result)
function js_set_result(message){
	let elementLayer1 = document.getElementById('layer1');
	elementLayer1.value = message;
}

eel.expose(js_in_execute)
function js_in_execute(state) {
  $('button').prop('disabled', state);
}

function js_check_version(){
	eel.check_version()
}

// MODAL SHOW 
eel.expose(js_modal_error)
function js_modal_error(title,message){
	const options = {
	  settings: {
        duration: 3000,
      },
      style: {
        main: {
          background: "#e8505b",
          color: "#fff",
	      },
	  },
	};
	iqwerty.toast.toast(message, options);
}

eel.expose(js_modal_success)
function js_modal_success(title,message){
	const options = {
	  settings: {
        duration: 3000,
      },
      style: {
        main: {
          background: "#14b1ab",
          color: "#fff",
	      },
	  },
	};
	iqwerty.toast.toast(message, options);
}

eel.expose(js_modal_info)
function js_modal_info(title,message){
	const options = {
	  settings: {
        duration: 3000,
      },
      style: {
        main: {
          background: "#62959c",
          color: "#fff",
	      },
	  },
	};
	iqwerty.toast.toast(message, options);
}

eel.expose(js_modal_warning)
function js_modal_warning(title,message){
	const options = {
	  settings: {
        duration: 3000,
      },
      style: {
        main: {
          background: "#f9d56e",
          color: "#fff",
	      },
	  },
	};
	iqwerty.toast.toast(message, options);
}


// Security
function js_disable_right_click(){
	$(function() {
        $(this).bind("contextmenu", function(e) {
            e.preventDefault();
        });
    });
}

function js_disable_reload(){
	var ctrlKeyDown = false;

	$(document).ready(function(){    
	    $(document).on("keydown", keydown);
	    $(document).on("keyup", keyup);
	});

	function keydown(e) { 
	    if ((e.which || e.keyCode) == 116 || ((e.which || e.keyCode) == 82 && ctrlKeyDown)) {
	        e.preventDefault();
	    } else if ((e.which || e.keyCode) == 17) {
	        ctrlKeyDown = true;
	    }
	};

	function keyup(e){
	    if ((e.which || e.keyCode) == 17) 
	        ctrlKeyDown = false;
	};
}

// js_disable_reload()
// js_disable_right_click()

// $(document).on("contextmenu", function (e) {        
//     e.preventDefault();
// });

// $(document).keydown(function (event) {
//     if (event.keyCode == 123) { 
//         return false;
//     } else if (event.ctrlKey && event.shiftKey && event.keyCode == 73) {   
//         return false;
//     } else if (event.ctrlKey){
//     	return false;
//     } else if (eevent.shiftKey){
//     	return false
//     }
// });

// End Security

eel.expose(js_save_note)
function js_save_note(){
	let text = document.getElementById('textNote').value;
	eel.save_note(text)
}

eel.expose(js_set_note);
function js_set_note(text){
	let file_div = document.getElementById('textNote');
	file_div.innerHTML = text;
	file_div.value = text;
}

function js_check_connection(){
	document.getElementById('check-connection').innerHTML = 'Checking Connection';
	eel.check_connection();
}

eel.expose(js_set_check_connection)
function js_set_check_connection(status){
	document.getElementById('check-connection').innerHTML = 'Check Connection';
	js_modal_info('INFORMATION','You are '+ status)
}

function js_check_update(){
	document.getElementById('check-update').innerHTML = 'Checking Update';
	eel.tools_check_update();
}

eel.expose(js_set_check_update)
function js_set_check_update(status){
	js_modal_info('INFORMATION','You are '+ status)
}

eel.expose(js_restore_update)
function js_restore_update(){
	document.getElementById('check-update').innerHTML = 'Check Update';
	js_modal_info('INFORMATION',"The application is up to date.")
}

eel.expose(js_show_startup_update)
function js_show_startup_update(version){
	document.getElementById('check-update').innerHTML = 'Check Update';
	js_modal_info('INFORMATION',"A new version "+ version +" is available, we recommend updating \n  to the latest version.")
}

// GOOGLE ANALITYC

window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-W4140HYN2D');