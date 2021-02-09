export default function menuThere(){
	var menuThere = new Vue({
		el: '#menu-there',
		data: {
			show: true,
			text_file_location: 'File Location',
			text_placeholder_tl1e: 'path to file with extension TL1E',
			button_tl1e: 'Browse',
			text_placeholder_tl2e: 'path to file with extension TL2E',
			button_tl2e: 'Browse',
			text_output_location: 'Output Location',
			text_placeholder_output_location: 'path to output file',
			button_output_location: 'Browse',
			text_security_key: 'Security Key',
			text_output_filename: 'Output Filename',
			text_extension: 'Extension',
			text_result: 'RESULT',
			text_button_execute: 'DECRYPT NOW',
			button_file: {
				width: "100%"
			},
			no_resize: {
				resize: "none"
			}
		},
		methods: {
			getTL1E: function(){
				get_file_tl1e()
			},
			getTL2E: function(){
				get_file_tl2e()
			},
			outputFile: function(){
				get_file_output_decrypt()
			},
			decrypt: function(){
				js_decrypt_now()
			}
		}
	})
}