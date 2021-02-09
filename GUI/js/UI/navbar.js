const element = '#myTab';

const data = {
	show: true,
    menuOne: ' Home',
    menuTwo: ' Encrypt',
    menuThere: ' Decrypt',
    menuFour: ' Text Editor',
    menuFive: ' Tools'};

const components = {
	'menuOne': {
  		template: '<i class="fas fa-home"></i>'
	},
	'menuTwo': {
  		template: '<i class="fas fa-lock"></i>'
	},
	'menuThere': {
  		template: '<i class="fas fa-lock-open"></i>'
	},
	'menuFour': {
  		template: '<i class="fas fa-sticky-note"></i>'
	},
	'menuFive': {
  		template: '<i class="fas fa-tools"></i>'
	}};

export default function navbar(){
		var nav = new Vue({
		  el: element,
		  data: data,
		  components: components,
	})
}