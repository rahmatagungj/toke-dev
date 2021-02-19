export default new Vue({
	el: '#myhead',
	data: {
		show: true,
	},
	components: {
		'tokeHead': {
			template: `
		    <div class="row">
				<div class="myhead col orange">
					<img src="./image/LP.png" class="tokelogo"> 
				</div>
			</div>`
		}
	},
	methods: {
		toInfo: function(){
			console.log("info")
		},
		toGithub: function(){
			window.open('https://github.com/rahmatagungj/toke', '_blank').focus();
		},
		toPackage: function(){
			js_modal("Package","Empty")
		},
	}
})