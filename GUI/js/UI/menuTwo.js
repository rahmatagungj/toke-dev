export default function menuTwo(){
	var menuTwo = new Vue({
		el: '#menu-two',
		data: {
			show: true,
			text_file_location: 'File Location',
			text_placeholder_file_location: 'path to file',
			button_file_location: 'Browse',
			text_output_location: 'Output Location',
			text_placeholder_output_location: 'path to output file',
			button_output_location: 'Browse',
			text_security_key: 'Security Key',
			text_output_filename: 'Output Filename',
			text_email: 'Email',
			text_email_checkbox: 'Send results to email',
			text_result: 'RESULT',
			text_button_execute: 'ENCRYPT NOW'
		},
		components: {
			'badgenew': {
				template: '<span class="badge bg-success">New</span>'
			}
		},
		methods: {
			fileEncrypt: function(){
				get_file()
			},
			fileEncryptOutput: function(){
				get_file_output()
			},
			encrypt: function(){
				js_encrypt_now()
			}
		}
	})
}