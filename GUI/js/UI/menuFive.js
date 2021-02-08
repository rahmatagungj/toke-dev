export default function menuFour(){
	 var menuFour = new Vue({
	 	el: '#menu-five',
	 	data: {
	 		show: true,
			text_tools: 'Tools',
			button_connection: 'Check Connection',
			button_update: 'Check Update',
			button_version: 'Check Version',
			button_coming_soon: 'Coming soon'
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
			}
		}
	 })
}