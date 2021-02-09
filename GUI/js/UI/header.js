export default function header(){
	var app = new Vue({
	  el: '#myhead',
	  data: {},
	  components : {
	  	'tokeHead': {
	  		template : `<center>
		  		<div class="myhead col-12 orange">
					<img src="/image/LP.png" class="tokelogo"> 
				</div>
				</center>`
	  	}
	  }
	})
}