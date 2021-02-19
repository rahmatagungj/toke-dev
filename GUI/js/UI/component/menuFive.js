export default new Vue({
	el: '#menu-five',
	data: {
		show: true,
		text_tools: 'Tools',
		button_connection: 'Check Connection',
		button_update: 'Check Update',
		button_version: 'Check Version',
		button_system: 'Check System',
		button_style: 'btn btn-info',
		button_cmd: 'Open Terminal',
		button_notepad: 'Open Notepad',
		button_calc: 'Open Notepad',
		button_regedit: 'Open Regedit'
	},
	methods: {
		connection: function(){
			js_check_connection()
		},
		update: function(){
			js_check_update()
		},
		version: function(){
			js_check_version()
		},
		system: function(){
			js_check_system()
		},
		cmd: function(){
			eel.start_app('cmd')
		},
		notepad: function(){
			eel.start_app('notepad')
		},
		calc: function(){
			eel.start_app('calc')
		},
		regedit: function(){
			eel.start_app('regedit')
		}
	}
})