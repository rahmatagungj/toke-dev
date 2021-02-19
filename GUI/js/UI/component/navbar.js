export default new Vue({
		el: '#myTab',
		data: {
		show: true,
		menuOne: ' Home',
		menuTwo: ' Encrypt',
		menuThere: ' Decrypt',
		menuFour: ' Text Editor',
		menuFive: ' Tools'},
		components: {
		'menuOne': {
				template: '<i class="fas fa-home hvr-grow"></i>'
		},
		'menuTwo': {
				template: '<i class="fas fa-lock hvr-grow"></i>'
		},
		'menuThere': {
				template: '<i class="fas fa-lock-open hvr-grow"></i>'
		},
		'menuFour': {
				template: '<i class="fas fa-sticky-note hvr-grow"></i>'
		},
		'menuFive': {
				template: '<i class="fas fa-tools hvr-grow"></i>'
		}
	},
})