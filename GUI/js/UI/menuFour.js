export default function menuFour(){
	 var menuFour = new Vue({
	 	el: '#menu-four',
	 	data: {
			show: true,
			text_editor: 'Text Editor',
			button_open: 'OPEN',
			button_save: 'SAVE'
		},
		methods:{
			openFile: function(){
				get_file_note()
			},
			saveFile: function(){
				js_save_note()
			}
		}
	 })
}